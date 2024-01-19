from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.system_mgmt.filters.operation_log import OperationLogFilter
from apps.system_mgmt.models.operation_log import OperationLog
from apps.system_mgmt.serializers.operation_log import OperationLogSer


class OperationLogViewSet(ListModelMixin, GenericViewSet):

    queryset = OperationLog.objects.all()
    serializer_class = OperationLogSer
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]
    filter_class = OperationLogFilter
