from drf_yasg.utils import swagger_auto_schema
from rest_framework import views
from rest_framework.response import Response

from apps.core.constants import AUTH_TOKEN_HEADER_NAME
from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.keycloak_client import KeyCloakClient


class LoginInfoView(views.APIView):

    @swagger_auto_schema(operation_description="用户登录之后，获取基本信息")
    @uma_permission('api_login_info')
    def get(self, request):
        token = request.META.get(AUTH_TOKEN_HEADER_NAME)
        # 获取用户基本信息
        user_info = KeyCloakClient().get_userinfo(token)
        # 判断用户是否为超管
        is_super = KeyCloakClient().is_super_admin(token)
        # 获取用户权限
        permissions = [] if is_super else KeyCloakClient().get_permissions(token)

        # TODO 过滤权限，只返回菜单权限
        menus_permissions = permissions

        return Response({"user_info": user_info, "is_super": is_super, "menus_permissions": menus_permissions})
