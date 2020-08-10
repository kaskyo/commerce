from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LotForm, BidForm, CommentForm
import datetime

from .models import User, Lot, Bid, Comment


def index(request, category=None):
    if category is None:
        lots = Lot.objects.filter(status="Open").order_by('-last_bump')
        return render(request, "auctions/index.html", {
            'active_lots': lots,
        })
    else:
        lots = Lot.objects.filter(status="Open", category=category).order_by('-last_bump')
        return render(request, "auctions/index.html", {
            'active_lots': lots,
            'category': category
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def lot(request, lot_id):
    lot = Lot.objects.get(id=lot_id)
    if 'Close' in request.POST:
        lot.status = 'Closed'
        lot.save()
    if 'watch' in request.POST:
        lot.watchlist.add(request.user)
        lot.save()
    elif 'unwatch' in request.POST:
        lot.watchlist.remove(request.user)
        lot.save()
    if lot.end <= datetime.datetime.now(lot.end.tzinfo) and lot.status == 'Open' :
        lot.status = 'Closed'
        lot.save()
    if 'bid' in request.POST and lot.status == 'Open':
        bid_form = BidForm(request.POST)
    else:
        bid_form = BidForm(None)
    if 'comment' in request.POST:
        comment_form = CommentForm(request.POST)
    else:
        comment_form = CommentForm(None)
    if request.method == 'POST':
        if bid_form.is_valid() and lot.status == 'Open':
            bid = bid_form.save(commit=False)
            bid.username = request.user
            bid.lot_id = lot
            bid.save()
        elif comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.username = request.user
            comment.lot_id = lot
            comment.save()
    bids = Bid.objects.filter(lot_id=lot_id).order_by('-value')
    winner = 'noone'
    if bids.exists():
        if lot.status == 'Open':
            if lot.max_bid < bids[0].value:
                lot.max_bid = bids[0].value
                lot.save()
        winner = bids[0].username
    comments = Comment.objects.filter(lot_id=lot_id).order_by('-time')
    if Lot.objects.filter(watchlist=request.user, id=lot_id).exists():
        toggle = 'unwatch'
    else:
        toggle = 'watch'
    creator = lot.username == request.user
    return render(request, "auctions/lot.html", {
        'lot': lot,
        'bids': bids,
        'comments': comments,
        'bid_form': bid_form,
        'comment_form': comment_form,
        'button': toggle,
        'creator': creator,
        'winner': winner
        })


def new(request):
    form = LotForm(request.POST or None)    
    if request.method == 'POST':
        lot = form.save(commit=False)
        lot.username = request.user
        lot.end = datetime.datetime.now() + datetime.timedelta(days=lot.length)
        lot.max_bid = form.cleaned_data['starting_bid']
        lot.save()
        return redirect("lot", lot_id=lot.id)
    else:
        return render(request, "auctions/new.html", {
            'form': LotForm()
        })


def categories(request):
    lots = Lot.objects.distinct('category').filter(status='Open')
    return render(request, "auctions/categories.html", {
        'active_lots': lots,
    })


@login_required
def watchlist(request):
    lots = Lot.objects.filter(watchlist=request.user)
    return render(request, "auctions/watchlist.html", {
        'active_lots': lots,
    })

