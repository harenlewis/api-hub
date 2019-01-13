from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.db.transaction import atomic
from django.shortcuts import get_object_or_404

from hub.models import Project, APIPermissions
from hub.api.serializers import ApiSerializer, APIPermissionsSerializer
from hub.api.pagination import StandardResultsPagination


class ApiCreateView(APIView):
    permission_classes = (IsAuthenticated, )
    pagination_class = StandardResultsPagination

    @atomic
    def post(self, request, *args, **kwargs):
        """
        Add an API for an project
        Request Data:
            - path: string
            - method: integer
            - res_type: integer
            - res_body: string

        Response:
        {
            "id": 78,
            "project": "Dummy Project",
            "path": "some/path",
            "method": 100,
            "res_type": 600,
            "res_body": "<p>Hey there</p>",
            "created_by": "John Doe",
            "created_at": "2019-01-14T23:08:20",
            "modified_by": "John Doe",
            "modified_at": "2019-01-14T23:08:20",
        }
        """
        user = request.user
        error = {'errorMsg': ''}
        project_id = kwargs.get('project_id', None)

        serializer = ApiSerializer(data=request.data,
                                   context={'request': request}
                                   )

        # if request data is not proper
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if project_id is None:
            error['errorMsg'] = 'Project not found'
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        project = get_object_or_404(Project, pk=project_id)

        has_proj_perm = (APIPermissions
                         .objects
                         .filter(user_id=user.id, project_id=project_id)
                         .exists()
                         )

        # check if user has permission on the project to add api's
        if not (user.id == project.created_by.id or has_proj_perm):
            error['errorMsg'] = 'No permission on this project'
            return Response(error, status=status.HTTP_403_FORBIDDEN)

        path = serializer.validated_data['path']
        serializer.validated_data['path'] = path.lstrip('/').rstrip('/')
        serializer.validated_data['project'] = project
        serializer.validated_data['created_by'] = request.user
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
