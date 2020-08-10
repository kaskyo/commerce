from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Lot(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+',)
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    description = models.TextField()
    image = models.URLField()
    starting_bid = models.FloatField()
    max_bid = models.FloatField()
    time = models.DateTimeField(auto_now=True)
    end = models.DateTimeField()
    length = models.IntegerField()
    last_bump = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=64, default='Open')
    watchlist = models.ManyToManyField(User)
    

class Comment(models.Model):
    lot_id = models.ForeignKey(Lot, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    time = models.DateTimeField(auto_now=True)

class Bid(models.Model):
    lot_id = models.ForeignKey(Lot, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.FloatField()
    time = models.DateTimeField(auto_now=True)
