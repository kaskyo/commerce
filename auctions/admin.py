from django.contrib import admin
from .models import User, Lot, Bid, Comment

# Register your models here.

admin.site.register(User)
admin.site.register(Lot)
admin.site.register(Bid)
admin.site.register(Comment)