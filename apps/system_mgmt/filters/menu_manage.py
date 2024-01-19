from django_filters import FilterSet, CharFilter

from apps.system_mgmt.models import MenuManage


class MenuManageFilter(FilterSet):
    """菜单过滤器"""

    search = CharFilter(field_name="menu_name", lookup_expr="icontains", label="菜单名称")

    class Meta:
        models = MenuManage
        fields = ["search"]
