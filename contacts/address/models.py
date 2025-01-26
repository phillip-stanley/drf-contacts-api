from django.db import models
from django.core.validators import RegexValidator


class Address(models.Model):
    postcode_regex = RegexValidator(
        regex=f'([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})',
        message="Invalid postcode"
    )

    address_line_one = models.CharField(max_length=255, blank=False)
    address_line_two = models.CharField(max_length=255, blank=True)
    town_or_city = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(validators=[postcode_regex], max_length=255, blank=True)
    county = models.CharField(max_length=255, blank=True)


# Create your models here.
class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=f'^\+?1?\d{9,15}$',
        message="Invalid phone number"
    )

    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=False)
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    primary_email = models.CharField(max_length=255, blank=False) 
    secondary_email = models.CharField(max_length=255, blank=False) 
    addresses = models.ManyToManyField(Address)


