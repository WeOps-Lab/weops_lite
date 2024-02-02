import logging
import traceback

from django.core.management import BaseCommand
from dotenv import load_dotenv

from apps.core.constants import DEFAULT_GROUP_ID
from apps.core.utils.keycloak_client import KeyCloakClient
from weops_lite.components.keycloak import KEYCLOAK_URL


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

    def handle(self, *args, **options):
        load_dotenv()
        logger = logging.getLogger(__name__)

        # 域配置初始化
        logger.info(f'初始化KeyCloak Realm,KeyCloak URL:[{KEYCLOAK_URL}]')

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
