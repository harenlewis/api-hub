from django.conf.urls import url

from .views import (
    ProjectCreateAPIView,
    ApiCreateView
)

from hub.api.views.hub import api_hub_view

urlpatterns = [
    url(r'^projects?/?$',
        ProjectCreateAPIView.as_view(), name='create-project'),
    
    url(r'^projects/(?P<project_id>\d+)/hub?/?$',
        ApiCreateView.as_view(), name='create-project-api'),

    # url(r'^mock/(?P<path>.*)?/?$',
    #     ApiHubView.as_view(), name='api-hub'),
    
    url(r'^mock/(?P<path>.*)?/?$', api_hub_view, name='api-hub'),
]
