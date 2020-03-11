from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name = "ShopHome"),
     path("about/", views.about, name = "AboutUs"),
      path("tracker/", views.tracker, name = "Tracker"),
       path("contact/", views.contact, name = "ContactUs"),
        path("productView/", views.productView, name = "ProductView"),
     path("search/", views.search, name = "Search"),
     path("checkout/", views.checkout, name = "Checkout"),
]