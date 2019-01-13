from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from django.db.transaction import atomic

from membership.models import User
from membership.forms import RegistrationForm


class UserAuthAPIView(ObtainAuthToken):
    permission_classes = ()

    @atomic
    def post(self, request, *args, **kwargs):
        """
        Authenticates the user and returns token for future API calls. 
        """
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        })
