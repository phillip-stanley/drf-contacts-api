import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APIRequestFactory
from pytest_factoryboy import register
from tests.factories import ContactFactory

@pytest.fixture
def test_user():
    """Create a test user for authentication"""
    return User.objects.create_user(
        username="testuser",
        email="testuser@admin.com",
    )

@pytest.fixture
def api_client():
    return APIClient()

register(ContactFactory)

# @pytest.fixture
# def contact_data():
#     return {
#         "first_name": "John",
#         "last_name": "Doe",
#         "middle_name": None,
#         "primary_phone_number": "07785684123",
#         "secondary_phone_number": None,
#         "primary_email": "john@gmail.com",
#         "secondary_email": None,
#         "addresses": [],
#         "owner": None,
#         "created_by": None,
#         "updated_by": None,
#     }
