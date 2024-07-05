import MenuTab from '@/components/menuTab/index.vue'
import { Component, Vue, Prop } from 'vue-property-decorator'
import { Pagination, TableData } from '@/common/types'
import ComTable from '@/components/comTable/index.vue'
import DrawerComponent from '@/components/comDrawer/index.vue'
import { ROLES_COLUMNS } from '@/common/constants/systemManage/groupManage'

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
    active: string = 'role'
    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    // 角色管理
    roleColumns: Array<TableData> = ROLES_COLUMNS
    searchValue: string = ''
    rawDataList: any = []
    dataList: any = []
    selectedData: any = {}
    allSelected: any = []
    rawSelected: any = []
    credentialsDetail: any = {}
    roleDetail: any = {}
    get isGroup() {
        return this.active === 'role'
    }

    async showSlider(list, row?) {
        this.visible = true
        this.searchValue = ''
        this.roleDetail = row
        const originList = {
            role: [],
            user: []
        }
        this.selectedData = this.$deepClone((list || originList))
        // 保存原始role数据
        this.rawSelected = this.$deepClone(this.selectedData.role)
        this.handleAllSelected()
        this.getDataList()
    }

    handleAllSelected() {
        this.allSelected = []
        Object.keys(this.selectedData).forEach(key => {
            this.allSelected = this.allSelected.concat(this.selectedData[key].map(r => ({ ...r, type: key })))
        })
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
            const selectMap = Object.fromEntries((this.selectedData[this.active] || []).map(r => [r.id, r]))
            const isAdminGroup = this.roleDetail?.role_name === 'admin_group'
            this.rawDataList = (res.data?.items || []).map(item => ({
                ...item,
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
        this.setRolesByGroup(this.rawSelected, this.allSelected)
        // this.$emit('confirm', this.selectedData)
    }
    async setRolesByGroup(rawData, updateData) {
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
        const deletePromises = []
        const addPromises = []
        addId.length > 0 && addPromises.push(this.$api.GroupManage.addGroupRoles({ id: this.roleDetail.id, addIds: addId }))
        deleteId.length > 0 && deletePromises.push(this.$api.GroupManage.delGroupRoles({ id: this.roleDetail.id, deleteIds: deleteId }))

        this.isConfirm = true
        try {
            const res = await Promise.all([...addPromises, ...deletePromises])
            if (res.every(item => item.result)) {
                this.$success('设置人员成功')
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

    handleSelect(selection, row) {
        const current = selection.find(select => select.id === row.id)
        if (current) {
            this.selectedData[this.active].push(row)
        } else {
            const index = this.selectedData[this.active].findIndex(r => r.id === row.id)
            this.selectedData[this.active].splice(index, 1)
        }
        this.handleAllSelected()
    }

    handleAllSelect(selection) {
        const isSelected = !!selection.length
        this.dataList.forEach(item => {
            if (isSelected) {
                const current = this.selectedData[this.active].find(r => r.id === item.id)
                !current && this.selectedData[this.active].push(item)
            } else {
                const index = this.selectedData[this.active].findIndex(r => r.id === item.id)
                this.selectedData[this.active].splice(index, 1)
            }
        })
        this.handleAllSelected()
    }

    handlePageChange(page) {
        this.pagination.current = page
        const { limit } = this.pagination
        this.dataList = this.dataList.slice((page - 1) * limit, page * limit)
    }

    handleLimitChange(size) {
        this.pagination.current = 1
        this.pagination.limit = size
        this.dataList = this.rawDataList.slice(0, size)
    }

    handleSearch() {
        this.pagination.current = 1
        this.getDataList()
    }

    handleRemove(row) {
        const index = this.allSelected.findIndex(r => r.id === row.id && r.type === row.type)
        if (index || index === 0) {
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
        this.selectedData = {
            role: [],
            user: []
        }
        this.handleAllSelected()
        this.$nextTick(() => {
            this.dataList.forEach(item => {
                this.$refs.userTable?.toggleRowSelection(item, false)
            })
        })
    }
}
