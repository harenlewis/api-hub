from django.conf.urls import url

from .views import (
    UserRegistrationAPIView,
    UserAuthAPIView
)

urlpatterns = [
    url(r'^register?/?$',
        UserRegistrationAPIView.as_view(), name='register-user'),
    
    url(r'^auth?/?$',
        UserAuthAPIView.as_view(), name='user-auth'),
]
