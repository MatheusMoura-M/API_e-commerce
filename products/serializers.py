from .models import Product
from rest_framework import serializers
from utils.fields.product_fields import ProductFields


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = ProductFields.fields
        read_only_fields = ProductFields.read_only_fields

    def create(self, validated_data):
        if validated_data["stock"] == 0:
            validated_data["isActive"] = False

        return Product.objects.create(**validated_data)

    def update(self, instance: Product, validated_data: dict) -> Product:
        for key, value in validated_data.items():
            if key != "stock":
                setattr(instance, key, value)
            elif value == 0:
                instance.isActive = False
                instance.stock = value
            else:
                instance.isActive = True
                instance.stock = value

        instance.save()
        return instance
