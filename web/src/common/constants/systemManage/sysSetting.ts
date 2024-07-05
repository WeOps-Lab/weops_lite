// 系统设置tab
export const SYSSETTING_PANELS = [
    {
        name: 'MenuManage',
        label: '菜单设置',
        content: '菜单管理允许您灵活配置菜单，包括菜单项、菜单层级等，可以根据需要自定义菜单并启用，以便更好使用系统功能'
    },
    {
        name: 'LogoSetting',
        label: 'Logo设置',
        content: '您可以进行主题logo的替换，或者恢复默认'
    }
]
export const MENU_MANAGE_COLUMNS = [
    {
        label: '菜单名称',
        key: 'menu_name',
        minWidth: '200px'
    },
    {
        label: '创建人',
        key: 'created_by'
    },
    {
        label: '创建时间',
        key: 'created_at'
    },
    {
        label: '更新时间',
        key: 'updated_at'
    },
    {
        label: '操作',
        key: 'operation',
        width: '200px',
        prop: 'operation',
        scopedSlots: 'operation'
    }
]
