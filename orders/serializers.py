from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order

    def create(self, validated_data):
        return super().create(validated_data)
