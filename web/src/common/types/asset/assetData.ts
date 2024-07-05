// 操作日志表格数据
export interface AssetRecordList {
    operator: string;
    operate_obj: string;
    operate_type: string;
    created_at: string;
    operate_summary: string;
    [key: string]: any
}
