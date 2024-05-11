from rest_framework import viewsets

from apps.cmdb_mgmt.models.change_record import ChangeRecord
from apps.cmdb_mgmt.serializers.change_record import ChangeRecordSerializer
from apps.cmdb_mgmt.filters.change_record import ChangeRecordFilter
from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.drf_utils import CustomPageNumberPagination
from apps.core.utils.web_utils import WebUtils


class ChangeRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChangeRecord.objects.all().order_by("-created_at")
    serializer_class = ChangeRecordSerializer
    filterset_class = ChangeRecordFilter
    pagination_class = CustomPageNumberPagination

    @uma_permission('change_record_list')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @uma_permission('change_record_detail')
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return WebUtils.response_success(serializer.data)
