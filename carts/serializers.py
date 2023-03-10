from .models import Cart
from rest_framework import serializers
from utils.fields.cart_fields import CartField as CF
from products.models import Product
from rest_framework.exceptions import NotFound


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart

        fields = CF.fields
        read_only_fields = CF.read_only_fields
        extra_kwargs = CF.extra_kwargs

    def update(self, instance, validated_data):
        products = validated_data.pop("products")

        products_instances = []

        for product in products:
            try:
                prod = Product.objects.get(name_iexact=product.name)

                products_instances.append(prod)

            except Product.DoesNotExist:
                raise NotFound("Product not found.")

        instance.products.set(products_instances)
        instance.save()
        return instance
