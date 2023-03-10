from django.shortcuts import get_object_or_404
from .models import Cart
from users.models import User
from rest_framework import generics
from .serializers import CartSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.permissions import AdminPermissions, AdminOrClientPermissions
from rest_framework.permissions import IsAuthenticated


class CartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminPermissions]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CartSerializer
    pagination_class = None

    # TODO: create a retrieve for self.request.user

    def get_queryset(self):
        # user = get_object_or_404(User, id=self.kwargs.get("pk"))

        return Cart.objects.filter(user=self.request.user)

    # def perform_update(self, serializer):
    #     user = get_object_or_404(User, id=self.kwargs.get("pk"))

    #     serializer.save(user=user)
