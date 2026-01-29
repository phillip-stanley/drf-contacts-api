import pytest
from django.contrib.auth.models import User
from django.db import IntegrityError, models
from rest_framework.reverse import reverse
from rest_framework.test import force_authenticate

from contacts.address.models import Address, Contact
from contacts.address.views import ContactsViewSet

# test model creation
# test created_at and updated_at dates update on save / publish
# test default user when none supplied
# test authenticated user when one provided
# test unique constraint is enforced.


@pytest.mark.django_db
class TestContactModel:
    def test_first_and_last_name_unique_constraint(self, test_user):
        """
        Given a contact in the data based with a `first_name` and `last_name`
        When a user tries to create a second contact with the same `first_name` and `last_name`
        Then an `IntegretyError` will be raised
        """
        # Given
        Contact.objects.create(
            first_name="John",
            last_name="Doe",
            primary_email="john1@example.com",
            owner=test_user,
        )

        # When / Then
        with pytest.raises(IntegrityError):
            Contact.objects.create(
                first_name="John",
                last_name="Doe",
                primary_email="john2@example.com",
                owner=test_user,
            )
