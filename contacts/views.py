from rest_framework.mixins import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from contacts.serializers import (
    ContactsTokenObtainPairSerializer,
    RegistrationSerializer
)


# Login User
class ContactsTokenObtainPairView(TokenObtainPairView):
    serializer_class = ContactsTokenObtainPairSerializer



# Registration View
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'User registered successfully'
            }, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

