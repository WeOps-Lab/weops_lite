from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet, ViewSet

from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.drf_utils import CustomPageNumberPagination
from apps.core.utils.web_utils import WebUtils
from apps.system_mgmt.filters.operation_log import OperationLogFilter
from apps.system_mgmt.models.operation_log import OperationLog
from apps.system_mgmt.serializers.operation_log import OperationLogSer


class OperationLogViewSet(ListModelMixin, GenericViewSet):
    queryset = OperationLog.objects.all().order_by("-created_at")
    serializer_class = OperationLogSer
    filterset_class = OperationLogFilter
    pagination_class = CustomPageNumberPagination

    @uma_permission("operation_log_list")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CustomOperationLogViewSet(ViewSet):
        @swagger_auto_schema(
            operation_id="operate_type_enum",
            operation_description="获取操作类型枚举值",
        )
        @action(detail=False, methods=["get"], url_path="operate_type/enum")
        @uma_permission("operate_type_enum")
        def enum(self, request):
            return WebUtils.response_success(OperationLog.OPERATE_TYPE_DICT)
