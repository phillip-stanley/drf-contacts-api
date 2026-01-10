import pytest
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import force_authenticate
from django.db import models
from contacts.address.models import Address, Contact
from contacts.address.views import ContactsViewSet

# test model creation
# test created_at and updated_at dates update on save / publish
# test default user when none supplied
# test authenticated user when one provided
# test unique constraint is enforced.

@pytest.mark.django_db
class TestContactModel:
    def test_contact_model_creates_successfully(self, contact_factory, api_client):
        """
        Given
        When
        Then
        """
        pass
