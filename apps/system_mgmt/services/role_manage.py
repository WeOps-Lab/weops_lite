from collections import defaultdict

from apps.core.exceptions.base_app_exception import BaseAppException
from apps.core.utils.keycloak_client import KeyCloakClient
from apps.system_mgmt.constants import APP_MODULE, ROLE, ADMIN, NORMAL, GRADE_ADMIN
from apps.system_mgmt.models import OperationLog
from apps.system_mgmt.models.graded_role import GradedRole
from apps.system_mgmt.utils.graded_role import get_role_all_child_role
from apps.system_mgmt.utils.keycloak import SupplementApi, get_realm_roles, get_realm_roles_of_user


class RoleManage(object):
    def __init__(self):
        self.keycloak_client = KeyCloakClient()

    def role_list(self, role_list=None):
        """角色列表"""
        result = get_realm_roles(self.keycloak_client.realm_client)
        role_objs = GradedRole.objects.all()
        role_dict = {i.role: i.superior_role for i in role_objs}
        for role_info in result:
            if role_info["name"] in role_dict:
                role_info.update(superior_role=role_dict[role_info["name"]])
        if role_list:
            result = [i for i in result if i["name"] in role_list]
        return result

    def get_subordinate_roles(self, role_name, hierarchy):
        # 递归函数来获取某个角色的所有下级角色
        sub_roles = []

        def _get_subordinate_roles(role_name):
            for sub_role in hierarchy.get(role_name, []):
                sub_roles.append(sub_role)
                _get_subordinate_roles(sub_role)

        _get_subordinate_roles(role_name)
        return sub_roles

    def get_user_child_role(self, user_id):

        # 查询所有角色及其上级角色
        roles = GradedRole.objects.all().values('role', 'superior_role')

        # 构建一个字典，键是上级角色，值是下级角色的列表
        role_hierarchy = defaultdict(list)
        for role in roles:
            role_hierarchy[role['superior_role']].append(role['role'])

        # 获取用户角色
        roles_to_query = get_realm_roles_of_user(self.keycloak_client.realm_client, user_id)
        all_subordinate_roles = set()

        for role_info in roles_to_query:
            role = role_info["name"]
            all_subordinate_roles.add(role)

            child_roles = self.get_subordinate_roles(role, role_hierarchy)
            for child_role in child_roles:
                all_subordinate_roles.add(child_role)

        return self.role_list(all_subordinate_roles)

    def role_permissions(self, role_name):
        """获取角色权限"""
        client_id = self.keycloak_client.get_client_id()
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

    def role_create(self, data, operator):
        """创建角色，先创建角色再创建角色对应的策略"""
        role_name, superior_role = data["name"], data.pop("superior_role", "")
        self.keycloak_client.realm_client.create_realm_role(data, True)
        role_info = self.keycloak_client.realm_client.get_realm_role(role_name=role_name)
        client_id = self.keycloak_client.get_client_id()
        policy_data = {
            "type": "role",
            "logic": "POSITIVE",
            "decisionStrategy": "AFFIRMATIVE",
            "name": role_name,
            "roles": [
                {
                    "id": role_info["id"]
                }
            ]
        }
        self.keycloak_client.realm_client.create_client_authz_role_based_policy(client_id, policy_data, True)

        if superior_role:
            GradedRole.objects.create(role=role_name, superior_role=superior_role)

        OperationLog.objects.create(
            operator=operator,
            operate_type=OperationLog.ADD,
            operate_obj=role_name,
            operate_summary=f"创建角色！",
            app_module=APP_MODULE,
            obj_type=ROLE,
        )

        return role_info

    def role_delete(self, role_name, operator):
        """
            删除角色
            1.角色关联校验（校验角色是否被用户或者组织关联）
            2.移除角色绑定的权限
            3.删除角色
        """

        # 禁止删除内置角色
        if role_name in {ADMIN, GRADE_ADMIN, NORMAL}:
            raise BaseAppException(f"内置角色禁止删除！")

        # 校验角色是否为其他角色的上级角色
        superior_objs = GradedRole.objects.filter(superior_role=role_name)
        if superior_objs.exists():
            msg = "、".join([i.role for i in superior_objs])
            raise BaseAppException(f"角色存在下级角色：{msg}")

        # 角色关联校验（校验角色是否被用户或者组织关联）
        groups = self.keycloak_client.realm_client.get_realm_role_groups(role_name)
        if groups:
            msg = "、".join([i["name"] for i in groups])
            raise BaseAppException(f"角色已被下列组织使用：{msg}！")

        users = self.keycloak_client.realm_client.get_realm_role_members(role_name)
        if users:
            msg = "、".join([i["username"] for i in users])
            raise BaseAppException(f"角色已被下列用户使用：{msg}！")

        # 移除角色权限
        client_id = self.keycloak_client.get_client_id()
        policies = self.keycloak_client.realm_client.get_client_authz_policies(client_id)
        policy_id = None
        for policy in policies:
            if policy["name"] == role_name:
                policy_id = policy["id"]
                break
        permissions = SupplementApi(
            self.keycloak_client.realm_client.connection).get_permission_by_policy_id(client_id, policy_id)
        supplement_api = SupplementApi(self.keycloak_client.realm_client.connection)
        for permission_info in permissions:
            del permission_info["config"]
            permission_policies = supplement_api.get_policies_by_permission_id(client_id, permission_info["id"])
            permission_policy_ids = [i["id"] for i in permission_policies]
            permission_policy_ids.remove(policy_id)
            permission_info.update(policies=permission_policy_ids, description="")
            supplement_api.update_permission(client_id, permission_info["id"], permission_info)

        # 删除角色
        role_info = self.keycloak_client.realm_client.get_realm_role(role_name=role_name)
        result = self.keycloak_client.realm_client.delete_realm_role(role_name)

        GradedRole.objects.filter(role=role_name).delete()

        OperationLog.objects.create(
            operator=operator,
            operate_type=OperationLog.DELETE,
            operate_obj=role_info["name"],
            operate_summary=f"删除角色！",
            app_module=APP_MODULE,
            obj_type=ROLE,
        )
        return result

    def role_update(self, description, role_name, operator):
        """修改角色信息"""
        role_info = self.keycloak_client.realm_client.get_realm_role(role_name=role_name)

        self.keycloak_client.realm_client.update_realm_role(role_name, dict(description=description, name=role_name))

        mes = f"{role_info['description']}->{description}"

        OperationLog.objects.create(
            operator=operator,
            operate_type=OperationLog.MODIFY,
            operate_obj=role_info["name"],
            operate_summary=f"修改角色描述！[{str(mes)}]",
            app_module=APP_MODULE,
            obj_type=ROLE,
        )

    def role_set_permissions(self, data, role_name, operator):
        """设置角色权限"""

        if role_name == ADMIN:
            raise BaseAppException(f"超管角色拥有全部权限，无需设置！")

        client_id = self.keycloak_client.get_client_id()
        all_resources = self.keycloak_client.realm_client.get_client_authz_resources(client_id)
        resource_mapping = {i["name"]: i["_id"] for i in all_resources}

        # 获取当前角色的子角色
        child_roles = get_role_all_child_role(role_name)
        child_roles_policies = set()

        # 获取角色映射的policy_id（角色与policy一对一映射）
        policies = self.keycloak_client.realm_client.get_client_authz_policies(client_id)
        policy_id = None
        for policy in policies:

            # 取出当前角色的子角色对应的policy_id
            if policy["name"] in child_roles:
                child_roles_policies.add(policy["id"])

            # 取角色的policy_id
            if policy["name"] == role_name:
                policy_id = policy["id"]

        permission_name_set = set(data)

        # 判断是否需要初始化权限，若需要就进行资源与权限的初始化
        all_permissions = self.keycloak_client.realm_client.get_client_authz_permissions(client_id)
        need_init_permissions = permission_name_set - {i["name"] for i in all_permissions}
        for permission_name in need_init_permissions:
            resource_id = resource_mapping.get(permission_name)
            if not resource_id:
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
                resource_id = resource_resp["_id"]
            permission = {
                "resources": [resource_id],
                "policies": [],
                "name": permission_name,
                "description": "",
                "decisionStrategy": "AFFIRMATIVE",
                "resourceType": ""
            }
            self.keycloak_client.realm_client.create_client_authz_resource_based_permission(client_id, permission, True)

        # 判断权限是否需要更新
        all_permissions = self.keycloak_client.realm_client.get_client_authz_permissions(client_id)
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

                # 当前角色的子角色解除权限
                for s_policy_id in child_roles_policies:
                    if s_policy_id not in permission_policy_ids:
                        continue
                    permission_policy_ids.remove(s_policy_id)

                # 当前角色解除权限绑定
                if policy_id not in permission_policy_ids:
                    continue
                permission_policy_ids.remove(policy_id)

            # 执行权限更新
            permission_info.update(policies=permission_policy_ids)
            supplement_api.update_permission(client_id, permission_info["id"], permission_info)

        OperationLog.objects.create(
            operator=operator,
            operate_type=OperationLog.MODIFY,
            operate_obj=role_name,
            operate_summary=f"修改角色权限！",
            app_module=APP_MODULE,
            obj_type=ROLE,
        )

    def role_add_user(self, role_id, user_id, operator):
        """为某个用户设置一个角色"""
        role = self.keycloak_client.realm_client.get_realm_role_by_id(role_id)
        self.keycloak_client.realm_client.assign_realm_roles(user_id, role)

        user_info = self.keycloak_client.realm_client.get_user(user_id)

        OperationLog.objects.create(
            operator=operator,
            operate_type=OperationLog.INCREASE,
            operate_obj=role["name"],
            operate_summary=f"对用户{user_info['username']}添加角色{role['name']}！",
            app_module=APP_MODULE,
            obj_type=ROLE,
        )

    def role_remove_user(self, role_id, user_id, operator):
        """移除角色下的某个用户"""
        role = self.keycloak_client.realm_client.get_realm_role_by_id(role_id)
        self.keycloak_client.realm_client.delete_realm_roles_of_user(user_id, role)

        user_info = self.keycloak_client.realm_client.get_user(user_id)

        OperationLog.objects.create(
            operator=operator,
            operate_type=OperationLog.REMOVE,
            operate_obj=role["name"],
            operate_summary=f"将用户{user_info['username']}的角色{role['name']}移除！",
            app_module=APP_MODULE,
            obj_type=ROLE,
        )

    def role_add_groups(self, data, role_id, operator):
        """为一些组添加某个角色"""
        role = self.keycloak_client.realm_client.get_realm_role_by_id(role_id)
        groups = []
        for group_id in data:
            self.keycloak_client.realm_client.assign_group_realm_roles(group_id, role)
            group = self.keycloak_client.realm_client.get_group(group_id)
            groups.append(group["name"])

        objs = [
            OperationLog(
                operator=operator,
                operate_type=OperationLog.INCREASE,
                operate_obj=role['name'],
                operate_summary=f"将角色[{role['name']}]加到用户组织[{group_name}]下",
                app_module=APP_MODULE,
                obj_type=ROLE,
            ) for group_name in groups
        ]
        OperationLog.objects.bulk_create(objs, batch_size=100)

    def role_remove_groups(self, data, role_id, operator):
        """将一些组移除某个角色"""
        role = self.keycloak_client.realm_client.get_realm_role_by_id(role_id)
        groups = []

        for group_id in data:
            self.keycloak_client.realm_client.delete_group_realm_roles(group_id, role)
            group = self.keycloak_client.realm_client.get_group(group_id)
            groups.append(group["name"])

        objs = [
            OperationLog(
                operator=operator,
                operate_type=OperationLog.REMOVE,
                operate_obj=role['name'],
                operate_summary=f"将角色[{role['name']}]从用户组织[{group_name}]移除",
                app_module=APP_MODULE,
                obj_type=ROLE,
            ) for group_name in groups
        ]
        OperationLog.objects.bulk_create(objs, batch_size=100)

    def role_groups(self, role_name):
        """获取角色关联的组"""
        result = self.keycloak_client.realm_client.get_realm_role_groups(role_name)
        return result
