from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass




class Listing(models.Model):
    item_name = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    image = models.URLField(blank=True, null=True)
    category = models.CharField(blank=True, null=True, max_length=64)
    current_price = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="myListings")
    current_winner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    running = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.item_name}: {self.description} ({self.current_price})"


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist_owner")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchlist_items")

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid_owner")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bid_item")
    offer = models.DecimalField(max_digits=20, decimal_places=2)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_owner")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comment_items")
    comment = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.user} says '{self.comment}'"

