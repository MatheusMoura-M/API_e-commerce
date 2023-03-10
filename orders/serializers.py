from users.models import User
from utils.fields.order_fields import OrderFields
from .models import Order
from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings


class OrderSerializer(serializers.ModelSerializer):

    def update(self, instance: Order, validated_data: dict) -> Order:
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
            send_mail(
                subject='Pedido Alterado',
                message=['Pedido Alterado com sucesso para', Order.status],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[User.email],
                fail_silently=False
            )
            instance.save()
        # shell do Django

            return instance
     
    class Meta:
        model = Order
        fields = OrderFields.fields
        read_only_fields = OrderFields.read_only_fields

        