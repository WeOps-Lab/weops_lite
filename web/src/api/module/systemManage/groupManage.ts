// 组织管理模块
import {get, deleteb, post, put, patch, reUrl} from '@/api/axiosconfig/axiosconfig'
export default {
    /**
     * 获取组织信息
     * @param {Object} params 请求参数
     */
    getGroups(params = {}) {
        return get(`${reUrl}/group/`, params)
    },
    /**
     * 新建组织
     * @param {Object} params 请求参数
     */
    addGroup(params = {}) {
        return post(`${reUrl}/group/`, params)
    },
    /**
     * 编辑组织
     * @param {Object} params 请求参数
     */
    editGroup(params = {}) {
        return put(`${reUrl}/group/${params.id}/`, params)
    },
    /**
     * 删除组织
     * @param {Object} params 请求参数
     */
    delGroup(params = {}) {
        return deleteb(`${reUrl}/group/delete_groups/`, params.deleteIds)
    },
    /**
     * 获取组的人员管理信息
     * @param {Object} params 请求参数
     */
    getGroupUsers(params = {}) {
        return get(`${reUrl}/group/${params.id}/users/`, {})
    },
    /**
     * 将一系列用户添加到组
     * @param {Object} params 请求参数
     */
    addGroupUsers(params = {}) {
        return patch(`${reUrl}/group/${params.id}/assign_users/`, params.addIds)
    },
    /**
     * 将一系列用户从组移除
     * @param {Object} params 请求参数
     */
    delGroupUsers(params = {}) {
        return deleteb(`${reUrl}/group/${params.id}/unassign_users/`, params.deleteIds)
    },
    /**
     * 获取组的角色信息
     * @param {Object} params 请求参数
     */
    getGroupRoles(params = {}) {
        return get(`${reUrl}/group/${params.id}/roles/`, {})
    },
    /**
     * 将一系列角色添加到组
     * @param {Object} params 请求参数
     */
    addGroupRoles(params = {}) {
        return patch(`${reUrl}/group/${params.id}/assign_roles/`, params.addIds)
    },
    /**
     * 将一系列角色从组移除
     * @param {Object} params 请求参数
     */
    delGroupRoles(params = {}) {
        return deleteb(`${reUrl}/group/${params.id}/unassign_roles/`, params.deleteIds)
    }
}
