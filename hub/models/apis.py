import json

from rest_framework.reverse import reverse

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from .types import METHOD_TYPES, RESP_TYPES, JSON
from . import Project


class Api(models.Model):
    class Meta:
        app_label = 'hub'
        db_table = 'hub_api'
        verbose_name = _('Api')
        verbose_name_plural = _('Apis')

    # GET = 100
    # POST = 200
    # PUT = 300
    # DELETE = 400

    # METHOD_TYPES = (
    #     (GET, 'GET'),
    #     (POST, 'POST'),
    #     (PUT, 'PUT'),
    #     (DELETE, 'DELETE'),
    # )

    # JSON = 500
    # HTML = 600
    # TEXT = 700

    # RESP_TYPES = (
    #     (JSON, 'JSON'),
    #     (HTML, 'HTML'),
    #     (TEXT, 'TEXT'),
    # )

    project = models.ForeignKey(Project, related_name='project')

    path = models.CharField(max_length=256, help_text=_('The path for the api'))

    method = models.IntegerField(db_index=True, choices=METHOD_TYPES,
                                 help_text=_('Method of the API'))

    res_type = models.IntegerField(db_index=True, choices=RESP_TYPES,
                                   help_text=_('Response type of the API'))

    res_body = models.TextField(help_text=_('Response of the API'))

    # audit fields
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name='created_apis')

    created_at = models.DateTimeField(auto_now_add=True)

    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    related_name='modified_apis',
                                    null=True,
                                    blank=True)

    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if self.id is None:
    #         if self.res_type == JSON:
    #             body = json.dumps(self.res_body)
    #             self.res_body = body
    #         super(Api, self).save(*args, **kwargs)

    def __str__(self):
        return '%s %s %s' % (self.project.name, self.path, self.method)
