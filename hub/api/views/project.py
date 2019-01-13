from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.db.transaction import atomic

from hub.api.serializers import ProjectSerializer
from hub.api.pagination import StandardResultsPagination


class ProjectCreateAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsPagination

    @atomic
    def post(self, request, *args, **kwargs):
        """
        Create a project.
        Request Data:
            - name: string

        Response:
        {
            "id": 78,
            "name": "Dummy Proj",
            "uuid": "8e767e81-1cb7-40b2-87aa-ad359a43c4e4",
            "created_by": "John Doe",
            "created_at": "2019-01-14T23:08:20",
            "modified_by": "John Doe",
            "modified_at": "2019-01-14T23:08:20",
        }
        """
        serializer = ProjectSerializer(data=request.data,
                                       context={'request': request}
                                       )
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.validated_data['created_by'] = request.user
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
