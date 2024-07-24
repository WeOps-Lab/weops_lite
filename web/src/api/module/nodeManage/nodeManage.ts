// 用户管理模块
import {get, deletes, post, reUrl} from '@/api/axiosconfig/axiosconfig'
export default {
    /**
     * 获取节点列表数据
     *
     * @param {Object} params 请求参数
     */
    getNodeList(params = {}) {
        return get(`${reUrl}/node/`, params)
    },
    /**
     * 批量创建节点
     * @param {Object} params 请求参数
     */
    createNodes(params = {}) {
        return post(`${reUrl}/node/batch_create/`, params.body)
    },
    /**
     * 删除节点
     * @param {Object} params 请求参数
     */
    deleteNode(params = {}) {
        return deletes(`${reUrl}/node/${params.id}/`)
    },
    /**
     * 查询节点管理的枚举值
     *
     * @param {Object} params 请求参数
     */
    getNodeEnum(params = {}) {
        return get(`${reUrl}/node/enum/`, params)
    }
}
