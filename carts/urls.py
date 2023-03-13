from . import views
from django.urls import path

urlpatterns = [path("cart/", views.CartDetailView.as_view()), path("carts/", views.CartView.as_view())]
