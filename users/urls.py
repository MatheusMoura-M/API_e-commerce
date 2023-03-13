from . import views
from django.urls import path
from orders import views as orders_view
from rest_framework_simplejwt import views as jwt_views


users_patterns = [
    path("users/", views.UserView.as_view()),
    path("users/<uuid:user_id>/", views.UserDetailView.as_view()),
]

orders_patterns = [path("users/orders/", orders_view.OrderUserView.as_view())]

login_patterns = [path("login/", jwt_views.TokenObtainPairView.as_view())]

urlpatterns = users_patterns + orders_patterns + login_patterns
