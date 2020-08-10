from django.forms import ModelForm
from .models import User, Lot, Bid, Comment

class LotForm(ModelForm): 
    class Meta:
        model = Lot
        fields = ['title', 'category', 'description', 'image', 'starting_bid', 'length']

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['value']
        labels = {
            'value': '',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['description']
        labels = {
            'description': '',
        }