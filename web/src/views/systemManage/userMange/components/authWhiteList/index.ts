import MenuTab from '@/components/menuTab/index.vue'
import { Component, Vue, Prop } from 'vue-property-decorator'
import { Pagination, TableData, Panels } from '@/common/types'
import ComTable from '@/components/comTable/index.vue'
import DrawerComponent from '@/components/comDrawer/index.vue'
import { GROUP_COLUMNS, AUTH_PANELS } from '@/common/constants/systemManage/userMange'

@Component({
    components: {
        MenuTab,
        ComTable,
        DrawerComponent
    }
})
export default class AuthWhiteList extends Vue {
    @Prop({
        type: Boolean,
        default: () => false
    })
    isMyCredentials: boolean
    @Prop({
        type: String,
        default: () => '白名单'
    })
    title: string
    // 只进行人员选择
    @Prop({
        type: Boolean,
        default: () => false
    })
    onlyChooseUser: boolean
    // 哪里调用，角色管理或者组织管理，调用的接口不一样
    @Prop({
        type: String,
        default: () => 'roleManage'
    })
    caller: string
    visible: boolean = false
    loading: boolean = false
    isConfirm: boolean = false
    panels: Array<Panels> = AUTH_PANELS
    active: string = 'role'
    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    groupColumns: Array<TableData> = GROUP_COLUMNS
    userColumns: Array<TableData> = [
        {
            type: 'selection',
            selectable: (row) => {
                if (this.onlyChooseUser && row.bk_username === 'admin') {
                    return !row.isChecked
                }
                return true
            }
        },
        {
            label: '中文名',
            key: 'chname'
        },
        {
            label: '用户名',
            key: 'bk_username'
        }
    ]
    searchValue: string = ''
    dataList: any = []
    selectedData: any = {}
    allSelected: any = []
    rawSelected: any = []
    credentialsDetail: any = {}
    roleDetail: any = {}
    get initChooseAdmin() {
        return !this.isMyCredentials && !this.onlyChooseUser
    }
    get isGroup() {
        return this.active === 'role'
    }

    async showSlider(list, row?) {
        this.visible = true
        this.searchValue = ''
        if (this.onlyChooseUser) {
            this.roleDetail = row
        }
        const originList = {
            role: [],
            user: []
        }
        if (this.isMyCredentials) {
            this.credentialsDetail = row
            const { result, data } = await this.$api.RemoteConnectMain.getCredDetail({ id: row.id })
            if (result) {
                originList.role = data.role
                originList.user = data.user
            }
        }
        this.selectedData = this.$deepClone(this.isMyCredentials ? originList : (list || originList))
        // 保存user原始数据
        this.rawSelected = this.$deepClone(this.selectedData.user)
        this.handleAllSelected()
        this.changeMenu(this.onlyChooseUser ? 'user' : 'role')
    }

    handleAllSelected() {
        this.allSelected = []
        Object.keys(this.selectedData).forEach(key => {
            this.allSelected = this.allSelected.concat(this.selectedData[key].map(r => ({ ...r, type: key })))
        })
        if (this.initChooseAdmin) {
            this.allSelected = this.allSelected.filter(item => item?.bk_username !== 'admin')
        }
    }

    changeMenu(active) {
        this.active = active
        this.pagination.current = 1
        this.$refs.userTable?.updateColumns(this.isGroup ? this.groupColumns : this.userColumns)
        this.getDataList()
    }

    async getDataList() {
        const params = {
            page: this.pagination.current,
            page_size: this.pagination.limit,
            search: this.searchValue
        }
        this.loading = true
        try {
            const res = await this.$api.UserManageMain[this.isGroup ? 'searchRoleList' : 'getUserList'](params)
            if (!res.result) {
                this.dataList = []
                this.pagination.count = 0
                return this.$error(res.message)
            }
            res.data.items = res.data.users.map(item => ({ id: item.id, bk_username: item.username, chname: item.lastName }))
            const selectMap = Object.fromEntries((this.selectedData[this.active] || []).map(r => [r.id, r]))
            const isAdminGroup = this.roleDetail?.role_name === 'admin_group'
            this.dataList = (res.data?.items || []).map(item => ({
                ...item,
                isChecked: isAdminGroup ? selectMap[item.id] : true
            }))
            this.pagination.count = res.data.count
            this.$nextTick(() => {
                this.dataList.forEach(item => {
                    if (selectMap[item.id] || (this.initChooseAdmin && item?.bk_username === 'admin')) {
                        this.$refs.userTable?.toggleRowSelection(item, true)
                    }
                })
            })
        } finally {
            this.loading = false
        }
    }

    handleConfirm() {
        if (this.isMyCredentials) {
            this.imPower()
        } else if (this.onlyChooseUser) {
            this.setUsersByRole(this.rawSelected, this.allSelected)
        } else {
            this.visible = false
            this.$emit('confirm', this.selectedData)
        }
    }
    async setUsersByRole(rawData, updateData) {
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
        // 如果是角色管理页面调用
        let deletePromises = []
        let addPromises = []
        if (this.caller === 'roleManage') {
            deletePromises = deleteId.map(id => {
                return this.$api.RoleManageMain.deleteUserRole({ id: this.roleDetail.id, userId: id })
            })
            addPromises = addId.map(id => {
                return this.$api.UserManageMain.setUserRoles({ id: this.roleDetail.id, userId: id })
            })
        } else if (this.caller === 'groupManage') { // 组织管理调用
            addId.length > 0 && addPromises.push(this.$api.GroupManage.addGroupUsers({ id: this.roleDetail.id, addIds: addId }))
            deleteId.length > 0 && deletePromises.push(this.$api.GroupManage.delGroupUsers({ id: this.roleDetail.id, deleteIds: deleteId }))
        }
        this.isConfirm = true
        try {
            // const res = await this.$api.UserManageMain.setUsersByRole({
            //     users: this.selectedData.user.map(item => item.id),
            //     id: this.roleDetail?.id
            // })
            // const { result, message } = res
            // if (!result) {
            //     this.$error(message)
            //     return false
            // }
            // this.$success('设置人员成功')
            // this.handleClose()
            // this.$emit('confirm')
            // const { result, message } = res
            // if (!result) {
            //     this.$error(message)
            //     return false
            // }
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
    imPower() {
        this.isConfirm = true
        this.$api.RemoteConnectMain.setCredAuthList({
            id: this.credentialsDetail.id,
            body: {
                user_list: this.selectedData.user.map(item => item.bk_username),
                role_list: this.selectedData.role.map(item => item.id)
            }
        }).then(res => {
            const { result, message } = res
            if (!result) {
                this.$error(message)
                return false
            }
            this.$success('授权成功')
            this.handleClose()
        }).finally(() => {
            this.isConfirm = false
        })
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
        this.getDataList()
    }

    handleLimitChange(size) {
        this.pagination.current = 1
        this.pagination.limit = size
        this.getDataList()
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
                const isAdmin = this.initChooseAdmin && item?.bk_username === 'admin'
                this.$refs.userTable?.toggleRowSelection(item, isAdmin)
            })
        })
    }
}
