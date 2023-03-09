from utils.fields.order_fields import OrderFields
from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):

    def update(self, instance: Order, validated_data: dict) -> Order:
        
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
     
    class Meta:
        model = Order
        fields = OrderFields.fields
        read_only_fields = OrderFields.read_only_fields

        