import json

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from django.db.transaction import atomic
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError

from hub.models.types import METHOD_TYPES_DICT, RESP_TYPES_DICT, JSON
from hub.models import Project, Api, APIPermissions
from hub.api.serializers import ProjectSerializer
from hub.api.pagination import StandardResultsPagination


@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_hub_view(request, *args, **kwargs):
    error = {'errorMsg': ''}
    path = kwargs.get('path', '').lstrip('/').rstrip('/')
    project_uuid = request.subdomain
    user = request.user
    req_method = request.method

    if path == '' or project_uuid == '':
        error['errorMsg'] = 'Not a valid url'
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    try:
        project = Project.objects.get(uuid=project_uuid)
    except Project.DoesNotExist:
        error['errorMsg'] = 'Project or API does not exists.'
        return Response(error, status=status.HTTP_400_BAD_REQUEST)
    except ValidationError:
        error['errorMsg'] = 'Project or API does not exists.'
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    has_proj_perm = (APIPermissions
                     .objects
                     .filter(user_id=user.id, project_id=project.id)
                     .exists()
                     )

    # check if user has permission on the project to add api's
    if not (user.id == project.created_by.id or has_proj_perm):
        error['errorMsg'] = 'No permission on this project'
        return Response(error, status=status.HTTP_403_FORBIDDEN)

    method_val = METHOD_TYPES_DICT.get(req_method, None)
    if method_val is None:
        error['errorMsg'] = 'Not a valid method.'
        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    api_qs = (Api
              .objects
              .filter(project_id=project.id, path=path, method=method_val)
              )
    if not api_qs.exists():
        error['errorMsg'] = "We were unable to find any matching requests for this method type and the mock path in your projects."
        return Response(error, status=status.HTTP_403_FORBIDDEN)

    api = api_qs[0]
    content_type = RESP_TYPES_DICT.get(api.get_res_type_display(), None)
    return Response(api.res_body, content_type=content_type, status=status.HTTP_200_OK)
