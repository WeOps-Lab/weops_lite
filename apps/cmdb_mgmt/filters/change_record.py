from django_filters import FilterSet, CharFilter, DateTimeFromToRangeFilter, NumberFilter

from apps.cmdb_mgmt.models.change_record import ChangeRecord


class ChangeRecordFilter(FilterSet):
    inst_id = NumberFilter(field_name="inst_id", lookup_expr="exact", label="实例ID")
    model_id = CharFilter(field_name="model_id", lookup_expr="exact", label="模型ID")
    type = CharFilter(field_name="type", lookup_expr="exact", label="变更类型")
    operator = CharFilter(field_name="operator", lookup_expr="icontains", label="操作者")
    created_at = DateTimeFromToRangeFilter(field_name="created_at", lookup_expr="range", label="创建时间区间")

    class Meta:
        model = ChangeRecord
        fields = ["inst_id", "model_id", "type", "operator", "created_at"]
