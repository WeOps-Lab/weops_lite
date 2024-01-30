from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.drf_utils import CustomPageNumberPagination
from apps.core.utils.web_utils import WebUtils
from apps.system_mgmt.filters.operation_log import OperationLogFilter
from apps.system_mgmt.models.operation_log import OperationLog
from apps.system_mgmt.serializers.operation_log import OperationLogSer


class OperationLogViewSet(ListModelMixin, GenericViewSet):
    queryset = OperationLog.objects.all()
    serializer_class = OperationLogSer
    ordering_fields = ["created_at"]
    ordering = ["-created_at"]
    filter_class = OperationLogFilter
    pagination_class = CustomPageNumberPagination

    @uma_permission("operation_log_list")
    def list(self, request, *args, **kwargs):
        results = super().list(request, *args, **kwargs)
        return WebUtils.response_success(results.data)
