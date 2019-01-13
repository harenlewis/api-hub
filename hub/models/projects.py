import os
import uuid

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from rest_framework.reverse import reverse


class Project(models.Model):
    class Meta:
        app_label = 'hub'
        db_table = 'hub_projects'
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    name = models.CharField(max_length=256,
                            help_text=_('Project name'),
                            )

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)

    # audit fields
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='created_projects')

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='projects_screens',
                                    null=True,
                                    blank=True)

    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return '%s' % (self.name)
