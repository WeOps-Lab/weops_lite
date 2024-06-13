from apps.cmdb_mgmt.constants import ORGANIZATION
from apps.cmdb_mgmt.models.Instance_permission import InstancePermission, QUERY, UserInstancePermission, MANAGE
from apps.cmdb_mgmt.utils.format_type import FORMAT_TYPE
from apps.cmdb_mgmt.utils.subgroup import SubGroup
from apps.core.exceptions.base_app_exception import BaseAppException
from apps.core.utils.keycloak_client import KeyCloakClient
from apps.system_mgmt.constants import ADMIN, DEFAULT_GROUP_NAME


class PermissionManage:
    def __init__(self, token, model_id, permission_type: str = None):
        self.token = token
        self.model_id = model_id
        self.permission_type = permission_type
        self.keycloak_client = KeyCloakClient()
        self.group_list = None

    def get_permission_params_by_user(self, username):
        """根据角色获取实例权限"""
        query_dict = dict(username=username)
        if self.model_id:
            query_dict.update(model_id=self.model_id)
        if self.permission_type:
            query_dict.update(permission_type=self.permission_type)

        objs = UserInstancePermission.objects.filter(**query_dict)
        return objs

    def get_group_list(self):
        """获取组织列表"""
        if not self.group_list:
            groups = self.keycloak_client.realm_client.get_groups({"search": ""})
            self.group_list = [i for i in groups if i["name"] == DEFAULT_GROUP_NAME]
        return self.group_list

    def supplementary_subgroups(self, params: list):
        """对组织补充子组, 并将类型改为str[]"""
        for param in params:
            if param["field"] != ORGANIZATION:
                continue
            if not param.get("include_subgroups"):
                continue
            if type(param["value"]) == str:
                param["value"] = [param["value"]]
                param["type"] = "str[]"

            groups = []
            for group_id in param["value"]:
                groups.extend(SubGroup(group_id, self.get_group_list()).get_group_id_and_subgroup_id())
            # 去重
            param["value"] = list(set(groups))

    def get_permission_params_by_roles(self, roles):
        """根据角色获取实例权限"""
        query_dict = dict(role_id__in=roles)
        if self.model_id:
            query_dict.update(model_id=self.model_id)
        if self.permission_type:
            query_dict.update(permission_type=self.permission_type)

        objs = InstancePermission.objects.filter(**query_dict)
        return objs

    def format_permission_params(self, param_objs):
        param_map = {}
        for obj in param_objs:
            if obj.model_id not in param_map:
                param_map[obj.model_id] = []

            for condition_group in obj.conditions:
                _connect, _param = " AND ", ""

                # 补充子组织
                self.supplementary_subgroups(condition_group)

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
            if not model_id:
                param_list.append(f"({' OR '.join(_param)})")
            else:
                param_list.append(f"(n.model_id = '{model_id}' AND ({' OR '.join(_param)}))")

        param_str = " OR ".join(param_list)

        return f"({param_str})" if param_str else param_str

    def get_permission_params(self):
        """获取条件，用于列表页查询"""

        # 查询用户角色
        roles = self.keycloak_client.get_roles(self.token)

        # 判断是否为超管, 超管返回空条件
        if ADMIN in roles:
            return ""

        # 获取用户权限
        userinfo = self.keycloak_client.get_userinfo(self.token)
        user_permissions = self.get_permission_params_by_user(userinfo["preferred_username"])

        # 获取角色权限
        role_permissions = self.get_permission_params_by_roles(roles)

        # 合并角色与用户授权
        permissions = list(user_permissions) + list(role_permissions)

        # 将用户创建的实例条件加上
        permissions.append(
            UserInstancePermission(
                username=userinfo["preferred_username"],
                model_id=self.model_id,
                permission_type=MANAGE,
                conditions=[[{"field": "_creator", "type": "str=", "value": userinfo["preferred_username"]}]]
            )
        )

        # 格式化权限条件
        permission_params = self.format_permission_params(permissions)

        # 普通用户权限参数为空，说明用户无实例权限
        if not permission_params:
            raise BaseAppException("无实例权限！")

        return permission_params


class RolePermissionManage(PermissionManage):

    def __init__(self, roles,  model_id,  permission_type: str = None, token: str = None):
        super().__init__(token, model_id, permission_type)
        self.roles = roles

    def get_permission_params(self):
        """获取条件，用于列表页查询"""

        # 判断是否为超管, 超管返回空条件
        if ADMIN in self.roles:
            return ""

        # 获取角色权限
        permissions = self.get_permission_params_by_roles(self.roles)

        # 格式化权限条件
        permission_params = self.format_permission_params(permissions)

        # 普通用户权限参数为空，说明用户无实例权限
        if not permission_params:
            raise BaseAppException("无实例权限！")

        return permission_params
