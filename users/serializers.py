from django.shortcuts import get_object_or_404
from utils.fields.user_fields import UserFields as UF
from rest_framework import serializers
from addresses.models import Address
from carts.models import Cart
from .models import User
from addresses.serializers import AddressSerializer
from carts.serializers import CartSerializer
import ipdb


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = User

        fields = UF.fields
        read_only_fields = UF.read_only_fields
        extra_kwargs = UF.extra_kwargs

    def create(self, validated_data: dict) -> User:
        address_data = validated_data.pop("address")

        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address = address_serializer.save()

        cart = Cart.objects.create()

        validated_data["address"] = address
        validated_data["cart"] = cart

        instance = User.objects.create_user(**validated_data)

        return instance

    def update(self, instance: User, validated_data: dict) -> User:
        if "address" in validated_data:
            address_data = validated_data["address"]
            address = Address.objects.get(id=instance.address.id)

            for key, value in address_data.items():
                setattr(address, key, value)
            address.save()

            instance.address = address

        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            elif key != "address":
                setattr(instance, key, value)

        instance.save()
        return instance
