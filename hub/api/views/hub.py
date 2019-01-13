from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.db.transaction import atomic

from hub.models import Project, Api, APIPermissions
from hub.api.serializers import ProjectSerializer
from hub.api.pagination import StandardResultsPagination


class ApiHubView(APIView):
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsPagination

    def get(self, request, *args, **kwargs):
        """
        Creates a project
        """
        pass

    @atomic
    def post(self, request, *args, **kwargs):
        """
        Creates a project
        """
        pass

    @atomic
    def put(self, request, *args, **kwargs):
        """
        Creates a project
        """
        pass

    @atomic
    def delete(self, request, *args, **kwargs):
        """
        Check for appropriate permissions and then allow the user to delete
        project.
        """
        pass
