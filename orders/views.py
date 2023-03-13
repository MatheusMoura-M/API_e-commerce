from .models import Order
from users.models import User
from carts.models import Cart
from rest_framework import generics
from .serializers import OrderSerializer
from rest_framework.views import Response
from rest_framework.views import Response, status
from rest_framework.permissions import IsAuthenticated
from utils.functions.orders import get_orders, create_orders
from rest_framework_simplejwt.authentication import JWTAuthentication
from utils.permissions import (
    AdminOrClientPermissions,
    AdminOrProductOwnerPermissions,
    AdminOrUserOwnerOrProductOwnerPermissions,
)


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOrClientPermissions]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        user_email = request.user.email

        user = User.objects.get(email__iexact=user_email)
        cart = Cart.objects.get(user=user)

        products = cart.products.all()

        orders_to_create = get_orders(products, user)

        created_orders = create_orders(orders_to_create)

        serializer = OrderSerializer(created_orders, many=True)

        count = len(serializer.data)

        data = {"count": count, "sellers": count, "results": serializer.data}

        cart.products.clear()
        cart.save()

        return Response(data, status=status.HTTP_201_CREATED)


class OrderDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOrProductOwnerPermissions]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = "order_id"

    def get_permissions(self):
        if self.request.method == "GET":
            return [AdminOrUserOwnerOrProductOwnerPermissions()]
        return [AdminOrProductOwnerPermissions()]


class OrderUserView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class

        order_seller = Order.objects.filter(seller=self.request.user)
        serializer_seller = serializer(order_seller, many=True)

        order_client = Order.objects.filter(client=self.request.user)
        serializer_client = serializer(order_client, many=True)

        data = {
            "orders_sold": {"count": len(order_seller), "results": serializer_seller.data},
            "orders_bought": {"count": len(order_client), "results": serializer_client.data},
        }

        return Response(data)
