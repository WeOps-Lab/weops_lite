from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action

from apps.cmdb_mgmt.services.classification import ClassificationManage
from apps.cmdb_mgmt.services.credential import CredentialManage
from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.web_utils import WebUtils

from rest_framework import viewsets


class CredentialViewSet(viewsets.ViewSet):

    @swagger_auto_schema(
        operation_id="cre_authorization",
        operation_description="授权",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "model_id": openapi.Schema(type=openapi.TYPE_STRING, description="模型ID"),
                "inst_id": openapi.Schema(type=openapi.TYPE_NUMBER, description="实例ID"),
                "roles": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING, description="角色名"), description="角色权限"),
                "users": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING, description="用户名"), description="用户权限"),
            },
            required=["model_id", "inst_id", "roles", "users"],
        ),
    )
    @action(methods=["post"], detail=False, url_path=r"authorization")
    @uma_permission("cre_authorization")
    def authorization(self, request):
        CredentialManage.user_authorisation(request.data["model_id"], request.data["inst_id"], request.data["users"])
        CredentialManage.role_authorisation(request.data["model_id"], request.data["inst_id"], request.data["roles"])
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="cre_authorization_list",
        operation_description="实例授权列表",
        manual_parameters=[
            openapi.Parameter("model_id", openapi.IN_PATH, description="模型ID", type=openapi.TYPE_STRING),
            openapi.Parameter("inst_id", openapi.IN_PATH, description="实例ID", type=openapi.TYPE_NUMBER),
        ],
        required=["model_id", "inst_id"],
    )
    @uma_permission("cre_authorization_list")
    @action(detail=False, methods=["get"], url_path=r"authorization_list/(?P<model_id>.+?)/(?P<inst_id>.+?)")
    def authorization_list(self, request, model_id: str, inst_id: int):
        roles = CredentialManage.get_roles(model_id, inst_id)
        users = CredentialManage.get_users(model_id, inst_id)
        return WebUtils.response_success(dict(users=users, roles=roles))

