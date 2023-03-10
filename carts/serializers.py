from .models import Cart
from rest_framework import serializers
from utils.fields.cart_fields import CartFields as CF
from utils.functions.products import get_products


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart

        fields = CF.fields
        read_only_fields = CF.read_only_fields
        extra_kwargs = CF.extra_kwargs

    def update(self, instance, validated_data):
        products = validated_data.pop("products")

        cart = Cart.objects.get(id=instance.cart.id)

        products_instances = get_products(products)
        cart.products.set(products_instances)
        instance.save()
        return instance


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
