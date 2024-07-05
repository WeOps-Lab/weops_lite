import MenuTab from '@/components/menuTab/index.vue'
import { Component, Vue, Prop } from 'vue-property-decorator'
import ComTable from '@/components/comTable/index.vue'
import DrawerComponent from '@/components/comDrawer/index.vue'
import { Pagination, TableData } from '@/common/types'
import { ROLE_COLUMNS } from '@/common/constants/systemManage/userMange'
@Component({
    components: {
        MenuTab,
        ComTable,
        DrawerComponent
    }
})
export default class RoleManage extends Vue {
    @Prop({
        type: String,
        default: () => '白名单'
    })
    title: string
    visible: boolean = false
    loading: boolean = false
    isConfirm: boolean = false
    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    // 角色管理
    roleColumns: Array<TableData> = ROLE_COLUMNS
    searchValue: string = ''
    rawDataList: any = []
    dataList: any = []
    selectedData: any = {}
    allSelected: any = []
    rawSelected: any = []
    credentialsDetail: any = {}
    roleDetail: any = {}

    async showSlider(list, row?) {
        this.visible = true
        this.searchValue = ''
        this.roleDetail = row
        const originList = {
            role: [],
            group_role: []
        }
        this.selectedData = this.$deepClone((list || originList))
        // 保存原始role数据
        this.rawSelected = this.$deepClone(this.selectedData.role)
        this.handleAllSelected()
        this.getDataList()
    }

    handleAllSelected() {
        this.allSelected = this.selectedData.role
    }
    async getDataList() {
        const params = {
            page: this.pagination.current,
            page_size: this.pagination.limit,
            search: this.searchValue
        }
        this.loading = true
        try {
            const res = await this.$api.RoleManageMain.getRoleList(params)
            res.data.items = res.data.map(item => ({ id: item.id, name: item.name, description: item.description }))
            if (!res.result) {
                this.rawDataList = []
                this.pagination.count = 0
                return this.$error(res.message)
            }
            const selectMap = Object.fromEntries((this.selectedData.role || []).map(r => [r.id, r]))
            const isAdminGroup = this.roleDetail?.role_name === 'admin_group'
            this.rawDataList = (res.data?.items || []).map(item => ({
                ...item,
                role_type: selectMap[item.id]?.role_type || 'user',
                isChecked: isAdminGroup ? selectMap[item.id] : true
            }))
            const { current, limit } = this.pagination
            // 搜索的关键字
            this.dataList = this.rawDataList.filter(item => item.name?.includes(this.searchValue))
            this.pagination.count = this.dataList.length
            // 分页
            this.dataList = this.dataList.slice((current - 1) * limit, current * limit)
            this.$nextTick(() => {
                this.dataList.forEach(item => {
                    if (selectMap[item.id]) {
                        this.$refs.userTable?.toggleRowSelection(item, true)
                    }
                })
            })
        } finally {
            this.loading = false
        }
    }

    handleConfirm() {
        this.visible = false
        this.setRoles(this.rawSelected, this.allSelected)
    }
    async setRoles(rawData, updateData) {
        // 找出要删除的id和要增加的id
        const deleteId = []
        const rawTemp = rawData.map(item => item.id)
        const updateTemp = updateData.map(item => item.id)
        for (let i = 0; i < rawTemp.length; i++) {
            if (!updateTemp.includes(rawTemp[i])) {
                deleteId.push(rawTemp[i])
            }
        }
        const addId = []
        for (let i = 0; i < updateTemp.length; i++) {
            if (!rawTemp.includes(updateTemp[i])) {
                addId.push(updateTemp[i])
            }
        }
        let deletePromises = []
        let addPromises = []
        if (addId.length) {
            addPromises = addId.map(id => {
                return this.$api.UserManageMain.setUserRoles({ id: id, userId: this.roleDetail.id })
            })
        }
        if (deleteId.length) {
            deletePromises = deleteId.map(id => {
                return this.$api.RoleManageMain.deleteUserRole({ id: id, userId: this.roleDetail.id })
            })
        }

        this.isConfirm = true
        try {
            const res = await Promise.all([...addPromises, ...deletePromises])
            if (res.every(item => item.result)) {
                this.$success('设置成功')
                this.handleClose()
                this.$emit('confirm')
            }
        } finally {
            this.isConfirm = false
        }
    }
    handleClose() {
        this.visible = false
    }

    handleSelect(selection) {
        this.selectedData.role = selection
        this.handleAllSelected()
    }

    handleAllSelect(selection) {
        this.selectedData.role = selection
        this.handleAllSelected()
    }

    handlePageChange(page) {
        this.pagination.current = page
        const { limit } = this.pagination
        this.dataList = this.dataList.slice((page - 1) * limit, page * limit)
        this.toggleRowSelection()
    }

    handleLimitChange(size) {
        this.pagination.current = 1
        this.pagination.limit = size
        this.dataList = this.rawDataList.slice(0, size)
        this.toggleRowSelection()
    }

    toggleRowSelection() {
        this.$nextTick(() => {
            this.dataList.forEach(item => {
                if (this.allSelected.find(target => target.id === item.id)) {
                    this.$refs.userTable?.toggleRowSelection(item, true)
                }
            })
        })
    }

    handleSearch() {
        this.pagination.current = 1
        this.getDataList()
    }

    handleRemove(row) {
        const index = this.allSelected.findIndex(r => r.id === row.id && r.type === row.type)
        if (index !== -1) {
            this.allSelected.splice(index, 1)
        }
        this.$nextTick(() => {
            this.dataList.forEach(item => {
                if (item.id === row.id) {
                    this.$refs.userTable?.toggleRowSelection(item, false)
                }
            })
        })
        // 移除用户或角色后，更新map数据
        const selectedIndex = this.selectedData[row.type].findIndex(r => r.id === row.id)
        this.selectedData[row.type].splice(selectedIndex, 1)
    }

    handleClear() {
        this.selectedData.role = this.selectedData.role.filter(item => item.role_type === 'group')
        this.handleAllSelected()
        this.$nextTick(() => {
            this.dataList.forEach(item => {
                if (item.role_type !== 'group') {
                    this.$refs.userTable?.toggleRowSelection(item, false)
                }
            })
        })
    }
}
