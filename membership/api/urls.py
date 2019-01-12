from django.conf.urls import url

from .views import (
    UserRegistrationView,
    UserAuthView
)

urlpatterns = [
    url(r'^register?/?$',
        UserRegistrationView.as_view(), name='register-user'),
    
    url(r'^auth?/?$',
        UserAuthView.as_view(), name='user-auth'),
]
