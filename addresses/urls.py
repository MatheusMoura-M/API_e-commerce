from . import views
from django.urls import path


urlpatterns = [
    path("address/", views.AddressView.as_view()),
    path("address/<uuid:address_id>/", views.AddressDetailView.as_view()),
]
