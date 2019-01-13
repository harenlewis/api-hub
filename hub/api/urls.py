from django.conf.urls import url

from .views import (
    ProjectCreateAPIView,
)

urlpatterns = [
    url(r'^projects?/?$',
        ProjectCreateAPIView.as_view(), name='create-project'),
]
