from .models import Address
from rest_framework import serializers
from utils.fields.address_fields import AddressFields, AddressWithoutIdFields


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address

        fields = AddressFields.fields
        read_only_fields = AddressFields.read_only_fields


class AddressWithoutIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address

        fields = AddressWithoutIdFields.fields
        read_only_fields = AddressWithoutIdFields.read_only_fields
