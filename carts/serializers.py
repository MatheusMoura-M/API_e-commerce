from .models import Cart
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart

    def create(self, validated_data):
        return super().create(validated_data)
