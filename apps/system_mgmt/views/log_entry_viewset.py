from auditlog.models import LogEntry
from rest_framework import viewsets

from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.drf_utils import CustomPageNumberPagination
from apps.system_mgmt.filters.log_entry_filter import LogEntryFilter
from apps.system_mgmt.serializers.log_entry_serializer import LogEntrySerializer


class LogEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    filterset_class = LogEntryFilter
    pagination_class = CustomPageNumberPagination

    @uma_permission('log_entry_retrieve')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @uma_permission('log_entry_list')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
