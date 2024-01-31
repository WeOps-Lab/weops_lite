from apps.core.exceptions.param_validation_exception import ParamValidationException
from apps.core.utils.keycloak_client import KeyCloakClient
from apps.system_mgmt.constants import NORMAL, APP_MODULE, GROUP
from apps.system_mgmt.models import OperationLog
from apps.system_mgmt.utils.keycloak import get_first_and_max, get_client_id, SupplementApi, get_realm_roles, \
    get_realm_roles_of_user


class UserManage(object):
    def __init__(self):
        self.keycloak_client = KeyCloakClient()

    def group_list(self, request):
        """用户组列表"""
        _first, _max = get_first_and_max(request.query_params)
        groups = self.keycloak_client.realm_client.get_groups(
            dict(first=_first, max=_max, search=request.query_params.get("search", "")))
        return groups

    def group_retrieve(self, group_id):
        """查询某个组织的信息"""
        group = self.keycloak_client.realm_client.get_group(group_id)
        return group

    def group_create(self, request):
        """创建用户组"""
        group_id = self.keycloak_client.realm_client.create_group(
            dict(name=request.data["group_name"]), request.data.get("parent_group_id", None))
        OperationLog.objects.create(
            operator=request.userinfo.get("username"),
            operate_type=OperationLog.ADD,
            operate_obj=request.data["group_name"],
            operate_summary="创建用户组织!",
            app_module=APP_MODULE,
            obj_type=GROUP,
        )
        return {"id": group_id}

    def group_update(self, request, group_id):
        """更新用户组"""
        group = UserManage().group_retrieve(group_id)
        self.keycloak_client.realm_client.update_group(group_id, dict(name=request.data["group_name"]))
        OperationLog.objects.create(
            operator=request.userinfo.get("username"),
            operate_type=OperationLog.MODIFY,
            operate_obj=group["name"],
            operate_summary="修改用户组织名称为:[{}]".format(request.data["group_name"]),
            app_module=APP_MODULE,
            obj_type=GROUP,
        )
        return {"id": group_id}

    def group_delete(self, request):
        """删除用户组"""
        if not request.data:
            raise ParamValidationException

        groups = []
        for group_id in request.data:
            group = UserManage().group_retrieve(group_id)
            groups.append(group["name"])

            self.keycloak_client.realm_client.delete_group(group_id)

        objs = [
            OperationLog(
                operator=request.userinfo.get("username"),
                operate_type=OperationLog.DELETE,
                operate_obj=group_name,
                operate_summary="删除用户组织!",
                app_module=APP_MODULE,
                obj_type=GROUP,
            ) for group_name in groups
        ]
        OperationLog.objects.bulk_create(objs, batch_size=100)

    def group_users(self, request, group_id):
        """获取用户组下用户"""
        _first, _max = get_first_and_max(request.query_params)
        users = self.keycloak_client.realm_client.get_group_members(group_id, dict(first=_first, max=_max))
        return users

    def group_add_users(self, request, group_id):
        """将一些用户添加到组"""
        if not request.data:
            raise ParamValidationException

        group = UserManage().group_retrieve(group_id)
        users = []
        for user_id in request.data:
            self.keycloak_client.realm_client.group_user_add(user_id, group_id)
            user = self.keycloak_client.realm_client.get_user(user_id)
            users.append(user["name"])

        objs = [
            OperationLog(
                operator=request.userinfo.get("username"),
                operate_type=OperationLog.INCREASE,
                operate_obj=user_name,
                operate_summary=f"将用户[{user_name}]加到用户组织[{group['name']}]下",
                app_module=APP_MODULE,
                obj_type=GROUP,
            ) for user_name in users
        ]
        OperationLog.objects.bulk_create(objs, batch_size=100)

        return {"id": group_id}

    def group_remove_users(self, request, group_id):
        """将一些用户从组中移除"""
        if not request.data:
            raise ParamValidationException

        group = UserManage().group_retrieve(group_id)
        users = []
        for user_id in request.data:
            self.keycloak_client.realm_client.group_user_remove(user_id, group_id)
            user = self.keycloak_client.realm_client.get_user(user_id)
            users.append(user["name"])

        objs = [
            OperationLog(
                operator=request.userinfo.get("username"),
                operate_type=OperationLog.REMOVE,
                operate_obj=user_name,
                operate_summary=f"将用户[{user_name}]从用户组织[{group['name']}]移除",
                app_module=APP_MODULE,
                obj_type=GROUP,
            ) for user_name in users
        ]
        OperationLog.objects.bulk_create(objs, batch_size=100)

        return {"id": group_id}

    def group_roles(self, group_id):
        """获取组下面的角色"""
        roles = self.keycloak_client.realm_client.get_group_realm_roles(group_id)
        return roles

    def group_add_roles(self, request, group_id):
        """将一些角色添加到组"""
        if not request.data:
            raise ParamValidationException

        roles = get_realm_roles(self.keycloak_client.realm_client)
        role_list = [i for i in roles if i["id"] in request.data]

        self.keycloak_client.realm_client.assign_group_realm_roles(group_id, role_list)
        return {"id": group_id}

    def group_remove_roles(self, request, group_id):
        """将一些角色从组中移除"""
        if not request.data:
            raise ParamValidationException

        roles = get_realm_roles(self.keycloak_client.realm_client)
        role_list = [i for i in roles if i["id"] in request.data]

        self.keycloak_client.realm_client.delete_group_realm_roles(group_id, role_list)
        return {"id": group_id}

    def user_list(self, request):
        """用户列表"""
        _first, _max = get_first_and_max(request.query_params)
        users = self.keycloak_client.realm_client.get_users(
            dict(first=_first, max=_max, search=request.query_params.get("search")))
        for user_info in users:

            # 用户补充角色信息
            try:
                roles = get_realm_roles_of_user(self.keycloak_client.realm_client, user_info["id"])
            except:
                roles = []

            # 用户补充用户组信息
            try:
                groups = self.keycloak_client.realm_client.get_user_groups(user_info["id"])
            except:
                groups = []

            user_info.update(roles=roles, groups=groups)
        return {"count": len(users), "users": users}

    def user_list_by_role(self, request, role_name):
        """获取角色下用户"""
        _first, _max = get_first_and_max(request.query_params)
        result = self.keycloak_client.realm_client.get_realm_role_members(role_name)
        return result

    def user_create(self, request):
        """创建用户"""
        user_info = dict(
            username=request.data["username"],
            email=request.data.get("email"),
            lastName=request.data.get("lastName"),
            enabled=True,
            credentials=[{"value": request.data["password"], "type": "password"}],
        )
        normal_role = self.keycloak_client.realm_client.get_realm_role(NORMAL)
        user_id = self.keycloak_client.realm_client.create_user(user_info)
        self.keycloak_client.realm_client.assign_realm_roles(user_id, normal_role)
        return {"id": user_id}

    def user_delete(self, user_id):
        """删除用户"""
        self.keycloak_client.realm_client.delete_user(user_id)
        return {"id": user_id}

    def user_update(self, request, user_id):
        """更新用户"""
        self.keycloak_client.realm_client.update_user(user_id, request.data)
        return {"id": user_id}

    def user_reset_password(self, request, user_id):
        """重置用户密码"""
        self.keycloak_client.realm_client.set_user_password(user_id, request.data["password"], False)
        return {"id": user_id}

    def user_add_groups(self, request, user_id):
        """为用户添加一些组"""
        for group_id in request.data:
            self.keycloak_client.realm_client.group_user_add(user_id, group_id)

    def user_remove_groups(self, request, user_id):
        """将用户从一些组中移除"""
        for group_id in request.data:
            self.keycloak_client.realm_client.group_user_remove(user_id, group_id)

    def role_list(self):
        """角色列表"""
        result = get_realm_roles(self.keycloak_client.realm_client)
        return result

    def role_permissions(self, role_name):
        """获取角色权限"""
        client_id = get_client_id(self.keycloak_client.realm_client)
        policies = self.keycloak_client.realm_client.get_client_authz_policies(client_id)
        policy_id = None
        for policy in policies:
            if policy["name"] == role_name:
                policy_id = policy["id"]
                break
        if not policy_id:
            return []
        permissions = SupplementApi(
            self.keycloak_client.realm_client.connection).get_permission_by_policy_id(client_id, policy_id)
        return [i["name"] for i in permissions]

    def role_create(self, request):
        """创建角色，先创建角色再创建角色对应的策略"""
        role_name = self.keycloak_client.realm_client.create_realm_role(request.data, True)
        role_info = self.keycloak_client.realm_client.get_realm_role(role_name=role_name)
        client_id = get_client_id(self.keycloak_client.realm_client)
        policy_data = {
            "type": "role",
            "logic": "POSITIVE",
            "decisionStrategy": "UNANIMOUS",
            "name": role_name,
            "roles": [
                {
                    "id": role_info["id"]
                }
            ]
        }
        self.keycloak_client.realm_client.create_client_authz_role_based_policy(client_id, policy_data, True)
        return role_info

    def role_delete(self, role_name):
        """删除角色"""
        result = self.keycloak_client.realm_client.delete_realm_role(role_name)
        return result

    def role_update(self, request, role_name):
        """修改角色信息"""
        self.keycloak_client.realm_client.update_realm_role(role_name, request.data)

    def role_set_permissions(self, request, role_name):
        """设置角色权限"""
        client_id = get_client_id(self.keycloak_client.realm_client)
        all_permissions = self.keycloak_client.realm_client.get_client_authz_permissions(client_id)
        # 获取角色映射的policy_id（角色与policy一对一映射）
        policies = self.keycloak_client.realm_client.get_client_authz_policies(client_id)
        policy_id = ""
        for policy in policies:
            if policy["name"] == role_name:
                policy_id = policy["id"]
                break

        permission_name_set = set(request.data)

        # 判断是否需要初始化权限，若需要就进行资源与权限的初始化
        need_init_permissions = permission_name_set - {i["name"] for i in all_permissions}
        for permission_name in need_init_permissions:
            resource = {
                "name": permission_name,
                "displayName": "",
                "type": "",
                "icon_uri": "",
                "scopes": [],
                "ownerManagedAccess": False,
                "attributes": {}
            }
            resource_resp = self.keycloak_client.realm_client.create_client_authz_resource(client_id, resource, True)
            permission = {
                "resources": [resource_resp["_id"]],
                "policies": [],
                "name": permission_name,
                "description": "",
                "decisionStrategy": "UNANIMOUS",
                "resourceType": ""
            }
            self.keycloak_client.realm_client.create_client_authz_resource_based_permission(client_id, permission, True)

        # 判断权限是否需要更新
        supplement_api = SupplementApi(self.keycloak_client.realm_client.connection)
        for permission_info in all_permissions:

            permission_policies = supplement_api.get_policies_by_permission_id(client_id, permission_info["id"])
            permission_policy_ids = [i["id"] for i in permission_policies]

            # 需要绑定权限与角色的
            if permission_info["name"] in permission_name_set:
                if policy_id in permission_policy_ids:
                    continue
                permission_policy_ids.append(policy_id)

            # 需求解绑权限与角色的
            else:
                if policy_id not in permission_policy_ids:
                    continue
                permission_policy_ids.remove(policy_id)

            # 执行权限更新
            permission_info.update(policies=permission_policy_ids)
            supplement_api.update_permission(client_id, permission_info["id"], permission_info)

    def role_add_user(self, role_id, user_id):
        """为某个用户设置一个角色"""
        role = self.keycloak_client.realm_client.get_realm_role_by_id(role_id)
        self.keycloak_client.realm_client.assign_realm_roles(user_id, role)

    def role_remove_user(self, role_id, user_id):
        """移除角色下的某个用户"""
        role = self.keycloak_client.realm_client.get_realm_role_by_id(role_id)
        self.keycloak_client.realm_client.delete_realm_roles_of_user(user_id, role)

    def role_add_groups(self, request, role_id):
        """为一些组添加某个角色"""
        role = self.keycloak_client.realm_client.get_realm_role_by_id(role_id)
        for group_id in request.data:
            self.keycloak_client.realm_client.assign_group_realm_roles(group_id, role)

    def role_remove_groups(self, request, role_id):
        """将一些组移除某个角色"""
        role = self.keycloak_client.realm_client.get_realm_role_by_id(role_id)
        for group_id in request.data:
            self.keycloak_client.realm_client.delete_group_realm_roles(group_id, role)

    def role_groups(self, request, role_name):
        """获取角色关联的组"""
        _first, _max = get_first_and_max(request.query_params)
        result = self.keycloak_client.realm_client.get_realm_role_groups(role_name)
        return result
