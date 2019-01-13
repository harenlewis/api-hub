from rest_framework import serializers

from hub.models import APIPermissions


class APIPermissionsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    project = serializers.SerializerMethodField()
    permission = serializers.SerializerMethodField()

    class Meta:
        model = APIPermissions
        fields = [
            'id',
            'user',
            'permission',
            'project',
            'created_by',
            'created_at',
            'modified_by',
            'modified_at',
        ]

        read_only_fields = ['created_by', 'created_at', 'modified_by',
                            'modified_at', ]

    def get_user(self, obj):
        return obj.user.username

    def get_created_by(self, obj):
        return obj.created_by.username

    def get_project(self, obj):
        return obj.project.name

    def get_permission(self, obj):
        return obj.get_permission_display()
    