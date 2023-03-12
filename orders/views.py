from .models import Order
from users.models import User
from carts.models import Cart
from rest_framework import generics
from .serializers import OrderSerializer
from rest_framework.views import Response
from utils.functions.orders import get_orders
from utils.permissions import AdminOrClientPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOrClientPermissions]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        user = User.objects.get(email__iexact=self.request.user.email)
        cart = Cart.objects.get(user=user)

        products = cart.products.all()
        orders = get_orders(products, user)

        instances = []
        for order in orders:
            instance = serializer.save(client=order["client"], seller=order["seller"], products=order["products"])
            instances.append(instance)

        cart.products.clear()
        cart.save()

        return Response(instances)
