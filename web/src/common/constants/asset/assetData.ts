// 约束条件
export const ASSET_DTIAL_PANELS = [
    {
        label: '基本信息',
        name: 'baseInfo'
    },
    {
        label: '关联信息',
        name: 'assoInfo'
    },
    {
        label: '变更记录',
        name: 'assetRecord'
    },
    {
        label: '资产凭据',
        name: 'assetCredential'
    }
]
// 操作日志表头
export const ASSET_RECORD_COLUMNS = [
    {
        label: '时间',
        key: 'created_at',
        align: 'left',
        minWidth: '100'
    },
    {
        label: '操作人',
        key: 'operator',
        scopedSlots: 'operator',
        align: 'left',
        minWidth: '100px'
    },
    {
        label: '操作类型',
        key: 'type',
        align: 'left',
        minWidth: '80px',
        scopedSlots: 'type'
    },
    {
        label: '操作',
        key: 'operation',
        align: 'left',
        width: '100px',
        scopedSlots: 'operation'
    }
]
