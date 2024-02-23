from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.web_utils import WebUtils
from apps.system_mgmt.responses.user_manage import user_list_responses, user_info_responses, \
    user_list_by_role_responses, user_create_responses, user_delete_responses, user_update_responses, \
    user_reset_password_responses, user_add_groups_responses, user_remove_groups_responses
from apps.system_mgmt.services.user_manage import UserManage
from apps.system_mgmt.utils.keycloak import get_first_and_max


class KeycloakUserViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_id="user_list",
        operation_description="查询用户列表",
        manual_parameters=[
            openapi.Parameter("page", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("page_size", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("search", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ],
        responses=user_list_responses
    )
    @uma_permission("user_list")
    def list(self, request):
        _first, _max = get_first_and_max(request.query_params)
        data = UserManage().user_list(dict(first=_first, max=_max, search=request.query_params.get("search", "")))
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="user_info",
        operation_description="获取用户信息",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户ID", type=openapi.TYPE_STRING),
        ],
        responses=user_info_responses,
    )
    def retrieve(self, request, pk: str):
        data = UserManage().get_user_info(pk)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="user_list_by_role",
        operation_description="获取该角色下的所有用户",
        manual_parameters=[
            openapi.Parameter("role_name", openapi.IN_PATH, description="角色英文名称", type=openapi.TYPE_STRING)
        ],
        responses=user_list_by_role_responses,
    )
    @action(detail=False, methods=["get"], url_path="roles/(?P<role_name>.+?)")
    @uma_permission("user_list_by_role")
    def get_users_in_role(self, request, role_name: str):
        data = UserManage().user_list_by_role(role_name)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="user_create",
        operation_description="创建用户",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING, description="User username"),
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="User email"),
                "lastName": openapi.Schema(type=openapi.TYPE_STRING, description="User last name"),
                "password": openapi.Schema(type=openapi.TYPE_STRING, description="User password"),
            },
            required=["username", "password"],
        ),
        responses=user_create_responses,
    )
    @uma_permission("user_create")
    def create(self, request):
        data = UserManage().user_create(request.data, request.userinfo.get("username"))
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="user_delete",
        operation_description="删除用户",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户id", type=openapi.TYPE_STRING)
        ],
        responses=user_delete_responses,
    )
    @uma_permission("user_delete")
    def destroy(self, request, pk: str):
        data = UserManage().user_delete(pk, request.userinfo.get("username"))
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="user_update",
        operation_description="修改用户信息",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="User ID", type=openapi.TYPE_STRING)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="User email"),
                "lastName": openapi.Schema(type=openapi.TYPE_STRING, description="User last name"),
            },
        ),
        responses=user_update_responses,
    )
    @uma_permission("user_update")
    def update(self, request, pk: str):
        data = UserManage().user_update(request.data, pk, request.userinfo.get("username"))
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="user_reset_password",
        operation_description="重置用户密码",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="User ID", type=openapi.TYPE_STRING)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "password": openapi.Schema(type=openapi.TYPE_STRING, description="User password"),
            },
            required=["password"],
        ),
        responses=user_reset_password_responses,
    )
    @uma_permission("user_reset_password")
    def partial_update(self, request, pk: str):
        data = UserManage().user_reset_password(request.data, pk, request.userinfo.get("username"))
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="user_add_groups",
        operation_description="将一系列组添加到用户",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户ID", type=openapi.TYPE_STRING)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="组ID"),
        ),
        responses=user_add_groups_responses,
    )
    @action(detail=True, methods=["patch"], url_path="assign_groups")
    @uma_permission("user_add_groups")
    def assign_user_groups(self, request, pk: str):
        UserManage().user_add_groups(request.data, pk, request.userinfo.get("username"))
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="user_remove_groups",
        operation_description="将一系列组从该用户移除",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户ID", type=openapi.TYPE_STRING)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="组ID"),
        ),
        responses=user_remove_groups_responses,
    )
    @action(detail=True, methods=["delete"], url_path="unassign_groups")
    @uma_permission("user_remove_groups")
    def unassign_user_groups(self, request, pk: str):
        UserManage().user_remove_groups(request.data, pk, request.userinfo.get("username"))
        return WebUtils.response_success()
