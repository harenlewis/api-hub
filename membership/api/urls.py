from django.conf.urls import url

from .views import (
    UserRegistrationView
)

urlpatterns = [
    url(r'^register?/?$',
        UserRegistrationView.as_view(), name='register-user'),
]
