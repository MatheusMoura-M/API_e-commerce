from utils.fields.user_fields import UserFields as UF
from rest_framework import serializers
from addresses.models import Address
from carts.models import Cart
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = UF.fields
        read_only_fields = UF.read_only_fields
        extra_kwargs = UF.extra_kwargs

    def create(self, validated_data: dict) -> User:
        # address_data = validated_data.pop["address"]
        # address = Address.objects.create(address_data)
        # cart = Cart.objects.create()

        instance = User.objects.create_user(**validated_data)
        return instance

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()
        return instance
