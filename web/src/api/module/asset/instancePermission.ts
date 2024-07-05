// 实例权限模块
import { post, get, reUrl, deletes, put } from '@/api/axiosconfig/axiosconfig'
export default {
    /**
     * 创建角色权限
     * @param {Object} params 请求参数
     */
    createInstPermission(params = {}) {
        return post(`${reUrl}/instance_permission/role/`, params)
    },
    /**
     * 获取角色实例权限列表
     * @param {Object} params 请求参数
     */
    getInstPermissionList(params = {}) {
        return get(`${reUrl}/instance_permission/role/`, params)
    },
    /**
     * 删除角色权限
     * @param {Object} params 请求参数
     */
    deleteInstPermissionList(params = {}) {
        return deletes(`${reUrl}/instance_permission/role/${params.id}/`)
    },
    /**
     * 更新角色实例权限
     * @param {Object} params 请求参数
     */
    updateInstPermission(params = {}) {
        return put(`${reUrl}/instance_permission/role/${params.id}/`, params)
    },
    /**
     * 查询角色实例权限详情
     * @param {Object} params 请求参数
     */
    getInstPermissionDetail(params = {}) {
        return get(`${reUrl}/instance/association/${params.id}/`)
    }
}
