from .models import Product
from rest_framework import serializers
from utils.fields.product_fields import ProductFields, ProductOmitStockFields


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = ProductFields.fields
        read_only_fields = ProductFields.read_only_fields

    def create(self, validated_data):
        if validated_data["stock"] == 0:
            validated_data["is_active"] = False

        return Product.objects.create(**validated_data)

    def update(self, instance: Product, validated_data: dict) -> Product:
        for key, value in validated_data.items():
            if key != "stock":
                setattr(instance, key, value)
            elif value == 0:
                instance.is_active = False
                setattr(instance, key, value)
            else:
                instance.is_active = True
                setattr(instance, key, value)

        instance.save()
        return instance


class ProductOmitStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

        fields = ProductOmitStockFields.fields
        read_only_fields = ProductOmitStockFields.read_only_fields
