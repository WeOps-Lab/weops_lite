from rest_framework.serializers import ModelSerializer

from apps.system_mgmt.models.operation_log import OperationLog


class OperationLogSer(ModelSerializer):
    class Meta:
        model = OperationLog
        fields = "__all__"
