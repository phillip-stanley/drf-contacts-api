from django.db import models
from django.core.validators import RegexValidator


class Address(models.Model):
    postcode_regex = RegexValidator(
        regex=f'([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})',
        message="Invalid postcode"
    )

    address_label = models.CharField(
        max_length=4,
        choices=(('HOME', 'Home'), ('WORK', 'Work')),
        blank=False,
        default='HOME',
    )
    address_line_one = models.CharField(max_length=255, blank=False)
    address_line_two = models.CharField(max_length=255, blank=True)
    town_or_city = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(validators=[postcode_regex], max_length=255, blank=True)
    county = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.postcode}"

    class Meta:
        models.UniqueConstraint(
            fields=["postcode", "address_label"],
            name="unique_postcode_and_label"
        )


class ContactManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name):
        return self.get(first_name=first_name, last_name=last_name)


# Create your models here.
class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=f'^\+?1?\d{9,15}$',
        message="Invalid phone number"
    )

    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=True)
    #primary_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    primary_phone_number = models.CharField(max_length=17, blank=True)
    secondary_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    primary_email = models.CharField(max_length=255, blank=False) 
    secondary_email = models.CharField(max_length=255, blank=True) 
    addresses = models.ManyToManyField(Address)

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
