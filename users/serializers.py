from .models import User
from carts.models import Cart
from addresses.models import Address
from rest_framework import serializers
from addresses.serializers import AddressSerializer
from utils.fields.user_fields import UserFields as UF, SellerFields as SF, ClientFields as CF


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


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = SF.fields
        read_only_fields = SF.read_only_fields
        extra_kwargs = SF.extra_kwargs


class ClientSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)

    class Meta:
        model = User

        fields = CF.fields
        read_only_fields = CF.read_only_fields
        extra_kwargs = CF.extra_kwargs
