import pytest
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

from contacts.address.models import Contact
from tests.conftest import api_client

# TODO: 1. test that `includeAddresses=true` returns a contacts list.
# TODO: 2. test POST/CREATE operation create a new contact
# TODO: 3. test PUT/UPDATE operation update an email address


class TestContactViewSet:
    def test_unauthorized_user_receives_401(self, api_client):
        """
        Given an non-authenticated user
        When the contacts `GET` endpoint is called
        Then a status of 401 is returned
        """
        # Given
        url = reverse("contacts-list")  # `/api/contacts/`

        # When
        response = api_client.get(url)

        # Then
        assert response.status_code == 401
        assert response.json() == {
            "detail": "Authentication credentials were not provided."
        }

    @pytest.mark.django_db
    def test_authorized_user_receives_correct_response(
        self, api_client, contact_factory, test_user
    ):
        """
        Given there is a contact in the database for the authenticated user
        When a request is made to the contacts list endpoint with a `GET` request
        Then the correct response is returned.
        """
        # Given
        contact = contact_factory(owner=test_user)

        # When
        api_client.force_authenticate(user=test_user)
        url = reverse("contacts-list")
        response = api_client.get(url)

        # Then
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["first_name"] == contact.first_name
        assert response.data[0]["last_name"] == contact.last_name
        assert response.data[0]["primary_email"] == contact.primary_email

    @pytest.mark.django_db
    def test_returned_contacts_belong_to_authenticated_user(
        self, api_client, contact_factory, test_user
    ):
        """
        Given 2 contacts in the database with each belonging to a different user
        When an authenticated user with 1 contact in their account makes a request
        Then a single contact for that user is returned
        """
        # Given
        contact_factory(owner=test_user)
        user_two = User.objects.create_user(
            username="newuser",
            email="newuser@user.com",
        )
        user_two_contact = contact_factory(owner=user_two)
        all_contacts = Contact.objects.all()

        # When
        api_client.force_authenticate(user=user_two)
        url = reverse("contacts-list")
        response = api_client.get(url)

        # Then
        assert len(all_contacts) == 2
        assert len(response.data) == 1
        assert response.data[0]["first_name"] == user_two_contact.first_name
        assert response.data[0]["last_name"] == user_two_contact.last_name
        assert response.data[0]["primary_email"] == user_two_contact.primary_email

    @pytest.mark.django_db
    def test_authenticated_user_can_create_new_contact(self, api_client, test_user):
        """
        Given an authenticated user makes a request to the contacts-list endpoint
        When a POST call is made including a new contact in the request body
        Then a new contact is created and a 200 response is returned
        """
        # Given
        api_client.force_authenticate(user=test_user)
        valid_payload = {
            "first_name": "valid-name",
            "last_name": "valid-surname",
            "primary_phone_number": "+4477792951",
            "primary_email": "valid@email.com",
            "addresses": [],
        }

        # When
        url = reverse("contacts-list")
        response = api_client.post(url, valid_payload, format="json")
        created_id = response.data["id"]

        # Then
        new_contact = Contact.objects.get(id=created_id)

        assert response.status_code == 201
        assert response.data["first_name"] == new_contact.first_name
        assert response.data["last_name"] == new_contact.last_name
        assert response.data["primary_email"] == new_contact.primary_email
