from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.add_listing, name="create"),
    path("<int:listing_id>", views.details, name="details"),
    path("bid/<int:listing_id>", views.bid, name="bid"),
    path("close/<int:listing_id>", views.close, name="close"),
    path("comment/<int:listing_id>", views.comment, name="comment"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.category_list, name="category_list"),
    path("category/<str:category_name>", views.category, name="category")
]
