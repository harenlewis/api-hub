# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-01-13 13:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.URLField(help_text='The path for the api')),
                ('method', models.IntegerField(choices=[(100, 'GET'), (200, 'POST'), (300, 'PUT'), (400, 'DELETE')], db_index=True, help_text='Method of the API')),
                ('res_type', models.IntegerField(choices=[(100, 'GET'), (200, 'POST'), (300, 'PUT'), (400, 'DELETE')], db_index=True, help_text='Response type of the API')),
                ('res_body', models.IntegerField(choices=[(500, 'JSON'), (600, 'HTML'), (700, 'TEXT')], db_index=True, help_text='Response of the API')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_apis', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_apis', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hub_api',
                'verbose_name': 'Api',
                'verbose_name_plural': 'Apis',
            },
        ),
        migrations.CreateModel(
            name='APIPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.IntegerField(choices=[(100, 'CREATE'), (200, 'READ'), (300, 'UPDATE'), (400, 'DELETE')], db_index=True, help_text='Permission of the user on an API')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_permissions', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_permissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hub_api_permissions',
                'verbose_name': 'APIPermission',
                'verbose_name_plural': 'APIPermissions',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Project name', max_length=256)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_projects', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects_screens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'hub_projects',
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AddField(
            model_name='apipermissions',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='hub.Project'),
        ),
        migrations.AddField(
            model_name='apipermissions',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_permissions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='api',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='hub.Project'),
        ),
    ]
