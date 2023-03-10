from . import views
from django.urls import path


# urlpatterns = [path(...), path(...)]
urlpatterns = []

urlpatterns = [
    path("cart/", views.CartDetailView.as_view()),
]
