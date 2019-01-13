from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from membership.models import User
from .projects import Project


class APIPermissions(models.Model):
    class Meta:
        app_label = 'hub'
        db_table = 'hub_api_permissions'
        verbose_name = _('APIPermission')
        verbose_name_plural = _('APIPermissions')

    CREATE = 100
    READ = 200
    UPDATE = 300
    DELETE = 400

    PERMISSION_TYPES = (
        (CREATE, 'CREATE'),
        (READ, 'READ'),
        (UPDATE, 'UPDATE'),
        (DELETE, 'DELETE'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='api_permissions',
                             null=True, blank=True)

    project = models.ForeignKey(Project, related_name='permissions')

    permission = models.IntegerField(db_index=True, choices=PERMISSION_TYPES,
                                     help_text=_('Permission of the user on an API'))

    # audit fields
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='created_permissions')

    created_at = models.DateTimeField(auto_now_add=True)

    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='modified_permissions',
                                    null=True,
                                    blank=True)

    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '%s, %s, %s' % (self.user.username, self.permission, self.project.name)
