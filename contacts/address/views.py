from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import ContactsSerializer
from .models import Contact

# Create your views here.
class ContactViewSet(viewsets.ViewSet):
    """
    A simple viewset for listing or retrieving contacts.
    """
    def list(self, request):
        queryset = Contact.objects.all()
        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data)
