from apps.core.constants import AUTH_TOKEN_HEADER_NAME
from apps.core.utils.keycloak_client import KeyCloakClient


class LoginInfo(object):
    def __init__(self):
        self.keycloak_client = KeyCloakClient()

    def get_user_login_info(self, request):
        """获取用户登录后的信息"""
        token = request.META.get(AUTH_TOKEN_HEADER_NAME)
        # 获取用户基本信息
        user_info = self.keycloak_client.get_userinfo(token)
        # 判断用户是否为超管
        is_super = self.keycloak_client.is_super_admin(token)
        # 获取用户权限
        permissions = [] if is_super else KeyCloakClient().get_permissions(token)

        # TODO 过滤权限，只返回菜单权限
        menus_permissions = permissions

        result = {"user_info": user_info, "is_super": is_super, "menus_permissions": menus_permissions}

        return result
