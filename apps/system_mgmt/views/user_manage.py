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
            openapi.Parameter("page", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("page_size", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("search", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    @uma_permission("group_list")
    def list(self, request):
        data = UserManage().group_list(request)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_retrieve",
        operation_description="获取一个组以及其子组",
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
        data = UserManage().group_create(request)
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
        data = UserManage().group_update(request, pk)
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
        UserManage().group_delete(request)
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="group_users",
        operation_description="获取该组下的所有用户",
        manual_parameters=[
            openapi.Parameter("page", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("page_size", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
        ],
    )
    @action(detail=True, methods=["get"], url_path="users")
    @uma_permission("group_users")
    def get_users_in_group(self, request, pk: str):
        data = UserManage().group_users(request, pk)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_add_users",
        operation_description="将一系列用户添加到组",
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="用户ID")
        ),
    )
    @action(detail=True, methods=["patch"], url_path="assign_users")
    @uma_permission("group_add_users")
    def assign_group_users(self, request, pk: str):
        data = UserManage().group_add_users(request, pk)
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
        data = UserManage().group_remove_users(request, pk)
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
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="角色ID")
        ),
    )
    @action(detail=True, methods=["patch"], url_path="assign_roles")
    @uma_permission("group_add_roles")
    def assign_group_roles(self, request, pk: str):
        data = UserManage().group_add_roles(request, pk)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="group_remove_roles",
        operation_description="将一系列角色从组移除",
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="角色ID")
        ),
    )
    @action(detail=True, methods=["delete"], url_path="unassign_roles")
    @uma_permission("group_remove_roles")
    def unassigned_group_roles(self, request, pk: str):
        data = UserManage().group_remove_roles(request, pk)
        return WebUtils.response_success(data)


class KeycloakUserViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_id="user_list",
        operation_description="查询用户列表",
        manual_parameters=[
            openapi.Parameter("page", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("page_size", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("search", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ],
    )
    @uma_permission("user_list")
    def list(self, request):
        data = UserManage().user_list(request)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="user_list_by_role",
        operation_description="获取该角色下的所有用户",
        manual_parameters=[
            openapi.Parameter("role_name", openapi.IN_PATH, description="角色英文名称", type=openapi.TYPE_STRING)
        ],
    )
    @action(detail=False, methods=["get"], url_path="roles/(?P<role_name>.+?)")
    @uma_permission("user_list_by_role")
    def get_users_in_role(self, request, role_name: str):
        data = UserManage().user_list_by_role(request, role_name)
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
            required=["username", "password"]
        ),
    )
    @uma_permission("user_create")
    def create(self, request):
        data = UserManage().user_create(request)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="user_create",
        operation_description="删除用户",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户id", type=openapi.TYPE_STRING)
        ],
    )
    @uma_permission("user_create")
    def destroy(self, request, pk: str):
        data = UserManage().user_delete(pk)
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
                "firstName": openapi.Schema(type=openapi.TYPE_STRING, description="User first name"),
                "lastName": openapi.Schema(type=openapi.TYPE_STRING, description="User last name"),
            },
        ),
    )
    @uma_permission("user_update")
    def update(self, request, pk: str):
        data = UserManage().user_update(request, pk)
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
            required=["password"]
        ),
    )
    @uma_permission("user_reset_password")
    def partial_update(self, request, pk: str):
        data = UserManage().user_reset_password(request, pk)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="user_add_groups",
        operation_description="将一系列组添加到用户",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户ID", type=openapi.TYPE_STRING)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="组ID")
        ),
    )
    @action(detail=True, methods=["patch"], url_path="assign_groups")
    @uma_permission("user_add_groups")
    def assign_user_groups(self, request, pk: str):
        UserManage().user_add_groups(request, pk)
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="user_remove_groups",
        operation_description="将一系列组从该用户移除",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="用户ID", type=openapi.TYPE_STRING)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="组ID")
        ),
    )
    @action(detail=True, methods=["delete"], url_path="unassign_groups")
    @uma_permission("user_remove_groups")
    def unassign_user_groups(self, request, pk: str):
        UserManage().user_remove_groups(request, pk)
        return WebUtils.response_success()


class KeycloakRoleViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_id="role_list",
        operation_description="获取所有角色",
    )
    @uma_permission("role_list")
    def list(self, request):
        data = UserManage().role_list()
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="role_permissions",
        operation_description="获取角色拥有的权限",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="角色英文名称", type=openapi.TYPE_STRING)
        ],
    )
    @uma_permission("role_permissions")
    @action(detail=True, methods=["get"], url_path="permissions")
    def role_permissions(self, request, pk: str):
        data = UserManage().role_permissions(pk)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="role_create",
        operation_description="创建角色",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="角色名称"),
                "description": openapi.Schema(type=openapi.TYPE_STRING, description="描述"),
            },
            required=["name"]
        ),
    )
    @uma_permission("role_create")
    def create(self, request):
        data = UserManage().role_create(request)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="role_delete",
        operation_description="删除角色",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="角色英文名称", type=openapi.TYPE_STRING),
        ],
    )
    @uma_permission("role_delete")
    def destroy(self, request, pk: str):
        data = UserManage().role_delete(pk)
        return WebUtils.response_success(data)

    @swagger_auto_schema(
        operation_id="role_update",
        operation_description="修改角色信息",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="角色英文名称", type=openapi.TYPE_STRING)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="角色英文名"),
                "description": openapi.Schema(type=openapi.TYPE_STRING, description="描述"),
            }
        )
    )
    @uma_permission("role_update")
    def update(self, request, pk: str):
        UserManage().role_update(request, pk)
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="role_set_permissions",
        operation_description="设置角色权限",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="角色英文名称", type=openapi.TYPE_STRING),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="权限名称")
        ),
    )
    @role_permissions.mapping.patch
    @uma_permission("role_set_permissions")
    def ch_permission(self, request, pk: str):
        UserManage().role_set_permissions(request, pk)
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="role_add_user",
        operation_description="将一个用户添加到角色",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="角色的ID", type=openapi.TYPE_STRING),
            openapi.Parameter("user_id", openapi.IN_PATH, description="用户的ID", type=openapi.TYPE_STRING),
        ],
    )
    @action(detail=True, methods=["put"], url_path="assign/(?P<user_id>[^/.]+)")
    @uma_permission("role_add_user")
    def assign_role(self, request, pk: str, user_id: str):
        UserManage().role_set_permissions(pk, user_id)
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="role_remove_user",
        operation_description="将一个用户从角色移除",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="角色的ID", type=openapi.TYPE_STRING),
            openapi.Parameter("user_id", openapi.IN_PATH, description="用户的ID", type=openapi.TYPE_STRING),
        ],
    )
    @action(detail=True, methods=["delete"], url_path="withdraw/(?P<user_id>[^/.]+)")
    @uma_permission("role_remove_user")
    def withdraw_role(self, request, pk: str, user_id: str):
        UserManage().role_remove_user(pk, user_id)
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="role_add_groups",
        operation_description="将该角色添加到一系列组中",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="角色的ID", type=openapi.TYPE_STRING),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="组ID")
        ),
    )
    @action(detail=True, methods=["patch"], url_path="assign_groups")
    @uma_permission("role_add_groups")
    def assign_groups(self, request, pk: str):
        UserManage().role_add_groups(request, pk)
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="role_remove_groups",
        operation_description="将该角色从一系列组中移除",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="角色ID", type=openapi.TYPE_STRING)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING, description="组ID")
        ),
    )
    @action(detail=True, methods=["delete"], url_path="unassign_groups")
    @uma_permission("role_remove_groups")
    def unassign_groups(self, request, pk: str):
        UserManage().role_remove_groups(request, pk)
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="role_groups",
        operation_description="获取该角色下的所有组",
        manual_parameters=[
            openapi.Parameter("role_name", openapi.IN_PATH, description="角色英文名称", type=openapi.TYPE_STRING)
        ],
    )
    @action(detail=False, methods=["get"], url_path="groups/(?P<role_name>.+?)")
    @uma_permission("role_groups")
    def get_groups_by_role(self, request, role_name: str):
        data = UserManage().role_remove_groups(request, role_name)
        return WebUtils.response_success(data)
