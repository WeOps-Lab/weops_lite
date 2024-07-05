import comTable from '@/components/comTable/index.vue'
import resetPassword from '../resetPassword/index.vue'
import operateUser from '../operateUser/index.vue'
import { Vue, Component } from 'vue-property-decorator'
import GroupSetting from '../groupSetting/index.vue'
import RoleManage from '../roleManage/index.vue'
import PageExplanation from '@/components/pageExplanation/index.vue'
import { Pagination, TableData } from '@/common/types'
import { USER_COLUMNS } from '@/common/constants/systemManage/userMange'
@Component({
    name: 'user-manage',
    components: {
        comTable,
        resetPassword,
        operateUser,
        GroupSetting,
        RoleManage,
        PageExplanation
    }
})
export default class UserManage extends Vue {
    tableLoading: boolean = false
    dataList: Array<any> = []
    columns: Array<TableData> = USER_COLUMNS
    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    rolList: Array<any> = []
    search: string = ''
    roles: Array<any> = []
    created() {
        this.getUserList()
        this.getRoleList()
    }
    // 获取用户拥有的全部角色
    getRoles(row) {
        return (row.roles || []).map(item => item.name).join('; ') || '--'
    }
    getOrganizationOrSuperior(row, { listKey, fieldKey }) {
        return (row[listKey] || []).map(item => item[fieldKey].slice(1)).join(';') || '--'
    }
    sourceFilterMethod(val) {
        this.roles = Object.values(val).flat()
        this.handlerIconClick()
    }
    // 删除用户角色
    changeRole(data) {
        setTimeout(() => {
            // this.confirmSetRole(data)
            const deleteRolesId = []
            const arr1 = data.roleV1
            const arr2 = data.allRoles
            for (let i = 0; i < arr1.length; i++) {
                if (!arr2.includes(arr1[i])) {
                    deleteRolesId.push(arr1[i])
                }
            }
            const deletePromises = deleteRolesId.map(id => {
                return this.$api.RoleManageMain.deleteUserRole({ id: id, userId: data.id })
            })
            this.tableLoading = true
            Promise.all(deletePromises).then(res => {
                if (res.every(item => item.result)) {
                    this.getUserList()
                }
            }).finally(() => {
                this.tableLoading = false
            })
        }, 0)
    }

    refreshList() {
        this.getUserList()
    }
    handlerIconClick() {
        this.pagination.current = 1
        this.getUserList()
    }
    operateUser(type, data?) {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: type === 'edit' ? 'SysUser_edit' : 'SysUser_create'
        })) {
            return false
        }
        const operateUser: any = this.$refs.operateUser
        operateUser.show(type, data)
    }
    resetPassword(row) {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: 'SysRole_edit'
        })) {
            return false
        }
        const resetPassword: any = this.$refs.resetPassword
        resetPassword.show(row)
    }
    deleteUser(row) {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: 'SysUser_delete'
        })) {
            return false
        }
        this.$confirm('确认要删除该用户？', {
            center: true
        }).then(async() => {
            await this.confirmDelete(row)
        })
    }
    async confirmDelete(row) {
        try {
            const res = await this.$api.UserManageMain.deleteUser({
                id: row.id,
                bk_user_id: row.bk_user_id
            })
            if (!res.result) {
                return this.$error(res.message)
            }
            this.$success('删除成功')
            if (this.pagination.current > 1 && this.dataList.length === 1) {
                this.pagination.current--
            }
            this.getUserList()
            // this.$store.dispatch('getAllUserList')
        } catch (e) {
            return false
        }
    }
    setUserRole(data) {
        const flag = data.allRoles.sort().toString() === data.roleV1.sort().toString()
        if (data.allRoles.length !== data.roleV1.length || (data.allRoles.length === data.roleV1.length && !flag)) {
            this.confirmSetRole(data)
        }
    }
    confirmSetRole(data) {
        // 要添加的角色
        const addRolesId = this.compareArrays(data.allRoles, data.roleV1)
        // 要删除的角色
        const deleteRolesId = this.compareArrays(data.roleV1, data.allRoles)
        const addPromises = addRolesId.map(id => {
            return this.$api.UserManageMain.setUserRoles({ id: id, userId: data.id })
        })
        const deletePromise = deleteRolesId.map(id => {
            return this.$api.RoleManageMain.deleteUserRole({ id: id, userId: data.id })
        })
        this.tableLoading = true
        Promise.all([...addPromises, ...deletePromise]).then(res => {
            if (res.every(item => item.result)) {
                this.$success('设置成功！')
                this.getUserList()
            }
        }).finally(() => {
            this.tableLoading = false
        })
    }
    getUserList() {
        const params = {
            roles: this.roles,
            page: this.pagination.current,
            page_size: this.pagination.limit,
            search: this.search
        }
        this.tableLoading = true
        this.$api.UserManageMain.getUserList(params).then(res => {
            if (!res.result) {
                return false
            }
            this.dataList = res.data.users
            this.dataList.forEach(item => {
                // 合并去重，用于显示角色列表
                const allRoles = this.dataList
                // 设置allRoles，allRoles与v-model绑定
                this.$set(item, 'allRoles', allRoles)
                // roleV1存放原始角色数据
                this.$set(item, 'roleV1', allRoles)
            })
            this.pagination.count = res.data.count
        }).finally(() => {
            this.tableLoading = false
        })
    }
    getRoleList() {
        this.$api.RoleManageMain.getRoleList().then(res => {
            if (!res.result) {
                return false
            }
            this.roleList = res.data.map(item => {
                return {
                    id: item.id,
                    name: item.name
                }
            })
        })
    }
    handlePageChange(val) {
        this.pagination.current = val
        this.getUserList()
    }
    limitChange(val) {
        this.pagination.current = 1
        this.pagination.limit = val
        this.getUserList()
    }
    // 传入两个数组，返回第一个数组比第二个数组多的项
    compareArrays(arrayA, arrayB) {
        const valuesOnlyInA = arrayA.filter(item => !arrayB.includes(item))
        return valuesOnlyInA
    }
    // 设置角色
    operateRole(row) {
        this.$refs.roleManage.showSlider({
            role: row.roles || [],
            group_role: row.group_roles || []
        }, row)
    }
    // 设置组织
    operateGroup(row) {
        const operateGroup: any = this.$refs.operateGroup
        operateGroup.show(row.groups || [], row.id)
    }
    // 设置组织完成后调用，重新获得数据
    confirm() {
        this.getUserList()
        this.getRoleList()
    }
}
