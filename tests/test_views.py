import pytest
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

from tests.conftest import api_client

# 1. TODO: test an unauthenticated user receives a 401 status code
# 2. TODO: test an authenticated user receives a 200 status code
# 3. TODO: test an authenticated user receives a list of contacts that only belong to them


class TestContactViewSet:
    def test_unauthorized_user_receives_404(self, api_client):
        """
        Given a valid endpoint address is called from a non-authenticated user
        When the get method is called
        Then a status of 401 is returned
        """
        # Given
        url = reverse("contacts-list")

        # Whef
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
        When a request is made to the contacts list end point with a `GET` request
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

    # @pytest.mark.django_db
    # def test_authorized_user_receives_200(self, api_client, contact_factory):
    #     """
    #     Given a valid endpoint address is called from an authenticated user
    #     When the get method is called
    #     Then a status of 200 is returned
    #     """
    #     # Given
    #     contact = contact_factory()
    #     user, created = User.objects.get_or_create(username="phill", email="phill@user.com")
    #     contact.owner = user
    #     contact.save()
    #
    #     # When
    #     api_client.force_authenticate(user=user, token=None)
    #     url = reverse("contacts-list")
    #     response = api_client.get(url)
    #
    #     # Then
    #     assert response.status_code == 200
    #     assert response.data[0]["first_name"] == contact.first_name
