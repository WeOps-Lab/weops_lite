from rest_framework import serializers

from apps.system_mgmt.models.menu_manage import MenuManage


class MenuManageModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False, format='%Y-%m-%d %H:%M:%S')
    updated_at = serializers.DateTimeField(required=False, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = MenuManage
        fields = "__all__"
