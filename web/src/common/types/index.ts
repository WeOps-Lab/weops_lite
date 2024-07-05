// 公用分页数据
export interface Pagination {
    current: number,
    count: number,
    limit: number,
    small?: boolean,
    [key: string]: any
}
// 公用表格数据
export interface TableData {
    label?: string,
    key?: string,
    minWidth?: string | number,
    [key: string]: any
}
// 公用校验规则
export interface Rule {
    required?: boolean,
    message?: string,
    trigger: string,
    type?: string,
    [key: string]: any
}
// 公用tab
export interface Panels {
    label: string,
    name: string,
    [key: string]: any
}
