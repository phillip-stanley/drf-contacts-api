from factory import Faker
from factory.django import DjangoModelFactory

from contacts.address.models import Contact


class ContactFactory(DjangoModelFactory):
    class Meta:
        model = Contact

    first_name = Faker("first_name")
    last_name = Faker("last_name")
    primary_phone_number = Faker("phone_number")
    primary_email = Faker("email")
