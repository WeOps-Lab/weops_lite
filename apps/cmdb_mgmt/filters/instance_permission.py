from django_filters import FilterSet, CharFilter

from apps.cmdb_mgmt.models.Instance_permission import InstancePermission, UserInstancePermission


class RoleInstancePermissionFilter(FilterSet):
    role_id = CharFilter(field_name="role_id", lookup_expr="exact", label="角色ID")
    model_id = CharFilter(field_name="model_id", lookup_expr="exact", label="模型ID")
    permission_type = CharFilter(field_name="type", lookup_expr="exact", label="变更类型")

    class Meta:
        model = InstancePermission
        fields = ["role_id", "model_id", "permission_type"]


class UserInstancePermissionFilter(FilterSet):
    username = CharFilter(field_name="username", lookup_expr="exact", label="用户名")
    model_id = CharFilter(field_name="model_id", lookup_expr="exact", label="模型ID")
    permission_type = CharFilter(field_name="type", lookup_expr="exact", label="变更类型")

    class Meta:
        model = UserInstancePermission
        fields = ["username", "model_id", "permission_type"]
