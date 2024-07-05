import ComTable from '@/components/comTable/index.vue'
import OperateRole from '../operateRole/index.vue'
import PermissionSettings from '../permissionSettings/index.vue'
import { Vue, Component } from 'vue-property-decorator'
import AuthWhiteList from '@/views/systemManage/userMange/components/authWhiteList/index.vue'
import PageExplanation from '@/components/pageExplanation/index.vue'
import UserAndGroup from '../userAndGroup/index.vue'
import { Pagination, TableData } from '@/common/types'
import { ROLE_MANAGE_COLUMNS } from '@/common/constants/systemManage/roleManage'
@Component({
    name: 'role-manage',
    components: {
        ComTable,
        OperateRole,
        PermissionSettings,
        AuthWhiteList,
        PageExplanation,
        UserAndGroup
    }
})
export default class RoleManage extends Vue {
    tableLoading: boolean = false
    dataList: Array<any> = []
    allDataList: Array<any> = []
    columns: Array<TableData> = ROLE_MANAGE_COLUMNS
    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    search: string = ''
    created() {
        this.getRoleList()
    }
    handlerIconClick() {
        this.pagination.current = 1
        this.dataList = this.allDataList.filter(item => item.name.includes(this.search))
        this.pagination.count = this.dataList.length
    }
    async personnelManage(row) {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: 'SysRole_users_manage'
        })) {
            return false
        }
        const res = await this.$api.RoleManageMain.getRoleAllUser({ name: row.name })
        res.data = res.data.map(item => ({
            id: item.id,
            bk_username: item.username,
            chname: item.lastName
        }))
        const detailRes = await this.$api.RoleManageMain.getRoleDetail({ name: row.name })
        this.$refs.userAndGroup.showSlider({
            user: res.data,
            group: detailRes.data
        }, row)
    }
    setPermission(row) {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: 'SysRole_permissions'
        })) {
            return false
        }
        const permissionSettings: any = this.$refs.permissionSettings
        permissionSettings.show(row)
    }
    operateRole(type, data?) {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: type === 'edit' ? 'SysRole_edit' : 'SysRole_create'
        })) {
            return false
        }
        const operateRole: any = this.$refs.operateRole
        operateRole.show(type, data)
    }
    refreshList() {
        this.getRoleList()
    }
    deleteRole(row) {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: 'SysRole_delete'
        })) {
            return false
        }
        this.$confirm('确认要删除该角色？', {
            center: true
        }).then(async() => {
            await this.confirmDelete(row)
        })
    }
    async confirmDelete(row) {
        try {
            const res = await this.$api.RoleManageMain.deleteRole({
                name: row.name
            })
            if (!res.result) {
                this.$error(res.message)
            } else {
                this.$success('删除成功!')
                if (this.pagination.current > 1 && this.dataList.length === 1) {
                    this.pagination.current--
                }
                this.getRoleList()
            }
            return true
        } catch (e) {
            return false
        }
    }
    getRoleList() {
        this.tableLoading = true
        this.$api.RoleManageMain.getRoleList().then(res => {
            if (!res.result) {
                return false
            }
            this.allDataList = res.data.map(item => {
                return {
                    ...item,
                    created: item.attributes?.created?.[0]
                }
            })
            // 三个角色置顶，其他角色按照创建时间排序
            const topDataName = ['admin', 'grade_admin', 'normal']
            const orderMap = {
                admin: 0,
                grade_admin: 1,
                normal: 2
            }
            const topData = []
            const otherData = []
            this.allDataList.forEach(item => {
                if (topDataName.includes(item.name)) {
                    topData.push(item)
                } else {
                    otherData.push(item)
                }
            })
            topData.sort((a, b) => orderMap[a.name] - orderMap[b.name])
            this.allDataList = [...topData, ...otherData.sort((a, b) => Date.parse(b.created) - Date.parse(a.created))]
            const { current, limit } = this.pagination
            this.dataList = this.allDataList.slice((current - 1) * limit, current * limit)
            this.pagination.count = res.data.length
        }).finally(() => {
            this.tableLoading = false
        })
    }
    handlePageChange(val) {
        this.pagination.current = val
        const { limit } = this.pagination
        this.dataList = this.allDataList.filter(item => item.name.includes(this.search)).slice((val - 1) * limit, val * limit)
    }
    limitChange(val) {
        this.pagination.current = 1
        this.pagination.limit = val
        this.dataList = this.allDataList.filter(item => item.name.includes(this.search)).slice(0, val)
    }
}
