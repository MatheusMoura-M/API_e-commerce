from . import views
from django.urls import path

urlpatterns = [
    path("orders/", views.OrderView.as_view()),
    path("orders/<uuid:order_id>/", views.OrderDetailView.as_view()),
]
