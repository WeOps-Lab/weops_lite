from drf_yasg import openapi

role_list_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": [
                {
                    "id": "276672e0-0d25-4b2b-a561-e6cd4e3b728c",
                    "name": "normal",
                    "description": "本角色为普通用户，需要超级管理员赋予其他权限",
                    "composite": False,
                    "clientRole": False,
                    "containerId": "0c3643d5-fc2e-4173-b5a3-4c36300c6d9b"
                },
                {
                    "id": "75e20f66-af9b-418d-87a4-7f6ee45888bf",
                    "name": "admin",
                    "description": "本角色为超级管理员，有全部的权限",
                    "composite": True,
                    "clientRole": False,
                    "containerId": "0c3643d5-fc2e-4173-b5a3-4c36300c6d9b"
                },
                {
                    "id": "561403a8-208a-4901-b7f7-4dc0937db461",
                    "name": "grade_admin",
                    "description": "本角色为分级管理员，有二次授权权限",
                    "composite": False,
                    "clientRole": False,
                    "containerId": "0c3643d5-fc2e-4173-b5a3-4c36300c6d9b"
                }
            ]
        }
    )
}
role_permissions_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": [
                "SysLog_view",
                "operation_log_list",
            ]
        }
    )
}
role_create_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "906ccb57-84bb-488d-879a-f3a6b15a2b19",
                "name": "string",
                "description": "string",
                "composite": False,
                "clientRole": False,
                "containerId": "0c3643d5-fc2e-4173-b5a3-4c36300c6d9b",
                "attributes": {}
            }
        }
    )
}
role_delete_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {}
        }
    )
}
role_update_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {}
        }
    )
}
role_set_permissions_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {}
        }
    )
}
role_add_user_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {}
        }
    )
}
role_remove_user_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {}
        }
    )
}
role_add_groups_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {}
        }
    )
}
role_remove_groups_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {}
        }
    )
}
role_groups_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": [
                {
                    "id": "a74996c3-fe2e-401c-90b9-38e3fd01d068",
                    "name": "test",
                    "path": "/test",
                    "subGroups": []
                },
                {
                    "id": "424c9439-bc18-42c7-b10a-706a8ecfb67e",
                    "name": "总公司",
                    "path": "/总公司",
                    "subGroups": []
                }
            ]
        }
    )
}
