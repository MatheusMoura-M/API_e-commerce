from .models import Cart
from rest_framework import generics
from .serializers import CartSerializer
from utils.permissions import AdminPermissions
from rest_framework.views import Response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminPermissions]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        user = request.user

        cart = Cart.objects.get(user=user)

        serializer = self.serializer_class(cart)

        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        user = request.user

        cart = Cart.objects.get(user=user)

        serializer = self.serializer_class(cart, request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        user = request.user

        cart = Cart.objects.get(user=user)

        cart.products.clear()

        return Response(status=status.HTTP_204_NO_CONTENT)
