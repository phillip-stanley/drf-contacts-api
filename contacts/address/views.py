from typing import Type
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Serializer

from .serializers import ContactsSerializer, ContactsListSerializer
from .models import Contact


class ContactsViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for listing or displaying contacts.
    """
    serializer_class = ContactsListSerializer
    queryset = Contact.objects.all()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_map = {
        'list': ContactsListSerializer,
        'create': ContactsSerializer,
        'update': ContactsSerializer,
        'partial_update': ContactsSerializer,
    }

    def get_serializer_class(self) -> Type[Serializer]:
        if self.request.query_params.get('includeAddresses', '') == 'true':
            return ContactsSerializer

        return self.serializer_map.get(self.action, self.serializer_class)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user) 
