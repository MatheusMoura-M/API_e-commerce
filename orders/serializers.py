from .models import Order
from rest_framework import serializers
from django.core.mail import send_mail
from utils.fields.order_fields import OrderFields
from products.serializers import ProductOmitStockSerializer
from users.serializers import ClientSerializer, SellerSerializer


class OrderSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(required=False)
    client = ClientSerializer(required=False)
    products = ProductOmitStockSerializer(many=True, required=False)

    class Meta:
        model = Order

        fields = OrderFields.fields
        read_only_fields = OrderFields.read_only_fields

    def create(self, validated_data: dict) -> Order:
        products = validated_data.pop("products")

        instance_order = Order.objects.create(**validated_data)

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
