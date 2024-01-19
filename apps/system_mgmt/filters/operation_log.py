from django_filters import FilterSet, CharFilter, DateTimeFromToRangeFilter

from apps.system_mgmt.models.operation_log import OperationLog


class OperationLogFilter(FilterSet):
    operator = CharFilter(field_name="operator", lookup_expr="icontains", label="操作者")
    operate_type = CharFilter(field_name="operate_type", lookup_expr="exact", label="操作行为")
    create_time = DateTimeFromToRangeFilter(field_name="created_at", lookup_expr="range", label="创建时间区间")

    class Meta:
        models = OperationLog
        fields = ["operator", "operate_type", "create_time"]
