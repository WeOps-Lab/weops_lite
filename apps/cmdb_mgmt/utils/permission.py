from apps.cmdb_mgmt.models.Instance_permission import InstancePermission, QUERY
from apps.cmdb_mgmt.utils.format_type import FORMAT_TYPE
from apps.core.exceptions.base_app_exception import BaseAppException
from apps.core.utils.keycloak_client import KeyCloakClient
from apps.system_mgmt.constants import ADMIN


class PermissionManage:
    def __init__(self, token, model_id, permission_type: str = None):
        self.token = token
        self.model_id = model_id
        self.permission_type = permission_type
        self.keycloak_client = KeyCloakClient()

    def get_permission_params_by_roles(self, roles):
        """根据角色获取实例权限"""
        query_dict = dict(role_id__in=roles)
        if self.token:
            query_dict.update(model_id=self.model_id)
        if self.permission_type:
            query_dict.update(permission_type=self.permission_type)

        objs = InstancePermission.objects.filter(**query_dict)

        param_map = {}
        for obj in objs:
            if obj.model_id not in param_map:
                param_map[obj.model_id] = []

            for condition_group in obj.conditions:
                _connect, _param = " AND ", ""
                for condition in condition_group:
                    method = FORMAT_TYPE.get(condition["type"])
                    if not method:
                        continue
                    _param += method(condition)
                    _param += _connect

                if not _param:
                    continue
                param_map[obj.model_id].append(f"({_param[:-5]})")

        param_list = []

        for model_id, _param in param_map.items():
            mode_param = {"field": "model_id", "type": "str=", "value": model_id}
            param_list.append(f"({mode_param} AND ({' OR '.join(_param)}))")

        param_str = " OR ".join(param_list)

        return f"({param_str})" if param_str else param_str

    def get_permission_params(self):
        """获取条件，用于列表页查询"""

        # 查询用户角色
        roles = self.keycloak_client.get_roles(self.token)

        # 判断是否为超管, 超管返回空条件
        if ADMIN in roles:
            return ""

        permission_params = self.get_permission_params_by_roles(roles)

        # 普通用户权限参数为空，说明用户无实例权限
        if not permission_params:
            raise BaseAppException("无实例权限！")

        return permission_params
