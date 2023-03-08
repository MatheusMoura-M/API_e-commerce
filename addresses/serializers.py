from .models import Address
from utils.fields.address_fields import AddressFields
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address

        fields = AddressFields.fields
        read_only_fields = AddressFields.read_only_fields
