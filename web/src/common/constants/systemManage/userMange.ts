export const GROUP_COLUMNS = [
    {
        type: 'selection'
    },
    {
        label: '角色名称',
        key: 'role_name'
    },
    {
        label: '用户数',
        key: 'user_count'
    }
]

export const AUTH_PANELS = [
    {
        label: '角色',
        name: 'role'
    },
    {
        label: '用户',
        name: 'user'
    }
]

export const USER_COLUMNS = [
    {
        label: '用户名',
        key: 'username',
        align: 'left',
        minWidth: '150px'
    },
    {
        label: '中文名',
        key: 'lastName',
        align: 'left',
        minWidth: '100px'
    },
    {
        label: '邮箱',
        key: 'email',
        align: 'left',
        minWidth: '150px'
    },
    {
        label: '用户角色',
        key: 'roles',
        align: 'left',
        minWidth: '220px',
        scopedSlots: 'roles'
        // filters: [],
        // filterRemote: true,
        // filterMultiple: true
    },
    {
        label: '组织',
        key: 'groups',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'groups'
    },
    {
        label: '操作',
        key: 'operation',
        align: 'left',
        width: '330px',
        fixed: 'right',
        scopedSlots: 'operation'
    }
]
export const ROLE_COLUMNS = [
    {
        type: 'selection',
        selectable: row => row.role_type !== 'group'
    },
    {
        label: '角色名称',
        key: 'name'
    },
    {
        label: '角色描述',
        key: 'description'
    }
]
