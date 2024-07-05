// 资产数据模块
import { get, deletes, post, patch, reUrl } from '@/api/axiosconfig/axiosconfig'
export default {
    /**
     * 查询实例列表
     * @param {Object} params 请求参数
     */
    getInstanceList(params = {}) {
        return post(`${reUrl}/instance/search/`, params)
    },
    /**
     * 创建实例
     * @param {Object} params 请求参数
     */
    createInstance(params = {}) {
        return post(`${reUrl}/instance/`, params)
    },
    /**
     * 修改实例
     * @param {Object} params 请求参数
     */
    updateInstance(params = {}) {
        return patch(`${reUrl}/instance/${params.id}/`, params.body)
    },
    /**
     * 批量删除实例
     * @param {Object} params 请求参数
     */
    deleteInstance(params = {}) {
        return post(`${reUrl}/instance/batch_delete/`, params.body)
    },
    /**
     * 实例详情
     * @param {Object} params 请求参数
     */
    getInstDetial(params = {}) {
        return get(`${reUrl}/instance/${params.id}/`)
    },
    /**
     * 查询某个实例的所有关联实例
     * @param {Object} params 请求参数
     */
    getAssoInstList(params = {}) {
        return get(`${reUrl}/instance/association_instance_list/${params.model_id}/${params.inst_id}/`, params.body)
    },
    /**
     * 创建实例关联
     * @param {Object} params 请求参数
     */
    createInstAsso(params = {}) {
        return post(`${reUrl}/instance/association/`, params)
    },
    /**
     * 删除实例关联
     * @param {Object} params 请求参数
     */
    deleteInstAsso(params = {}) {
        return deletes(`${reUrl}/instance/association/${params.id}/`)
    },
    /**
     * 删除实例关联
     * @param {Object} params 请求参数
     */
    getRelatedList(params = {}) {
        return get(`${reUrl}/instance/instance_association/${params.model_id}/${params.inst_id}/`)
    },
    /**
    * 下载导入模板
    * @param {Object} params 请求参数
    */
    downloadTemplate(params = {}) {
        return get(`${reUrl}/instance/${params.id}/download_template/`, {}, { responseType: 'blob' })
    },
    /**
    * 实例导出
    * @param {Object} params 请求参数
    */
    exportInst(params = {}) {
        return post(`${reUrl}/instance/${params.id}/inst_export/`, params.body, { responseType: 'blob' })
    },
    /**
    * 实例导入
    * @param {Object} params 请求参数
    */
    importInst(params = {}) {
        return post(`${reUrl}/instance/${params.id}/inst_import/`, params.body)
    },
    /**
     * 查询实例拓扑
     * @param {Object} params 请求参数
     */
    getInstanceTopo(params = {}) {
        return get(`${reUrl}/instance/topo_search/${params.model_id}/${params.inst_id}/`)
    },
    /**
     * 实例列表展示字段
     * @param {Object} params 请求参数
     */
    getShowFields(params = {}) {
        return get(`${reUrl}/instance/${params.model_id}/show_field/detail/`)
    },
    /**
    * 设置实例列表展示字段
    * @param {Object} params 请求参数
    */
    setShowFields(params = {}) {
        return post(`${reUrl}/instance/${params.model_id}/show_field/settings/`, params.body)
    },
    /**
    * 批量修改实例
    * @param {Object} params 请求参数
    */
    batchUpdate(params = {}) {
        return post(`${reUrl}/instance/batch_update/`, params)
    },
    /**
     * 实例列表展示字段
     * @param {Object} params 请求参数
     */
    getModelInstCount(params = {}) {
        return get(`${reUrl}/instance/model_inst_count/`, params)
    },
    /**
     * 查询变更记录列表
     * @param {Object} params 请求参数
     */
    getChangeRecordList(params = {}) {
        return get(`${reUrl}/change_record/`, params)
    },
    /**
     * 查询变更记录详情
     * @param {Object} params 请求参数
     */
    getChangeRecordDetail(params = {}) {
        return get(`${reUrl}/change_record/${params.id}/`)
    },
    /**
     * 获取变更类型枚举数据
     * @param {Object} params 请求参数
     */
    getRecordType(params = {}) {
        return get(`${reUrl}/change_record/enum_data/`)
    },
    /**
     * 凭据授权
     * @param {Object} params 请求参数
     */
    credentialAuthorization(params = {}) {
        return post(`${reUrl}/credential/authorization/`, params)
    },
    /**
     * 查询授权列表
     * @param {Object} params 请求参数
     */
    getAuthorizationList(params = {}) {
        return get(`${reUrl}/credential/authorization_list/${params.model_id}/${params.inst_id}/`)
    }
}
