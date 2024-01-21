import ast

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.core.decorators.uma_permission import uma_permission
from apps.core.exceptions.param_validation_exception import ParamValidationException
from apps.core.utils.keycloak_client import KeyCloakClient
from apps.system_mgmt.constants import NORMAL
from apps.system_mgmt.utils.keycloak import get_first_and_max, get_client_id, SupplementApi


class KeycloakGroupViewSet(viewsets.ViewSet):
    realm_client = KeyCloakClient().get_realm_client()

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("page", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("page_size", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("search", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ],
        operation_description="查询组"
    )
    @uma_permission("SysGroup_view")
    def list(self, request):
        _first, _max = get_first_and_max(request.query_params)
        groups = self.realm_client.get_groups(
            dict(first=_first, max=_max, search=request.query_params.get("search", "")))
        return Response(groups)

    @swagger_auto_schema(operation_description="获取一个组以及其子组")
    @uma_permission("SysGroup_view")
    def retrieve(self, request, pk: str):
        group = self.realm_client.get_group(pk)
        return Response(group)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "group_name": openapi.Schema(type=openapi.TYPE_STRING, description="Role name"),
                "parent_group_id": openapi.Schema(type=openapi.TYPE_STRING, description="description"),
            },
            required=["group_name"]
        ),
        operation_description="创建一个组，如有父组织请添加字段parent_group_id"
    )
    @uma_permission("SysGroup_create")
    def create(self, request):
        group_id = self.realm_client.create_group(
            dict(name=request.data["group_name"]), request.data.get("parent_group_id", None))
        return Response({"id": group_id})

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={"group_name": openapi.Schema(type=openapi.TYPE_STRING, description="group name")},
            required=["group_name"]
        ),
        operation_description="修改组名"
    )
    @uma_permission("SysGroup_edit")
    def update(self, request, pk: str):
        self.realm_client.update_group(pk, dict(name=request.data["group_name"]))
        return Response({"id": pk})

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING)
        ),
        operation_description="删除组"
    )
    @action(detail=False, methods=["delete"])
    @uma_permission("SysGroup_delete")
    def delete_groups(self, request):
        if not request.data:
            raise ParamValidationException
        for group_id in request.data:
            self.realm_client.delete_group(group_id)
        return Response()

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("page", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("page_size", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
        ],
        operation_description="获取该组下的所有用户"
    )
    @action(detail=True, methods=["get"], url_path="users")
    @uma_permission("SysGroup_user")
    def get_users_in_group(self, request, pk: str):
        _first, _max = get_first_and_max(request.query_params)
        users = self.realm_client.get_group_members(pk, dict(first=_first, max=_max))
        return Response(users)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING)
        ),
        operation_description="将一系列用户添加到组"
    )
    @action(detail=True, methods=["patch"], url_path="assign_users")
    @uma_permission("SysGroup_user")
    def assign_group_users(self, request, pk: str):
        if not request.data:
            raise ParamValidationException
        for user_id in request.data:
            self.realm_client.group_user_add(user_id, pk)
        return Response({"id": pk})

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING)
        ),
        operation_description="将一系列用户从组移除"
    )
    @action(detail=True, methods=["delete"], url_path="unassign_users")
    @uma_permission("SysGroup_user")
    def unassigned_group_users(self, request, pk: str):
        if not request.data:
            raise ParamValidationException
        for user_id in request.data:
            self.realm_client.group_user_remove(user_id, pk)
        return Response({"id": pk})

    @swagger_auto_schema(operation_description="获取该组下的所有角色")
    @action(detail=True, methods=["get"], url_path="roles")
    @uma_permission("SysGroup_role")
    def get_roles_in_group(self, request, pk: str):
        if not request.data:
            raise ParamValidationException
        roles = self.realm_client.get_group_realm_roles(pk)
        return Response(roles)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING)
        ),
        operation_description="将一系列角色添加到组"
    )
    @action(detail=True, methods=["patch"], url_path="assign_roles")
    @uma_permission("SysGroup_role")
    def assign_group_roles(self, request, pk: str):
        if not request.data:
            raise ParamValidationException
        self.realm_client.assign_group_realm_roles(pk, request.data)
        return Response({"id": pk})

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING)
        ),
        operation_description="将一系列角色从组移除"
    )
    @action(detail=True, methods=["delete"], url_path="unassign_roles")
    @uma_permission("SysGroup_role")
    def unassigned_group_roles(self, request, pk: str):
        if not request.data:
            raise ParamValidationException
        self.realm_client.delete_group_realm_roles(pk, request.data)
        return Response({"id": pk})


