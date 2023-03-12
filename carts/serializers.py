from .models import Cart
from rest_framework import serializers
from utils.functions.products import get_products
from utils.fields.cart_fields import CartFields as CF
from products.serializers import ProductOmitStockSerializer


class CartSerializer(serializers.ModelSerializer):
    products = ProductOmitStockSerializer(many=True)

    class Meta:
        model = Cart

        fields = CF.fields
        read_only_fields = CF.read_only_fields
        extra_kwargs = CF.extra_kwargs

    def update(self, instance: Cart, validated_data: dict):
        products = validated_data.pop("products")

        products_instances = get_products(products)

        instance.products.set(products_instances)

        instance.save()
        return instance


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
