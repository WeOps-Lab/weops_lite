import os
import traceback

from apps.core.constants import DEFAULT_GROUP_ID
from apps.core.utils.keycloak_client import KeyCloakClient


def init_admin(**kwargs):
    client = KeyCloakClient()

    role_name = "admin"
    username = "admin"
    password = os.getenv("WEOPS_ADMIN_PASSWORD", "weops-lite")
    email = ""
    lastname = "超管"

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
