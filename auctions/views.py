from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Watchlist, Bid, Comment
from .forms import NewListingForm, categories



def index(request):
    listings = Listing.objects.filter(running=True)
    return render(request, "auctions/index.html", {
        "listings": listings
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

def add_listing(request):
    if request.method == "POST":
        form = NewListingForm()
        form.title = request.POST.get('title')
        form.description = request.POST.get('description')
        form.bid = request.POST.get('bid')
        if request.POST.get('image'):
            form.image = request.POST.get('image')
        else:
            form.image = None
        if request.POST.get('category'):
            form.category = request.POST.get('category')
        else:
            form.category = ""
        listing = Listing(item_name=form.title, description=form.description,current_price=form.bid,image=form.image, category=form.category, user=request.user )
        listing.save()
        return HttpResponseRedirect(reverse("details", args=(listing.id,))) 

    else:
        form = NewListingForm()
        return render(request, "auctions/create.html", {
            "form": form
        })

def details(request, listing_id):
    listing = Listing.objects.get(pk = listing_id)
    winnerMessage = ""
    #specifies if listing is owned by user
    if listing.user == request.user:
        is_owner = "True"
    else:
        is_owner = "False"
        if not listing.running and listing.current_winner == request.user:
            winnerMessage = "You have won this auction!"
    
    #gets comments for listing
    comments = Comment.objects.filter(listing=listing)

    #gets category name
    category_name = categories[int(listing.category)-1][1]
    
    #gets bid information
    bid_list = Bid.objects.filter(listing=listing).order_by('offer')
    bid_number = len(bid_list)

    #updates watchlist if button is clicked
    if request.method == "POST":
        watchlist = request.POST.get('watchlist')       
        if watchlist == "False":
            w = Watchlist(user=request.user, listing=listing)
            w.save()
            watchlist = "True"
        else:
            w = Watchlist.objects.filter(user=request.user)
            x = w.filter(listing=listing)
            x.delete()
            watchlist = "False"
    else:
        watchlist = "False"
        if request.user.is_authenticated:
            user_watchlist = Watchlist.objects.filter(user=request.user).filter(listing=listing)
            if user_watchlist:   
                watchlist="True"
    
    #renders details page with all info
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "watchlist": watchlist,
        "owner": is_owner,
        "winnerMessage": winnerMessage,
        "comments":comments,
        "category": category_name,
        "bid_number": bid_number
    })

def bid(request, listing_id):
    offer = request.POST.get('bid')
    listing = Listing.objects.get(pk=listing_id)
    if float(offer) > listing.current_price:
        new_bid = Bid(user = request.user, listing = listing, offer=offer)
        new_bid.save()
        listing.current_price = offer
        listing.current_winner = request.user
        listing.save()
        return HttpResponseRedirect(reverse("details", args=(listing_id,))) 
    return render(request,"auctions/error.html", {
        "listing":listing_id
    })


def close(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    listing.running = False
    listing.save()
    return HttpResponseRedirect(reverse("index"))

def comment(request, listing_id):
    listing=Listing.objects.get(pk=listing_id)
    c= Comment(user=request.user, listing=listing, comment=request.POST.get('comment'))
    c.save()
    return HttpResponseRedirect(reverse("details", args=(listing_id,)))

def watchlist(request):
    items = request.user.watchlist_owner.all()
    listings = []
    for item in items:
        listings.append(item.listing)
    return render(request, "auctions/watchlist.html", {
        "listings": listings
    })

def category_list(request):
    list = []
    for category in categories:
        list.append(category[1])
    return render(request, "auctions/category_list.html", {
        "categories":list
    })


def category(request, category_name):
    for category in categories:
        if category[1] == category_name:
            id = category[0]
    listings = Listing.objects.filter(category=id).filter(running=True)
    print(listings)
    return render(request, "auctions/category_listings.html", {
        "listings": listings,
        "category": category_name
    })
