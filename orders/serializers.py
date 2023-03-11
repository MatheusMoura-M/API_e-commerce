from carts.models import Cart
from products.models import Product
from products.serializers import ProductOmitStockSerializer
from users.models import User
from utils.fields.order_fields import OrderFields
from .models import Order
from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings


class OrderSerializer(serializers.ModelSerializer):
    products = ProductOmitStockSerializer(many=True, required=False)
    
    class Meta:
        model = Order
        fields = OrderFields.fields
        read_only_fields = OrderFields.read_only_fields

    def create(self, validated_data):
        
        client = validated_data.pop("client")
        seller = validated_data.pop("seller")
        products = validated_data.pop("products")
        instance_order = Order.objects.create(seller=seller, client=client) 
        instance_order.products.set(products)
        instance_order.save()
                
        return instance_order

    # def update(self, instance: Order, validated_data: dict) -> Order:
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)

    #         send_mail(
    #             subject="Pedido Alterado",
    #             message=["Pedido Alterado com sucesso para", Order.status],
    #             from_email=settings.EMAIL_HOST_USER,
    #             recipient_list=[User.email],
    #             fail_silently=False,
    #         )
    #         instance.save()
    #         # shell do Django

    #         return instance
