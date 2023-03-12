from . import views
from django.urls import path

urlpatterns = [path("orders/", views.OrderView.as_view())]
