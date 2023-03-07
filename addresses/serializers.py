from .models import Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address

    def create(self, validated_data):
        return super().create(validated_data)
