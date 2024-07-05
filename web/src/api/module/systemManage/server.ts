// server模块（各模块）api
import { get, post, put, reUrl } from '@/api/axiosconfig/axiosconfig'

// 返回在vue模板中的调用接口
export default {
    getLogo: function(params, config) {
        return get(reUrl + '/logo/', params, config)
    },
    updateLogo: function(params) {
        return put(reUrl + '/logo/', params)
    },
    getLogs: function(params) {
        return get(reUrl + '/operation_log/', params)
    },
    getOperateType: function(params = {}) {
        return get(reUrl + '/operation_log/custom/operate_type/enum/', params)
    },
    resetlogo: function(params) {
        return post(reUrl + '/logo/reset/', params, { showLoad: true })
    }
}
