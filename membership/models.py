from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _


class User(AbstractUser):
    class Meta:
        app_label = 'membership'
        db_table = 'membership_user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')