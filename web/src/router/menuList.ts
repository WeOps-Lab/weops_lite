export const routeConfig = [
    {
        name: '资产',
        id: 'Asset',
        sortIndex: 6,
        auth: [
            {
                key: 'checkAuth',
                value: false,
                label: '查看',
                type: 'check'
            },
            {
                key: 'operateAuth',
                value: false,
                label: '操作',
                type: 'operate'
            }
        ],
        children: [
            {
                name: '资产搜索',
                icon: 'cw-icon weops-discover',
                id: 'AssetSearch',
                sortIndex: 7,
                auth: [
                    {
                        key: 'AssetSearch_view',
                        value: false,
                        label: '查看',
                        type: 'check',
                        apiKey: ['instance_fulltext_search', 'model_list', 'group_list', 'model_attr_list']
                    }
                ]
            },
            {
                name: '资产目录',
                icon: 'cw-icon weops-application',
                id: 'AssetsOverview',
                sortIndex: 8,
                auth: [
                    {
                        key: 'AssetsOverview_view',
                        value: false,
                        label: '查看',
                        type: 'check',
                        apiKey: ['model_list', 'model_inst_count']
                    }
                ]
            },
            {
                name: '资产数据',
                icon: 'cw-icon weops-template',
                id: 'AssetData',
                sortIndex: 9,
                auth: [
                    {
                        key: 'checkAuth',
                        value: false,
                        label: '查看',
                        type: 'check'
                    },
                    {
                        key: 'operateAuth',
                        value: false,
                        label: '操作',
                        type: 'operate'
                    }
                ],
                children: []
            },
            {
                name: '资产凭据',
                icon: 'cw-icon weops-user-permission',
                id: 'AssetCredential',
                sortIndex: 10,
                auth: [
                    {
                        key: 'AssetCredential_view',
                        value: false,
                        label: '查看',
                        type: 'check',
                        apiKey: ['model_list', 'model_attr_list', 'instance_list', 'group_list', 'instance_detail', 'instance_association_instance_list', 'model_association_type', 'topo_search', 'change_record_list', 'change_record_detail', 'cre_authorization_list']
                    },
                    {
                        key: 'AssetCredential_manage',
                        value: false,
                        label: '操作',
                        type: 'operate',
                        apiKey: ['instance_create', 'instance_update', 'instance_batch_update', 'instance_batch_delete', 'instance_association_create', 'instance_association_delete', 'cre_authorization']
                    }
                ]
            }
        ]
    },
    {
        name: '管理',
        id: 'Setting',
        sortIndex: 11,
        auth: [
            {
                key: 'checkAuth',
                value: false,
                label: '查看',
                type: 'check'
            },
            {
                key: 'operateAuth',
                value: false,
                label: '操作',
                type: 'operate'
            }
        ],
        children: [
            {
                name: '资产管理',
                icon: 'cw-icon weops-template',
                id: 'AssetManage',
                sortIndex: 12,
                auth: [
                    {
                        key: 'checkAuth',
                        value: false,
                        label: '查看',
                        type: 'check'
                    },
                    {
                        key: 'operateAuth',
                        value: false,
                        label: '操作',
                        type: 'operate'
                    }
                ],
                children: [
                    {
                        name: '模型管理',
                        id: 'ModelManage',
                        icon: 'cw-icon weops-user',
                        url: '/modelManage',
                        auth: [
                            {
                                key: 'ModelManage_view',
                                value: false,
                                label: '查看',
                                type: 'check',
                                apiKey: ['model_list', 'model_association_list', 'model_attr_list', 'model_association_type']
                            },
                            {
                                key: 'ModelManage_create',
                                value: false,
                                label: '创建模型',
                                type: 'operate',
                                apiKey: ['classification_create', 'model_create', 'model_association_create', 'model_attr_create']
                            },
                            {
                                key: 'ModelManage_edit',
                                value: false,
                                label: '编辑模型',
                                type: 'operate',
                                apiKey: ['classification_update', 'model_attr_update', 'model_update']
                            },
                            {
                                key: 'ModelManage_delete',
                                value: false,
                                label: '删除模型',
                                type: 'operate',
                                apiKey: ['classification_delete', 'model_delete', 'model_association_delete', 'model_attr_delete']
                            }
                        ]
                    }
                ]
            },
            {
                name: '系统管理',
                icon: 'cw-icon weops-system',
                id: 'sysManage',
                sortIndex: 13,
                auth: [
                    {
                        key: 'checkAuth',
                        value: false,
                        label: '查看',
                        type: 'check'
                    },
                    {
                        key: 'operateAuth',
                        value: false,
                        label: '操作',
                        type: 'operate'
                    }
                ],
                children: [
                    {
                        name: '组织管理',
                        id: 'SysGroup',
                        icon: 'cw-icon weops-user',
                        url: '/sysGroup',
                        auth: [
                            {
                                key: 'SysGroup_view',
                                value: false,
                                label: '查看',
                                type: 'check',
                                apiKey: ['group_list']
                            },
                            {
                                key: 'SysGroup_create',
                                value: false,
                                label: '创建组织',
                                type: 'operate',
                                apiKey: ['group_create']
                            },
                            {
                                key: 'SysGroup_edit',
                                value: false,
                                label: '编辑组织',
                                type: 'operate',
                                apiKey: ['group_update']
                            },
                            {
                                key: 'SysGroup_delete',
                                value: false,
                                label: '删除组织',
                                type: 'operate',
                                apiKey: ['group_delete']
                            },
                            {
                                key: 'SysGroup_role',
                                value: false,
                                label: '角色管理',
                                type: 'operate',
                                apiKey: ['group_users', 'user_list', 'group_add_users', 'group_remove_users']
                            },
                            {
                                key: 'SysGroup_user',
                                value: false,
                                label: '人员管理',
                                type: 'operate',
                                apiKey: ['group_roles', 'role_list', 'group_add_roles', 'group_remove_roles']
                            }
                        ]
                    },
                    {
                        name: '角色管理',
                        id: 'SysRole',
                        icon: 'cw-icon weops-role',
                        url: '/sysRole',
                        auth: [
                            {
                                key: 'SysRole_view',
                                value: false,
                                label: '查看',
                                type: 'check',
                                apiKey: ['role_list']
                            },
                            {
                                key: 'SysRole_create',
                                value: false,
                                label: '创建角色',
                                type: 'operate',
                                apiKey: ['role_create']
                            },
                            {
                                key: 'SysRole_edit',
                                value: false,
                                label: '编辑角色',
                                type: 'operate',
                                apiKey: ['role_update']
                            },
                            {
                                key: 'SysRole_delete',
                                value: false,
                                label: '删除角色',
                                type: 'operate',
                                apiKey: ['role_delete']
                            },
                            {
                                key: 'SysRole_users_manage',
                                value: false,
                                label: '人员管理',
                                type: 'operate',
                                apiKey: ['user_list_by_role', 'role_groups', 'user_list', 'group_list', 'role_remove_user', 'role_add_user', 'role_add_groups', 'role_remove_groups']
                            },
                            {
                                key: 'SysRole_permissions',
                                value: false,
                                label: '设置权限',
                                type: 'operate',
                                apiKey: ['role_permissions', 'role_set_permissions', 'r_permission_list', 'r_permission_create', 'r_permission_del', 'r_permission_update']
                            }
                        ]
                    },
                    {
                        name: '用户管理',
                        id: 'SysUser',
                        icon: 'cw-icon weops-user',
                        url: '/sysUser',
                        auth: [
                            {
                                key: 'SysUser_view',
                                value: false,
                                label: '查看',
                                type: 'check',
                                apiKey: ['user_list', 'role_list']
                            },
                            {
                                key: 'SysUser_create',
                                value: false,
                                label: '创建用户',
                                type: 'operate',
                                apiKey: ['user_create']
                            },
                            {
                                key: 'SysUser_edit',
                                value: false,
                                label: '编辑用户',
                                type: 'operate',
                                apiKey: ['user_update', 'user_reset_password', 'role_add_user', 'role_remove_user', 'role_list', 'group_list', 'user_remove_groups', 'user_add_groups']
                            },
                            {
                                key: 'SysUser_delete',
                                value: false,
                                label: '删除用户',
                                type: 'operate',
                                apiKey: ['user_delete']
                            }
                        ]
                    },
                    {
                        name: '操作日志',
                        id: 'SysLog',
                        icon: 'cw-icon weops-operation-log-fill',
                        url: '/sysLog',
                        auth: [
                            {
                                key: 'SysLog_view',
                                value: false,
                                label: '查看',
                                type: 'check',
                                apiKey: ['operation_log_list', 'operate_type_enum']
                            }
                        ]
                    },
                    {
                        name: '系统设置',
                        id: 'SysSetting',
                        icon: 'cw-icon weops-setting',
                        url: '/sysSetting',
                        auth: [
                            {
                                key: 'SysSetting_menus_view',
                                value: false,
                                label: '查看',
                                type: 'check',
                                apiKey: ['menu_list']
                            },
                            {
                                key: 'SysSetting_menus_create',
                                value: false,
                                label: '新增菜单',
                                type: 'operate',
                                apiKey: ['menu_create']
                            },
                            {
                                key: 'SysSetting_menus_edit',
                                value: false,
                                label: '编辑菜单',
                                type: 'operate',
                                apiKey: ['menu_update', 'menu_retrieve', 'menu_use']
                            },
                            {
                                key: 'SysSetting_menus_delete',
                                value: false,
                                label: '删除菜单',
                                type: 'operate',
                                apiKey: ['menu_delete']
                            },
                            {
                                key: 'SysSetting_logo_change',
                                value: false,
                                label: '更换logo',
                                type: 'operate',
                                apiKey: ['logo_update', 'logo_reset']
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
