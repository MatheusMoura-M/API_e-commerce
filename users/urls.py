from . import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

login_patterns = [
    path("login/", jwt_views.TokenObtainPairView.as_view()),
]

view_patterns = [
    path("users/", views.UserView.as_view()),
    path("users/<uuid:user_id>/", views.UserDetailView.as_view()),
]

urlpatterns = view_patterns + login_patterns
