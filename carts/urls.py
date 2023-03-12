from . import views
from django.urls import path

urlpatterns = [path("carts/", views.CartView.as_view()), path("cart/", views.CartDetailView.as_view())]
