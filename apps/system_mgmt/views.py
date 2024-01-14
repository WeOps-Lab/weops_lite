from auditlog.models import LogEntry
from rest_framework import viewsets

from apps.system_mgmt.filters import LogEntryFilter
from apps.system_mgmt.serializers import LogEntrySerializer


class LogEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    filterset_class = LogEntryFilter
