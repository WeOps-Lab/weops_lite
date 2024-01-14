import django_filters
from auditlog.models import LogEntry


class LogEntryFilter(django_filters.FilterSet):
    action = django_filters.NumberFilter(field_name='action')
    actor = django_filters.CharFilter(field_name='actor__username', lookup_expr='icontains')
    timestamp = django_filters.DateFromToRangeFilter(field_name='timestamp')

    class Meta:
        model = LogEntry
        fields = ['action', 'timestamp']
