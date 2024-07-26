import logging
import traceback

from django.core.management import BaseCommand
from dotenv import load_dotenv

from apps.core.constants import DEFAULT_GROUP_ID
from apps.core.utils.keycloak_client import KeyCloakClient
from weops_lite.components.keycloak import KEYCLOAK_URL_API


class Command(BaseCommand):
    help = 'KeyCloak Realm 数据初始化'

    def init_realm(self):
        """初始化域配置"""
        client = KeyCloakClient()
        realm_config_file_path = 'support-files/keycloak/realm-export-v1.json'
        result = client.import_realm_from_file(realm_config_file_path)
        return result

    def init_admin(self):
        client = KeyCloakClient()
        username, password, lastname, email, role_name = "admin", "weops-lite", "超管", "", "admin"
        try:
            user_info = {
                'username': username,
                'credentials': [{"value": password, "type": 'password', 'temporary': False}],
                'email': email,
                'lastName': lastname,
                'enabled': True
            }
            # 创建admin用户
            user_id = client.realm_client.create_user(user_info, True)

            # 为admin用户设置admin角色
            role = client.realm_client.get_realm_role(role_name)
            client.realm_client.assign_realm_roles(user_id, role)

            # 将admin用户添加到总公司组织
            client.realm_client.group_user_add(user_id, DEFAULT_GROUP_ID)

            return True
        except Exception as e:
            traceback.print_exception(e)
            return False

    def init_grade_admin(self):

        try:
            from apps.system_mgmt.services.role_manage import RoleManage
            grade_admin_default_permissions = ['SysRole_view', 'SysRole_create', 'SysRole_edit', 'SysRole_delete', 'SysRole_users_manage', 'SysRole_permissions', 'role_list', 'role_create', 'role_update', 'role_delete', 'user_list_by_role', 'role_groups', 'user_list', 'group_list', 'role_remove_user', 'role_add_user', 'role_add_groups', 'role_remove_groups', 'role_permissions', 'role_set_permissions', 'r_permission_list', 'r_permission_create', 'r_permission_del', 'r_permission_update']
            RoleManage().role_set_permissions(grade_admin_default_permissions, "grade_admin", "system")
            return True
        except Exception as e:
            traceback.print_exception(e)
            return False

    def init_default_set_superior_role(self):
        try:
            from apps.system_mgmt.models.graded_role import GradedRole
            from apps.system_mgmt.utils.keycloak import get_realm_roles
            from apps.system_mgmt.constants import ADMIN
            result = get_realm_roles(KeyCloakClient().realm_client)
            graded_roles = [
                GradedRole(
                    role=role_info["name"],
                    superior_role=ADMIN,
                )
                for role_info in result
            ]
            GradedRole.objects.bulk_create(graded_roles, batch_size=100)
            return True
        except Exception as e:
            traceback.print_exception(e)
            return False

    def handle(self, *args, **options):
        load_dotenv()
        logger = logging.getLogger(__name__)

        # 域配置初始化
        logger.info(f'初始化KeyCloak Realm,KeyCloak URL:[{KEYCLOAK_URL_API}]')

        result = self.init_realm()

        if result is True:
            logger.info(f'初始化KeyCloak Realm 完成')
        else:
            logger.error(f'初始化KeyCloak Realm 失败')

        # 域超管用户初始化
        logger.info(f'初始化域admin用户！')

        result = self.init_admin()

        if result is True:
            logger.info(f'初始化域admin用户 完成')
        else:
            logger.error(f'初始化域admin用户 失败')

        # 分级管理员默认权限初始化
        logger.info(f'分级管理员默认权限初始化！')

        result = self.init_grade_admin()

        if result is True:
            logger.info(f'分级管理员默认权限初始化 完成')
        else:
            logger.error(f'分级管理员默认权限初始化 失败')

        # 初始化角色的上级角色
        logger.info(f'初始化角色的上级角色！')

        result = self.init_default_set_superior_role()

        if result is True:
            logger.info(f'初始化角色的上级角色 完成')
        else:
            logger.error(f'初始化角色的上级角色 失败')
