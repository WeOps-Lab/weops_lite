from apps.core.constants import AUTH_TOKEN_HEADER_NAME
from apps.core.utils.keycloak_client import KeyCloakClient
from apps.system_mgmt.constants import ADMIN
from apps.system_mgmt.utils.keycloak import get_client_id, SupplementApi


class LoginInfo(object):
    def __init__(self):
        self.keycloak_client = KeyCloakClient()

    def get_user_login_info(self, request):
        """获取用户登录后的信息"""
        token = request.META.get(AUTH_TOKEN_HEADER_NAME)

        # 获取用户基本信息
        user_info = self.keycloak_client.get_userinfo(token)

        # 查询用户角色
        user_roles = self.keycloak_client.get_roles(token)

        # 判断是否为超管
        is_super = True if ADMIN in user_roles else False

        permissions = set()

        # 若用户非超管，就获取用户的权限列表
        if not is_super:
            # 获取角色对应的policy_ids
            client_id = get_client_id(self.keycloak_client.realm_client)
            policies = self.keycloak_client.realm_client.get_client_authz_policies(client_id)
            policy_ids = [i["id"] for i in policies if i["name"] in user_roles]

            # 根据policy_ids获取所有策略下的权限

            for policy_id in policy_ids:
                permission_list = SupplementApi(
                    self.keycloak_client.realm_client.connection).get_permission_by_policy_id(client_id, policy_id)
                for permission_info in permission_list:
                    permissions.add(permission_info["name"])

        # TODO 过滤权限，只返回菜单权限
        menus_permissions = list(permissions)
        result = {"user_info": user_info, "is_super": is_super, "menus_permissions": menus_permissions}
        return result
