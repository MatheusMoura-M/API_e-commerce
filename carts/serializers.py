from .models import Cart
from rest_framework import serializers
from utils.fields.cart_fields import CartFields
from utils.functions.products import get_products
from products.serializers import ProductOmitStockSerializer


class CartSerializer(serializers.ModelSerializer):
    products = ProductOmitStockSerializer(many=True)
    total_amount = serializers.SerializerMethodField()
    products_count = serializers.SerializerMethodField()

    def get_total_amount(self, obj: Cart):
        prices = [float(products.price) for products in obj.products.all()]

        total_string_rounded = str(round(sum(prices), 2))

        return total_string_rounded

    def get_products_count(self, obj: Cart):
        return len(obj.products.all())

    def update(self, instance: Cart, validated_data: dict):
        products = validated_data.pop("products")

        products_instances = get_products(products)

        instance.products.set(products_instances)

        instance.save()
        return instance

    class Meta:
        model = Cart

        fields = CartFields.fields
        read_only_fields = CartFields.read_only_fields
        extra_kwargs = CartFields.extra_kwargs


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
