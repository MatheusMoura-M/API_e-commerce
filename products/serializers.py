from .models import Product
from rest_framework import serializers
from utils.fields.product_fields import ProductFields


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = ProductFields.fields
        read_only_fields = ProductFields.read_only_fields

    def create(self, validated_data):
        return super().create(validated_data)
