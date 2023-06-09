from . import views
from django.urls import path


urlpatterns = [
    path("products/", views.ProductView.as_view()),
    path("products/<uuid:product_id>/", views.ProductDetailView.as_view()),
]
