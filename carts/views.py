from .models import Cart
from rest_framework import generics
from .serializers import CartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.permissions import AdminPermissions, AdminOrOwnerPermissions


class CartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminPermissions]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOrOwnerPermissions]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_url_kwarg = "cart_id"
