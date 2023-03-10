from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from carts.models import Cart
from users.models import User
from .models import Order
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from django.shortcuts import get_object_or_404


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # pagination_class = PageNumberPagination
    cart_url_kwarg = "cart_id"

    def get_queryset(self):
        cart_id = self.kwargs["cart_id"]   

        return Order.objects.filter(cart_id=cart_id)

    def perform_create(self, serializer):
        return super().perform_create(serializer)
