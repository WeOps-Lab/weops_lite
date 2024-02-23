from drf_yasg import openapi

user_list_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "count": 7,
                "users": [
                    {
                        "id": "70579dc8-5f83-44e5-9465-d2cceb81b5fe",
                        "createdTimestamp": 1707026628277,
                        "username": "admin",
                        "enabled": True,
                        "totp": False,
                        "emailVerified": False,
                        "lastName": "超管",
                        "email": "admin1@qq.com",
                        "disableableCredentialTypes": [],
                        "requiredActions": [],
                        "notBefore": 0,
                        "access": {
                            "manageGroupMembership": True,
                            "view": True,
                            "mapRoles": True,
                            "impersonate": True,
                            "manage": True
                        },
                        "roles": [
                            {
                                "id": "476b1619-cefb-44e5-bf5d-eb3e5c18aa30",
                                "name": "测试",
                                "description": "测试角色",
                                "composite": False,
                                "clientRole": False,
                                "containerId": "0c3643d5-fc2e-4173-b5a3-4c36300c6d9b",
                                "role_type": "group"
                            },
                            {
                                "id": "75e20f66-af9b-418d-87a4-7f6ee45888bf",
                                "name": "admin",
                                "description": "本角色为超级管理员，有全部的权限",
                                "composite": True,
                                "clientRole": False,
                                "containerId": "0c3643d5-fc2e-4173-b5a3-4c36300c6d9b",
                                "role_type": "user"
                            },
                            {
                                "id": "2b989de4-8f82-4459-bf5f-9d0e2d983ce0",
                                "name": "测试角色",
                                "description": "",
                                "composite": False,
                                "clientRole": False,
                                "containerId": "0c3643d5-fc2e-4173-b5a3-4c36300c6d9b",
                                "role_type": "group"
                            }
                        ],
                        "groups": [
                            {
                                "id": "5989f073-7bb2-4796-9d78-00ca47b14f20",
                                "name": "dsad",
                                "path": "/test/dsad",
                                "parentId": "a74996c3-fe2e-401c-90b9-38e3fd01d068",
                                "subGroups": []
                            },
                            {
                                "id": "424c9439-bc18-42c7-b10a-706a8ecfb67e",
                                "name": "总公司",
                                "path": "/总公司",
                                "subGroups": []
                            }
                        ]
                    },
                    {
                        "id": "b771a5f5-8136-4e76-93ca-b9c5fefd4509",
                        "createdTimestamp": 1708326321151,
                        "username": "byf",
                        "enabled": True,
                        "totp": False,
                        "emailVerified": False,
                        "lastName": "中文名",
                        "email": "sdsadasd@163.com",
                        "disableableCredentialTypes": [],
                        "requiredActions": [],
                        "notBefore": 0,
                        "access": {
                            "manageGroupMembership": True,
                            "view": True,
                            "mapRoles": True,
                            "impersonate": True,
                            "manage": True
                        },
                        "roles": [
                            {
                                "id": "476b1619-cefb-44e5-bf5d-eb3e5c18aa30",
                                "name": "测试",
                                "description": "测试角色",
                                "composite": False,
                                "clientRole": False,
                                "containerId": "0c3643d5-fc2e-4173-b5a3-4c36300c6d9b",
                                "role_type": "group"
                            },
                            {
                                "id": "276672e0-0d25-4b2b-a561-e6cd4e3b728c",
                                "name": "normal",
                                "description": "本角色为普通用户，需要超级管理员赋予其他权限",
                                "composite": False,
                                "clientRole": False,
                                "containerId": "0c3643d5-fc2e-4173-b5a3-4c36300c6d9b",
                                "role_type": "user"
                            }
                        ],
                        "groups": [
                            {
                                "id": "424c9439-bc18-42c7-b10a-706a8ecfb67e",
                                "name": "总公司",
                                "path": "/总公司",
                                "subGroups": []
                            }
                        ]
                    },
                    {
                        "id": "0094f317-6be5-4001-992e-886366a0099e",
                        "createdTimestamp": 1707200997491,
                        "username": "dba",
                        "enabled": True,
                        "totp": False,
                        "emailVerified": False,
                        "lastName": "数据库管理员",
                        "email": "dba@qq.com",
                        "disableableCredentialTypes": [],
                        "requiredActions": [],
                        "notBefore": 0,
                        "access": {
                            "manageGroupMembership": True,
                            "view": True,
                            "mapRoles": True,
                            "impersonate": True,
                            "manage": True
                        },
                        "roles": [
                            {
                                "id": "476b1619-cefb-44e5-bf5d-eb3e5c18aa30",
                                "name": "测试",
                                "description": "测试角色",
                                "composite": False,
                                "clientRole": False,
                                "containerId": "0c3643d5-fc2e-4173-b5a3-4c36300c6d9b",
                                "role_type": "group"
                            }
                        ],
                        "groups": [
                            {
                                "id": "39d989d9-05bd-4c29-96a7-5067af822beb",
                                "name": "广州分公司",
                                "path": "/总公司/广州分公司",
                                "parentId": "424c9439-bc18-42c7-b10a-706a8ecfb67e",
                                "subGroups": []
                            }
                        ]
                    },
                ]
            }
        }
    )
}

user_info_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "70579dc8-5f83-44e5-9465-d2cceb81b5fe",
                "createdTimestamp": 1707026628277,
                "username": "admin",
                "enabled": True,
                "totp": False,
                "emailVerified": False,
                "lastName": "超管",
                "email": "admin1@qq.com",
                "disableableCredentialTypes": [],
                "requiredActions": [],
                "notBefore": 0,
                "access": {
                    "manageGroupMembership": True,
                    "view": True,
                    "mapRoles": True,
                    "impersonate": True,
                    "manage": True
                }
            }
        }
    )
}

user_list_by_role_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": [
                {
                    "id": "70579dc8-5f83-44e5-9465-d2cceb81b5fe",
                    "createdTimestamp": 1707026628277,
                    "username": "admin",
                    "enabled": True,
                    "totp": False,
                    "emailVerified": False,
                    "lastName": "超管",
                    "email": "admin1@qq.com",
                    "disableableCredentialTypes": [],
                    "requiredActions": [],
                    "notBefore": 0
                }
            ]
        }
    )
}

user_create_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "2ab3fc7e-5a31-4275-abb2-9b84410c6094"
            },
        }
    )
}

user_delete_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "2ab3fc7e-5a31-4275-abb2-9b84410c6094"
            }
        }
    )
}

user_update_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "b771a5f5-8136-4e76-93ca-b9c5fefd4509"
            }
        }
    )
}

user_reset_password_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "b771a5f5-8136-4e76-93ca-b9c5fefd4509"
            }
        }
    )
}

user_add_groups_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {}
        }
    )
}

user_remove_groups_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {}
        }
    )
}
