from django.conf.urls import url

from .views import (
    ProjectCreateAPIView,
    ApiCreateView
)

urlpatterns = [
    url(r'^projects?/?$',
        ProjectCreateAPIView.as_view(), name='create-project'),
    
    url(r'^projects/(?P<project_id>\d+)?/?$',
        ApiCreateView.as_view(), name='create-project'),
]
