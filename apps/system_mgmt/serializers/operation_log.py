from rest_framework import serializers

from apps.system_mgmt.models.operation_log import OperationLog


class OperationLogSer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = OperationLog
        fields = "__all__"