class KeycloakUserViewSet(viewsets.ViewSet):
    realm_client = KeyCloakClient().get_realm_client()

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("page", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("page_size", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("search", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter("roles", in_=openapi.IN_QUERY, type=openapi.TYPE_ARRAY, items=openapi.TYPE_STRING),
        ],
        operation_description="查询用户列表"
    )
    @uma_permission("SysUser_view")
    def list(self, request):
        _first, _max = get_first_and_max(request.query_params)
        roles = ast.literal_eval(request.query_params.get("roles", "[]"))

        users = self.realm_client.get_users(dict(first=_first, max=_max, search=request.query_params.get("search")))
        for user in users:
            user["groups"] = self.realm_client.get_user_groups(user["id"])
            user["group_roles"] = list()
            for group in user["groups"]:
                roles = self.realm_client.get_group_realm_roles(group["id"])
                user["group_roles"].extend(roles)
            user["roles"] = self.realm_client.get_realm_roles_of_user(user["id"])

        # TODO 查询角色下用户待优化
        # 根据roles字段筛用户
        if len(roles) != 0:
            users = [
                user for user in users if
                any(role["id"] in roles for role in user["roles"]) or
                any(group_role["id"] in roles for group_role in user["group_roles"])
            ]

        return Response({"count": len(users), "users": users})

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("page", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter("page_size", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
        ],
        operation_description="获取该角色下的所有用户"
    )
    @action(detail=False, methods=["get"], url_path="roles/<str:role_name>")
    @uma_permission("SysRole_users_manage")
    def get_users_in_role(self, request, role_name: str):
        _first, _max = get_first_and_max(request.query_params)
        result = self.realm_client.get_realm_role_members(role_name)
        return Response(result)

    @swagger_auto_schema(
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
        operation_description="创建用户"
    )
    @uma_permission("SysUser_create")
    def create(self, request):
        user_info = dict(
            username=request.data["username"],
            email=request.data.get("email"),
            lastName=request.data.get("lastName"),
            enabled=True,
            credentials=[{"value": request.data["password"], "type": "password"}],
        )
        normal_role = self.realm_client.get_realm_role(NORMAL)
        user_id = self.realm_client.create_user(user_info)
        self.realm_client.assign_realm_roles(user_id, normal_role)
        return Response({"id": id})

    @swagger_auto_schema(operation_description="删除用户")
    @uma_permission("SysUser_delete")
    def destroy(self, request, pk: str):
        self.realm_client.delete_user(pk)
        return Response({"id": pk})

    @swagger_auto_schema(
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
        operation_description="修改用户信息"
    )
    @uma_permission("SysUser_edit")
    def update(self, request, pk: str):
        self.realm_client.update_user(pk, request.data)
        return Response({"id": pk})

    @swagger_auto_schema(
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
        operation_description="重置用户密码"
    )
    @uma_permission("SysUser_edit")
    def partial_update(self, request, pk: str):
        self.realm_client.set_user_password(pk, request.data["password"], False)
        return Response({"id": pk})

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING)
        ),
        operation_description="将一系列组添加到用户"
    )
    @action(detail=True, methods=["patch"], url_path="assign_groups")
    def assign_user_groups(self, request, pk: str):
        for id in request.data:
            self.realm_client.group_user_add(pk, id)
        return Response()

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING)
        ),
        operation_description="将一系列组从该用户移除"
    )
    @action(detail=True, methods=["delete"], url_path="unassign_groups")
    def unassign_user_groups(self, request, pk: str):
        for id in request.data:
            self.realm_client.group_user_remove(pk, id)
        return Response()


