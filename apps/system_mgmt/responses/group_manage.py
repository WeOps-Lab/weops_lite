from drf_yasg import openapi

group_list_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": [
                {
                    "id": "17ecc8b9-804f-4a1f-a280-49a983393cea",
                    "name": "kayla公司",
                    "path": "/kayla公司",
                    "subGroupCount": 1,
                    "subGroups": [
                        {
                            "id": "55dc0b54-88ab-493e-b0c0-ab19b8da62a2",
                            "name": "分公司",
                            "path": "/kayla公司/分公司",
                            "parentId": "17ecc8b9-804f-4a1f-a280-49a983393cea",
                            "subGroupCount": 0,
                            "subGroups": [],
                            "access": {
                                "view": True,
                                "viewMembers": True,
                                "manageMembers": True,
                                "manage": True,
                                "manageMembership": True
                            }
                        }
                    ],
                    "access": {
                        "view": True,
                        "viewMembers": True,
                        "manageMembers": True,
                        "manage": True,
                        "manageMembership": True
                    }
                },
                {
                    "id": "a74996c3-fe2e-401c-90b9-38e3fd01d068",
                    "name": "test",
                    "path": "/test",
                    "subGroupCount": 1,
                    "subGroups": [
                        {
                            "id": "5989f073-7bb2-4796-9d78-00ca47b14f20",
                            "name": "dsad",
                            "path": "/test/dsad",
                            "parentId": "a74996c3-fe2e-401c-90b9-38e3fd01d068",
                            "subGroupCount": 0,
                            "subGroups": [],
                            "access": {
                                "view": True,
                                "viewMembers": True,
                                "manageMembers": True,
                                "manage": True,
                                "manageMembership": True
                            }
                        }
                    ],
                    "access": {
                        "view": True,
                        "viewMembers": True,
                        "manageMembers": True,
                        "manage": True,
                        "manageMembership": True
                    }
                },
                {
                    "id": "424c9439-bc18-42c7-b10a-706a8ecfb67e",
                    "name": "总公司",
                    "path": "/总公司",
                    "subGroupCount": 2,
                    "subGroups": [
                        {
                            "id": "ceb14a55-6801-4bad-a9f1-0b67f35f6124",
                            "name": "sss",
                            "path": "/总公司/sss",
                            "parentId": "424c9439-bc18-42c7-b10a-706a8ecfb67e",
                            "subGroupCount": 0,
                            "subGroups": [],
                            "access": {
                                "view": True,
                                "viewMembers": True,
                                "manageMembers": True,
                                "manage": True,
                                "manageMembership": True
                            }
                        },
                        {
                            "id": "39d989d9-05bd-4c29-96a7-5067af822beb",
                            "name": "广州分公司",
                            "path": "/总公司/广州分公司",
                            "parentId": "424c9439-bc18-42c7-b10a-706a8ecfb67e",
                            "subGroupCount": 0,
                            "subGroups": [],
                            "access": {
                                "view": True,
                                "viewMembers": True,
                                "manageMembers": True,
                                "manage": True,
                                "manageMembership": True
                            }
                        }
                    ],
                    "access": {
                        "view": True,
                        "viewMembers": True,
                        "manageMembers": True,
                        "manage": True,
                        "manageMembership": True
                    }
                }
            ]
        }
    )
}
group_retrieve_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "17ecc8b9-804f-4a1f-a280-49a983393cea",
                "name": "kayla公司",
                "path": "/kayla公司",
                "subGroupCount": 1,
                "subGroups": [],
                "attributes": {},
                "realmRoles": [],
                "clientRoles": {},
                "access": {
                    "view": True,
                    "viewMembers": True,
                    "manageMembers": True,
                    "manage": True,
                    "manageMembership": True
                }
            }
        }
    )
}
group_create_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "e98abdd8-1aa7-4cb4-bc6f-30f195d31ff0"
            }
        }
    )
}
group_update_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "e98abdd8-1aa7-4cb4-bc6f-30f195d31ff0"
            }
        }
    )
}
group_delete_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {}
        }
    )
}
group_users_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": [
                {
                    "id": "b771a5f5-8136-4e76-93ca-b9c5fefd4509",
                    "createdTimestamp": 1708326321151,
                    "username": "byf",
                    "enabled": True,
                    "totp": False,
                    "emailVerified": False,
                    "firstName": "string",
                    "lastName": "string",
                    "email": "sdsadasd@163.com",
                    "disableableCredentialTypes": [],
                    "requiredActions": [],
                    "notBefore": 0
                },
                {
                    "id": "da6c42a5-ab98-4529-8bfb-cbd8b0c9e58e",
                    "createdTimestamp": 1708496422154,
                    "username": "kayla",
                    "enabled": True,
                    "totp": False,
                    "emailVerified": False,
                    "lastName": "蒙蒙",
                    "disableableCredentialTypes": [],
                    "requiredActions": [],
                    "notBefore": 0
                }
            ]
        }
    )
}
group_add_users_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "e98abdd8-1aa7-4cb4-bc6f-30f195d31ff0"
            }
        }
    )
}
group_remove_users_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "e98abdd8-1aa7-4cb4-bc6f-30f195d31ff0"
            }
        }
    )
}
group_roles_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": [
                {
                    "id": "c629ddf0-12ca-4ae9-9747-439371eaaba7",
                    "name": "普通角色",
                    "description": "普通角色",
                    "composite": False,
                    "clientRole": False,
                    "containerId": "0c3643d5-fc2e-4173-b5a3-4c36300c6d9b"
                }
            ]
        }
    )
}
group_add_roles_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "e98abdd8-1aa7-4cb4-bc6f-30f195d31ff0"
            }
        }
    )
}
group_remove_roles_responses = {
    200: openapi.Response(
        "成功",
        examples={
            "application/json": {
                "id": "e98abdd8-1aa7-4cb4-bc6f-30f195d31ff0"
            }
        }
    )
}