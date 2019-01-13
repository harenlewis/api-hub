from rest_framework import serializers

from hub.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

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

    def get_created_by(self, obj):
        return obj.created_by.username