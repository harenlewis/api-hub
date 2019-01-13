from rest_framework import serializers

from hub.models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'uuid',
            'created_by',
            'created_at',
            'modified_by',
            'modified_at',
        ]

        read_only_fields = ['uuid', 'created_by', 'created_at', 'modified_by',
                            'modified_at', ]
