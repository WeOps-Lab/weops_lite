from rest_framework import viewsets

from apps.cmdb_mgmt.models.change_record import ChangeRecord
from apps.cmdb_mgmt.serializers.change_record import ChangeRecordSerializer
from apps.cmdb_mgmt.filters.change_record import ChangeRecordFilter
from apps.core.utils.drf_utils import CustomPageNumberPagination


class ChangeRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChangeRecord.objects.all().order_by("-created_at")
    serializer_class = ChangeRecordSerializer
    filterset_class = ChangeRecordFilter
    pagination_class = CustomPageNumberPagination