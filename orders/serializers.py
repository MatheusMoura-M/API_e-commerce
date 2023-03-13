from .models import Order
from django.conf import settings
from rest_framework import serializers
from django.core.mail import send_mail
from utils.fields.order_fields import OrderFields
from rest_framework.exceptions import ValidationError
from products.serializers import ProductOmitStockSerializer
from users.serializers import ClientSerializer, SellerSerializer


class OrderSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(required=False)
    client = ClientSerializer(required=False)
    products = ProductOmitStockSerializer(many=True, required=False)
    products_count = serializers.SerializerMethodField()

    def get_products_count(self, obj: Order):
        return len(obj.products.all())

    def update(self, instance: Order, validated_data: dict) -> Order:
        if "status" not in validated_data:
            raise ValidationError("required status field")

        setattr(instance, "status", validated_data["status"])
        instance.save()

        send_mail(
            subject="Pedido Alterado",
            message=f"Pedido Alterado com sucesso para {instance.status}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.client.email, instance.seller.email],
            fail_silently=False,
        )

        return instance

    class Meta:
        model = Order

        fields = OrderFields.fields
        read_only_fields = OrderFields.read_only_fields
