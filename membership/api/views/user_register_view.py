from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.db.transaction import atomic

from membership.models import User
from membership.forms import RegistrationForm


class UserRegistrationAPIView(APIView):
    permission_classes = ()

    @atomic
    def post(self, request, *args, **kwargs):
        """
        Registers a new user.
        Request Data:
            - username: string
            - email: string
            - password: string

        Response: Return user token for future API calls.
        {
            58fb9cf9f2d88ca678aa34407d9d22b761c36bd6
        }
        """
        error = {"errorMsg": ""}
        form = RegistrationForm(request.data)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if not User.objects.filter(username=username).exists():
                user = User.objects.create(email=email, username=username)
                user.set_password(password)
                user.save()
                token = Token.objects.create(user=user)
                return Response(token.key, status=status.HTTP_201_CREATED)
            else:
                error['errorMsg'] = "Username already exists."
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
