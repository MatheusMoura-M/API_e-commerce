from .models import User
from carts.models import Cart
from addresses.models import Address
from rest_framework import serializers
from utils.fields.user_fields import UserFields, SellerFields, ClientFields
from addresses.serializers import AddressSerializer, AddressWithoutIdSerializer
from rest_framework.exceptions import PermissionDenied


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

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
        if self.context["request"].user.is_superuser and instance.email != self.context["request"].user.email:
            if "is_seller" in validated_data:
                setattr(instance, "is_seller", validated_data["is_seller"])

                instance.save()
                return instance
            else:
                raise PermissionDenied("Cannot change user instance fields other than is_seller")

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

    class Meta:
        model = User

        fields = UserFields.fields
        read_only_fields = UserFields.read_only_fields
        extra_kwargs = UserFields.extra_kwargs


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = SellerFields.fields
        read_only_fields = SellerFields.read_only_fields
        extra_kwargs = SellerFields.extra_kwargs


class ClientSerializer(serializers.ModelSerializer):
    address = AddressWithoutIdSerializer(required=False)

    class Meta:
        model = User

        fields = ClientFields.fields
        read_only_fields = ClientFields.read_only_fields
        extra_kwargs = ClientFields.extra_kwargs
