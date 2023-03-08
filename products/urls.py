from . import views
from django.urls import path
from .views import ProductView


urlpatterns = [
    path("products/", views.ProductView.as_view()),
]
