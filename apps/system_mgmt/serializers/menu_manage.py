from rest_framework.serializers import ModelSerializer

from apps.system_mgmt.models.menu_manage import MenuManage


class MenuManageModelSerializer(ModelSerializer):
    class Meta:
        model = MenuManage
        fields = "__all__"
