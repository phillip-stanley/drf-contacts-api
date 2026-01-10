from django.contrib.auth.models import User
from django.db import models

from contacts.address.validators.validators import (
    validate_uk_landline,
    validate_uk_mobile,
    validate_uk_postcode,
)


class Address(models.Model):
    address_label = models.CharField(
        max_length=4,
        choices=(("HOME", "Home"), ("WORK", "Work")),
        blank=False,
        default="HOME",
    )
    address_line_one = models.CharField(max_length=255, blank=False)
    address_line_two = models.CharField(max_length=255, blank=True)
    town_or_city = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(
        validators=[validate_uk_postcode],
        max_length=255,
        blank=True,
    )
    county = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        models.UniqueConstraint(
            fields=["postcode", "address_label"], name="unique_postcode_and_label"
        )


class ContactManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name):
        return self.get(first_name=first_name, last_name=last_name)


class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=True)
    primary_phone_number = models.CharField(
        validators=[validate_uk_landline, validate_uk_mobile],
        max_length=17,
        blank=True,
    )
    secondary_phone_number = models.CharField(
        validators=[validate_uk_landline, validate_uk_mobile],
        max_length=17,
        blank=True,
    )
    primary_email = models.CharField(max_length=255, blank=False)
    secondary_email = models.CharField(max_length=255, blank=True)

    addresses = models.ManyToManyField(Address)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
    )
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    objects = ContactManager()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name"],
                name="unique_first_last_name",
            )
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
