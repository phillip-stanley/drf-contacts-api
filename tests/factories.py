import factory
from factory.django import DjangoModelFactory
from contacts.address.models import Address, Contact, User

class ContactFactory(DjangoModelFactory):
    class Meta:
        model = Contact

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    primary_phone_number = factory.Faker('phone_number')
    primary_email = factory.Faker('email')