// 操作类型
export const TYPE_LIST = [
    { id: 'add', name: '增加' },
    { id: 'modify', name: '修改' },
    { id: 'exec', name: '执行' },
    { id: 'delete', name: '删除' },
    { id: 'download', name: '下载' },
    { id: 'upload', name: '上传' },
    { id: 'login', name: '登录' }
]
// 操作日志表头
export const LOG_COLUMNS = [
    {
        label: '操作者',
        key: 'operator',
        align: 'left',
        minWidth: '100px'
    },
    {
        label: '操作对象',
        key: 'operate_obj',
        align: 'left',
        minWidth: '180px'
    },
    {
        label: '操作类型',
        key: 'operate_type',
        align: 'left',
        minWidth: '80px',
        scopedSlots: 'operate_type'
    },
    {
        label: '操作时间',
        key: 'created_at',
        align: 'left',
        minWidth: '100'
    },
    {
        label: '概要',
        key: 'operate_summary',
        align: 'left',
        minWidth: '240px'
    }
]
