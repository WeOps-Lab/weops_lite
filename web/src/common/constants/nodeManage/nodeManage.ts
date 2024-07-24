export const NODE_MANAGE_COLUMNS = [
    {
        label: '实例名',
        key: 'node_name',
        align: 'left',
        minWidth: '100px'
    },
    {
        label: 'IP地址',
        key: 'node_ip',
        align: 'left',
        minWidth: '100px'
    },
    {
        label: '资产模型',
        key: 'model_id',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'model_id'
    },
    {
        label: '控制器状态',
        key: 'sidecar_status',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'sidecar_status',
        filters: [],
        filterRemote: true,
        filterMultiple: false
    },
    {
        label: '操作',
        key: 'operation',
        align: 'left',
        width: '160px',
        scopedSlots: 'operation'
    }
]
