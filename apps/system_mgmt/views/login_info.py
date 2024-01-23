from drf_yasg.utils import swagger_auto_schema
from rest_framework import views
from rest_framework.response import Response

from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.keycloak_client import KeyCloakClient


class LoginInfoView(views.APIView):
    realm_client = KeyCloakClient().get_realm_client()

    @swagger_auto_schema(operation_description="用户登录之后，获取基本信息")
    @uma_permission('api_login_info')
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        is_super = KeyCloakClient().is_super_admin(token)
        user_info = self.realm_client.userinfo(token)
        permissions = self.realm_client.get_permissions(token)

        # TODO 过滤权限，只返回菜单权限
        menus_permissions = permissions

        return Response({"user_info": user_info, "is_super": is_super, "menus_permissions": menus_permissions})
