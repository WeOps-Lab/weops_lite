from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action

from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.web_utils import WebUtils
from apps.system_mgmt.services.user_manage import UserManage


class KeycloakGroupViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_id="group_list",
        operation_description="用户组列表",
        manual_parameters=[
            openapi.Parameter("search", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    @uma_permission("group_list")
    def list(self, request):
        data = UserManage().group_list(dict(search=request.query_params.get("search", "")))
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_retrieve",
        operation_description="获取组织或者子组的信息",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户组ID", type=openapi.TYPE_STRING),
        ],
    )
    @uma_permission("group_retrieve")
    def retrieve(self, request, pk: str):
        data = UserManage().group_retrieve(pk)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_create",
        operation_description="创建一个组，如有父组织请添加字段parent_group_id",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "group_name": openapi.Schema(type=openapi.TYPE_STRING, description="Role name"),
                "parent_group_id": openapi.Schema(type=openapi.TYPE_STRING, description="description"),
            },
            required=["group_name"]
        )
    )
    @uma_permission("group_create")
    def create(self, request):
        data = UserManage().group_create(request.data, request.userinfo.get("username"))
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_update",
        operation_description="修改组名",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户组ID", type=openapi.TYPE_STRING),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={"group_name": openapi.Schema(type=openapi.TYPE_STRING, description="group name")},
            required=["group_name"]
        ),
    )
    @uma_permission("group_update")
    def update(self, request, pk: str):
        data = UserManage().group_update(request.data, pk, request.userinfo.get("username"))
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_delete",
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="组ID")
        ),
        operation_description="删除组"
    )
    @action(detail=False, methods=["delete"])
    @uma_permission("group_delete")
    def delete_groups(self, request):
        UserManage().group_delete(request.data, request.userinfo.get("username"))
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="group_users",
        operation_description="获取该组下的所有用户",
    )
    @action(detail=True, methods=["get"], url_path="users")
    @uma_permission("group_users")
    def get_users_in_group(self, request, pk: str):
        data = UserManage().group_users(pk)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_add_users",
        operation_description="将一些用户添加到用户组织下",
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="用户ID")
        ),
    )
    @action(detail=True, methods=["patch"], url_path="assign_users")
    @uma_permission("group_add_users")
    def assign_group_users(self, request, pk: str):
        data = UserManage().group_add_users(request.data, pk, request.userinfo.get("username"))
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_remove_users",
        operation_description="将一系列用户从组移除",
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="用户ID")
        ),
    )
    @action(detail=True, methods=["delete"], url_path="unassign_users")
    @uma_permission("group_remove_users")
    def unassigned_group_users(self, request, pk: str):
        data = UserManage().group_remove_users(request.data, pk, request.userinfo.get("username"))
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_roles",
        operation_description="获取该组下的所有角色",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户组ID", type=openapi.TYPE_STRING)
        ],
    )
    @action(detail=True, methods=["get"], url_path="roles")
    @uma_permission("group_roles")
    def get_roles_in_group(self, request, pk: str):
        data = UserManage().group_roles(pk)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_add_roles",
        operation_description="将一系列角色添加到组",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户组ID", type=openapi.TYPE_STRING)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="角色ID")
        ),
    )
    @action(detail=True, methods=["patch"], url_path="assign_roles")
    @uma_permission("group_add_roles")
    def assign_group_roles(self, request, pk: str):
        data = UserManage().group_add_roles(request.data, pk, request.userinfo.get("username"))
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_remove_roles",
        operation_description="将一系列角色从组移除",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户组ID", type=openapi.TYPE_STRING)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="角色ID")
        ),
    )
    @action(detail=True, methods=["delete"], url_path="unassign_roles")
    @uma_permission("group_remove_roles")
    def unassigned_group_roles(self, request, pk: str):
        data = UserManage().group_remove_roles(request.data, pk, request.userinfo.get("username"))
        return WebUtils.response_success(data)