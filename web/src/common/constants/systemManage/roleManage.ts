// 角色管理表头
export const ROLE_MANAGE_COLUMNS = [
    {
        label: '角色名称',
        key: 'name',
        align: 'left',
        minWidth: '100px'
    },
    {
        label: '角色描述',
        key: 'description',
        align: 'left',
        minWidth: '300px'
    },
    {
        label: '上级角色',
        key: 'superior_role',
        align: 'left',
        minWidth: '100px'
    },
    {
        label: '是否内置',
        key: 'built_in',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'built_in'
    },
    {
        label: '操作',
        key: 'operation',
        align: 'left',
        width: '280px',
        scopedSlots: 'operation'
    }
]
// 人员表头
export const USER_COLUMNS = [
    {
        type: 'selection'
    },
    {
        label: '中文名',
        key: 'chname'
    },
    {
        label: '用户名',
        key: 'bk_username'
    }
]
// 人员和组织tab
export const ROLE_PANELS = [
    {
        label: '人员',
        name: 'user'
    },
    {
        label: '组织',
        name: 'group'
    }
]
// 角色管理表头
export const ASSET_AUTH_COLUMNS = [
    {
        label: '资产模型',
        key: 'model_id',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'model_id'
    },
    {
        label: '权限类型',
        key: 'permission_type',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'permission_type'
    },
    {
        label: '资产范围',
        key: 'resource_type',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'resource_type'
    },
    {
        label: '操作',
        key: 'operation',
        align: 'left',
        width: '100px',
        scopedSlots: 'operation'
    }
]
