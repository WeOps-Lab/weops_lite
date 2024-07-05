// 角色管理模块
import {get, deletes, post, put, patch, reUrl, deleteb} from '@/api/axiosconfig/axiosconfig'
export default {
    /**
     * 获取角色列表数据
     *
     * @param {Object} params 请求参数
     */
    getRoleList(params = {}) {
        return get(`${reUrl}/role/`, params)
    },
    /**
     * 删除角色
     *
     * @param {Object} params 请求参数
     */
    deleteRole(params = {}) {
        return deletes(`${reUrl}/role/${params.name}/`, {})
    },
    /**
     * 新增角色
     *
     * @param {Object} params 请求参数
     */
    createRole(params = {}) {
        return post(`${reUrl}/role/`, params)
    },
    /**
     * 编辑角色
     *
     * @param {Object} params 请求参数
     */
    editRole(params = {}) {
        return put(`${reUrl}/role/${params.name}/`, params)
    },
    /**
     * 将一个用户从角色移除
     *
     * @param {Object} params 请求参数
     */
    deleteUserRole(params = {}) {
        return deletes(`${reUrl}/role/${params.id}/withdraw/${params.userId}/`, {})
    },
    /**
     * 获取该角色下的所有用户
     *
     * @param {Object} params 请求参数
     */
    getRoleAllUser(params = {}) {
        return get(`${reUrl}/user/roles/${params.name}/`, {})
    },
    /**
     * 设置角色菜单权限
     *
     * @param {Object} params 请求参数
     */
    setRoleMenu(params = {}) {
        return patch(`${reUrl}/role/${params.name}/permissions/`, params.array)
    },
    /**
     * 获取角色菜单
     *
     * @param {Object} params 请求参数
     */
    getRoleMenus(params = {}) {
        return get(`${reUrl}/role/${params.roleId}/permissions/`, {})
    },
    /**
     * 将该角色添加到一系列组中
     *
     * @param {Object} params 请求参数
     */
    addRoleGroups(params = {}) {
        return patch(`${reUrl}/role/${params.id}/assign_groups/`, params.addGroupId)
    },
    /**
     * 将该角色一系列组中移除
     *
     * @param {Object} params 请求参数
     */
    delRoleGroups(params = {}) {
        return deleteb(`${reUrl}/role/${params.id}/unassign_groups/`, params.deleteGroupId)
    },
    /**
     * 获取角色拥有的权限
     *
     * @param {Object} params 请求参数
     */
    getRoleDetail(params = {}) {
        return get(`${reUrl}/role/groups/${params.name}/`, {})
    }
}
