// 全文检索模块
import { post, reUrl } from '@/api/axiosconfig/axiosconfig'
export default {
    /**
     * 实例全文检索
     * @param {Object} params 请求参数
     */
    getFulltextSearchList(params = {}) {
        return post(`${reUrl}/instance/fulltext_search/`, params)
    }
}
