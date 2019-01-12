from rest_framework import serializers

from . import UserInfoSerializer
from screens.models import Screen


class ScreenSerializer(serializers.ModelSerializer):
    created_by = UserInfoSerializer(read_only=True)
    user = UserInfoSerializer(read_only=True)

    class Meta:
        model = Screen
        fields = [
                  'id',
                  'screen_name',
                  'created_by',
                  'created_at',
                  'modified_by',
                  'modified_at',
                ]

        read_only_fields = ['gallery', 'user', 'created_by', 'created_at',
                            'account', 'role_name', 'modified_by',
                            'modified_at']

    def get_user_role(self, obj):
        return obj.get_role_display()