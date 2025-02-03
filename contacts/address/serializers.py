from rest_framework import serializers
from rest_framework.utils import serializer_helpers

from .models import Contact, Address


class AddressSerializer(serializers.ModelSerializer):
    """"""
    address_line_one = serializers.CharField(max_length=255, allow_blank=False)
    address_line_two = serializers.CharField(max_length=255, allow_blank=True)
    town_or_city = serializers.CharField(max_length=255, allow_blank=True)
    postcode = serializers.CharField(max_length=255, allow_blank=True)
    county = serializers.CharField(max_length=255, allow_blank=True)

    class Meta:
        model = Address
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    """"""
    first_name = serializers.CharField(max_length=100, allow_blank=False)
    last_name = serializers.CharField(max_length=100, allow_blank=False)
    middle_name = serializers.CharField(max_length=100, allow_blank=False)
    mobile_number = serializers.CharField(max_length=17, allow_blank=False)
    primary_email = serializers.CharField(max_length=255, allow_blank=False)
    secondary_email = serializers.CharField(max_length=255, allow_blank=True)

    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'