class KeycloakRoleViewSet(viewsets.ViewSet):
    realm_client = KeyCloakClient().get_realm_client()

    @swagger_auto_schema(operation_description="获取所有角色")
    @uma_permission("SysRole_view")
    def list(self, request):
        result = self.realm_client.get_realm_roles()
        return Response(result)

    @swagger_auto_schema(operation_description="获取角色拥有的权限")
    @uma_permission("SysRole_view")
    def retrieve(self, request, pk: str):

        client_id = get_client_id(self.realm_client)
        policies = self.realm_client.get_client_authz_policies(client_id)
        policy_id = ""
        for policy in policies:
            if policy["name"] == pk:
                policy_id = policy["id"]
                break
        permissions = SupplementApi(self.realm_client.connection).get_permission_by_policy_id(client_id, policy_id)
        return Response(permissions)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "role_name": openapi.Schema(type=openapi.TYPE_STRING, description="Role name"),
                "description": openapi.Schema(type=openapi.TYPE_STRING, description="description"),
            },
            required=["role_name"]
        ),
        operation_description="创建角色"
    )
    @uma_permission("SysRole_create")
    def create(self, request):
        result = self.realm_client.create_realm_role(request.data)
        return Response(result)

    @swagger_auto_schema(operation_description="删除角色")
    @uma_permission("SysRole_delete")
    def destroy(self, request, pk: str):
        result = self.realm_client.delete_realm_role(pk)
        return Response(result)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING)
        ),
        operation_description="更改角色的权限状态，如果有切换为有，反之"
    )
    @action(detail=True, methods=["patch"], url_path="permissions")
    @uma_permission("SysRole_permissions")
    def ch_permission(self, request, pk: str):
        client_id = get_client_id(self.realm_client)
        all_permissions = self.realm_client.get_client_authz_permissions(client_id)

        # 获取角色映射的policy_id（角色与policy一对一映射）
        policies = self.realm_client.get_client_authz_policies(client_id)
        policy_id = ""
        for policy in policies:
            if policy["name"] == pk:
                policy_id = policy["id"]
                break

        # 判断权限是否需要更新
        permission_name_set = set(request.data)
        supplement_api = SupplementApi(self.realm_client.connection)
        for permission_info in all_permissions:

            permission_policies = supplement_api.get_policies_by_permission_id(client_id, permission_info["id"])
            permission_policy_ids = [i["id"] for i in permission_policies]

            # 需要绑定权限与角色的
            if permission_info["name"] in permission_name_set:
                if policy_id in permission_policy_ids:
                    continue
                permission_policy_ids.append(policy_id)

            # 需求解绑权限与角色的
            else:
                if policy_id not in permission_policy_ids:
                    continue
                permission_policy_ids.remove(policy_id)

            # 执行权限更新
            permission_info.update(policies=permission_policy_ids)
            supplement_api.update_permission(client_id, permission_info["id"], permission_info)

        return Response()

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("user_id", openapi.IN_PATH, description="user ID", type=openapi.TYPE_STRING),
        ],
        operation_description="将一个用户添加到角色"
    )
    @action(detail=True, methods=["put"], url_path="assign/(?P<user_id>[^/.]+)")
    @uma_permission("SysRole_users_manage")
    def assign_role(self, request, pk: str, user_id: str):
        role = self.realm_client.get_realm_role_by_id(pk)
        self.realm_client.assign_realm_roles(user_id, role)
        return Response()

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("user_id", openapi.IN_PATH, description="user ID", type=openapi.TYPE_STRING),
        ],
        operation_description="将一个用户从角色移除"
    )
    @action(detail=True, methods=["delete"], url_path="withdraw/(?P<user_id>[^/.]+)")
    @uma_permission("SysRole_users_manage")
    def withdraw_role(self, request, pk: str, user_id: str):
        role = self.realm_client.get_realm_role_by_id(pk)
        self.realm_client.delete_realm_roles_of_user(user_id, role)
        return Response()

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="User ID", type=openapi.TYPE_STRING)
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "description": openapi.Schema(type=openapi.TYPE_STRING, description="Role description")
            }
        )
    )
    @uma_permission("SysRole_edit")
    def update(self, request, pk: str):
        role = self.realm_client.get_realm_role_by_id(pk)
        self.realm_client.update_realm_role(role["name"], request.data)
        return Response()

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING)
        ),
        operation_description="将该角色添加到一系列组中"
    )
    @action(detail=True, methods=["patch"], url_path="assign_groups")
    def assign_groups(self, request, pk: str):
        role = self.realm_client.get_realm_role_by_id(pk)
        for group_id in request.data:
            self.realm_client.assign_group_realm_roles(group_id, role)
        return Response()

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING)
        ),
        operation_description="将该角色从一系列组中移除"
    )
    @action(detail=True, methods=["delete"], url_path="unassign_groups")
    def unassign_groups(self, request, pk: str):
        role = self.realm_client.get_realm_role_by_id(pk)
        for group_id in request.data:
            self.realm_client.delete_group_realm_roles(group_id, role)
        return Response()
