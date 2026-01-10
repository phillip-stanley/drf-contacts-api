from rest_framework import serializers
from rest_framework.utils import serializer_helpers

from django.contrib.auth.models import User

from .models import Contact, Address


class AddressSerializer(serializers.ModelSerializer):
    """
    A simple serializer for the `Address` model.
    """
    address_label= serializers.ChoiceField(
        choices=(('HOME', 'home'), ('WORK', 'work')),
        allow_blank=False,
    )
    address_line_one = serializers.CharField(max_length=255, allow_blank=False)
    address_line_two = serializers.CharField(max_length=255, allow_blank=True, required=False)
    town_or_city = serializers.CharField(max_length=255, allow_blank=True)
    postcode = serializers.CharField(max_length=255, allow_blank=True)
    county = serializers.CharField(max_length=255, allow_blank=True, required=False)

    class Meta:
        model = Address
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """
    A simple serializer for `User` model creation
    """
    class Meta:
        model = User
        fields = '__all__'


class ContactsListSerializer(serializers.ModelSerializer):
    """
    A simple serializer for `Contact` model listing without addresses
    """
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'primary_phone_number',
            'secondary_phone_number',
            'primary_email',
            'secondary_email',
        ]


class ContactsSerializer(serializers.ModelSerializer):
    """
    A simple serializer for `Contact` model listing including
    `ManyToMany` relation with `Addresses`.
    """
    first_name = serializers.CharField(max_length=100, allow_blank=False)
    last_name = serializers.CharField(max_length=100, allow_blank=False)
    middle_name = serializers.CharField(max_length=100, allow_blank=True, required=False)
    primary_phone_number = serializers.CharField(max_length=17, allow_blank=False)
    secondary_phone_number = serializers.CharField(max_length=17, allow_blank=True, required=False)
    primary_email = serializers.CharField(max_length=255, allow_blank=False)
    secondary_email = serializers.CharField(max_length=255, allow_blank=True, required=False)

    addresses = AddressSerializer(many=True, read_only=False)

    owner = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('owner')
        return representation

    def create(self, validated_data):
        addresses = validated_data.pop('addresses', [])
        contact = Contact.objects.create(**validated_data)
        for address in addresses:
            address = Address.objects.create(contact=contact, **address)
            contact.add(address)
        return contact

