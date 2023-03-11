from urllib import response
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from carts.models import Cart
from rest_framework.views import APIView, Request, Response
from users.models import User
from .models import Order
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
   
    def perform_create(self, serializer):
        user = User.objects.get(email__iexact=self.request.user.email)
        
        cart = Cart.objects.get(user=user)
        
        products = cart.products.all()
        orders = []
        
        for product in products:
            
            if not product.is_active or product.stock == 0:
                raise NotFound("The product is out of stock or not found in the database")
                
            product.stock -= 1
            product.save()
            if len(orders) == 0:
                order_create = {
                    "client": user,
                    "seller": product.user,
                    "products": [product]
                }
                
                orders.append(order_create)
            else:           
                for order in orders:
                    if product.user.id == order["seller"].id: 
                        order["products"].append(product) 
                    else:
                        order_create = {
                            "client": user,
                            "seller": product.user,
                            "products": [product]
                        }
                        orders.append(order_create)
        for order in orders:
            serializer.save(client=order["client"], seller=order["seller"], products=order["products"])       
        return super().perform_create(serializer)
