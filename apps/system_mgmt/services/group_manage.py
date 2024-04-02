from apps.core.exceptions.base_app_exception import BaseAppException
from apps.core.utils.keycloak_client import KeyCloakClient
from apps.system_mgmt.constants import APP_MODULE, GROUP, DEFAULT_GROUP_NAME
from apps.system_mgmt.models import OperationLog
from apps.system_mgmt.utils.keycloak import get_realm_roles


class GroupManage(object):
    def __init__(self):
        self.keycloak_client = KeyCloakClient()

    def group_list(self, query_params):
        """用户组列表"""
        groups = self.keycloak_client.realm_client.get_groups(query_params)
        # 过滤组织，只返回默认组织
        groups = [i for i in groups if i["name"] == DEFAULT_GROUP_NAME]
        return groups

    def group_retrieve(self, group_id):
        """查询某个组织的信息"""
        group = self.keycloak_client.realm_client.get_group(group_id)
        return group

    def group_create(self, data, operator):
        """创建用户组"""
        group_id = self.keycloak_client.realm_client.create_group(
            dict(name=data["group_name"]), data.get("parent_group_id") or None)
        OperationLog.objects.create(
            operator=operator,
            operate_type=OperationLog.ADD,
            operate_obj=data["group_name"],
            operate_summary="创建用户组织!",
            app_module=APP_MODULE,
            obj_type=GROUP,
        )
        return {"id": group_id}

    def group_update(self, data, group_id, operator):
        """更新用户组"""
        group = GroupManage().group_retrieve(group_id)
        self.keycloak_client.realm_client.update_group(group_id, dict(name=data["group_name"]))
        OperationLog.objects.create(
            operator=operator,
            operate_type=OperationLog.MODIFY,
            operate_obj=group["name"],
            operate_summary="修改用户组织名称为:[{}]".format(data["group_name"]),
            app_module=APP_MODULE,
            obj_type=GROUP,
        )
        return {"id": group_id}

    def group_delete(self, data, operator):
        """
            删除用户组
            1.校验用户组下是否存在用户
            2.删除操作
        """
        if not data:
            raise BaseAppException("参数验证失败!")

        groups = []
        for group_id in data:
            users = self.keycloak_client.realm_client.get_group_members(group_id)
            if users:
                msg = "、".join([i["username"] for i in users])
                raise BaseAppException(f"组织下已存在用户：{msg}！")

            group = GroupManage().group_retrieve(group_id)
            groups.append(group["name"])

            self.keycloak_client.realm_client.delete_group(group_id)

        objs = [
            OperationLog(
                operator=operator,
                operate_type=OperationLog.DELETE,
                operate_obj=group_name,
                operate_summary="删除用户组织!",
                app_module=APP_MODULE,
                obj_type=GROUP,
            ) for group_name in groups
        ]
        OperationLog.objects.bulk_create(objs, batch_size=100)

    def group_users(self, group_id):
        """获取用户组下用户"""
        users = self.keycloak_client.realm_client.get_group_members(group_id)
        return users

    def group_add_users(self, data, group_id, operator):
        """将一些用户添加到组"""
        if not data:
            raise BaseAppException("参数验证失败!")

        group = GroupManage().group_retrieve(group_id)
        users = []
        for user_id in data:
            self.keycloak_client.realm_client.group_user_add(user_id, group_id)
            user = self.keycloak_client.realm_client.get_user(user_id)
            users.append(user["username"])

        objs = [
            OperationLog(
                operator=operator,
                operate_type=OperationLog.INCREASE,
                operate_obj=group['name'],
                operate_summary=f"将用户[{user_name}]加到用户组织[{group['name']}]下",
                app_module=APP_MODULE,
                obj_type=GROUP,
            ) for user_name in users
        ]
        OperationLog.objects.bulk_create(objs, batch_size=100)

        return {"id": group_id}

    def group_remove_users(self, data, group_id, operator):
        """将一些用户从组中移除"""
        if not data:
            raise BaseAppException("参数验证失败!")

        group = GroupManage().group_retrieve(group_id)
        users = []
        for user_id in data:
            self.keycloak_client.realm_client.group_user_remove(user_id, group_id)
            user = self.keycloak_client.realm_client.get_user(user_id)
            users.append(user["username"])

        objs = [
            OperationLog(
                operator=operator,
                operate_type=OperationLog.REMOVE,
                operate_obj=group['name'],
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

    def group_add_roles(self, data, group_id, operator):
        """将一些角色添加到组"""
        if not data:
            raise BaseAppException("参数验证失败!")

        roles = get_realm_roles(self.keycloak_client.realm_client)
        role_list = [i for i in roles if i["id"] in data]

        self.keycloak_client.realm_client.assign_group_realm_roles(group_id, role_list)

        group = GroupManage().group_retrieve(group_id)
        objs = [
            OperationLog(
                operator=operator,
                operate_type=OperationLog.INCREASE,
                operate_obj=group['name'],
                operate_summary=f"将角色[{role_info['name']}]加到用户组织[{group['name']}]下",
                app_module=APP_MODULE,
                obj_type=GROUP,
            ) for role_info in role_list
        ]
        OperationLog.objects.bulk_create(objs, batch_size=100)

        return {"id": group_id}

    def group_remove_roles(self, data, group_id, operator):
        """将一些角色从组中移除"""
        if not data:
            raise BaseAppException("参数验证失败!")

        roles = get_realm_roles(self.keycloak_client.realm_client)
        role_list = [i for i in roles if i["id"] in data]

        self.keycloak_client.realm_client.delete_group_realm_roles(group_id, role_list)

        group = GroupManage().group_retrieve(group_id)
        objs = [
            OperationLog(
                operator=operator,
                operate_type=OperationLog.REMOVE,
                operate_obj=group['name'],
                operate_summary=f"将角色[{role_info['name']}]从用户组织[{group['name']}]移除",
                app_module=APP_MODULE,
                obj_type=GROUP,
            ) for role_info in role_list
        ]
        OperationLog.objects.bulk_create(objs, batch_size=100)

        return {"id": group_id}
