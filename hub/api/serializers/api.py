from rest_framework import serializers

from hub.models import Api


class ApiSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    project_uuid = serializers.SerializerMethodField()

    class Meta:
        model = Api
        fields = [
            'id',
            'project_uuid',
            'path',
            'method',
            'res_type',
            'res_body',
            'created_by',
            'created_at',
            'modified_by',
            'modified_at',
        ]

        read_only_fields = ['created_by', 'created_at', 'modified_by',
                            'modified_at', ]

    def get_created_by(self, obj):
        return obj.created_by.username

    def get_project_uuid(self, obj):
        return obj.project.uuid
