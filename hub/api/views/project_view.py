from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from django.db.transaction import atomic

from hub.api.serializers import ProjectSerializer
from hub.api.pagination import StandardResultsPagination


class ProjectCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsPagination

    @atomic
    def post(self, request, *args, **kwargs):
        """
        Comment
        """
        serializer = ProjectSerializer(data=request.data,
                                       context={'request': request}
                                       )
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.validated_data['created_by'] = request.user
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
