<template>
    <drawer-component
        :title="title"
        :size="800"
        :visible="visible"
        destroy-on-close
        custom-class="common-dialog-wrapper"
        :before-close="handleClose">
        <div slot="content" class="common-dialog-wrapper-main">
            <div class="auth-white-list">
                <div class="list-container">
                    <div class="header">
                        <menu-tab
                            :panels="panels"
                            v-model="active"
                            type="capsule"
                            @change="changeMenu">
                        </menu-tab>
                        <el-input
                            clearable
                            size="small"
                            style="width: 300px;"
                            :placeholder="'请输入关键字搜索'"
                            suffix-icon="el-icon-search"
                            v-model="searchValue"
                            @change="handleSearch">
                        </el-input>
                    </div>
                    <com-table
                        class="mt20 table-container"
                        ref="userTable"
                        :data="dataList"
                        :pagination="pagination"
                        v-loading="loading"
                        :columns="groupColumns"
                        height="calc(100vh - 248px)"
                        @select="handleSelect"
                        @select-all="handleAllSelect"
                        @page-change="handlePageChange"
                        @page-limit-change="handleLimitChange">
                    </com-table>
                </div>
                <div class="selection-container">
                    <p>已选择（共<span>{{allSelected.length}}</span>条）<span class="clear" @click="handleClear">清空</span></p>
                    <ul>
                        <li v-for="item in allSelected" :key="item.id + item.type">
                            {{ item.type === 'role' ? item.name : `${item.lastName}(${item.username})` }}
                            <span>{{ item.type === 'role' ? '角色' : '用户' }}</span>
                            <i class="el-icon-close" @click="handleRemove(item)"></i>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <template slot="footer">
            <el-button
                class="mr10"
                size="small"
                :type="'primary'"
                :loading="isConfirm"
                @click="handleConfirm()">
                确认
            </el-button>
            <el-button
                :type="'default'"
                size="small"
                :disabled="isConfirm"
                @click="handleClose()">
                取消
            </el-button>
        </template>
    </drawer-component>
</template>

<script lang="ts">
    import MenuTab from '@/components/menuTab/index.vue'
    import ComTable from '@/components/comTable/index.vue'
    import DrawerComponent from '@/components/comDrawer/index.vue'
    import { Component, Vue, Prop } from 'vue-property-decorator'
    import { Pagination, TableData } from '@/common/types'
    @Component({
        components: {
            MenuTab,
            ComTable,
            DrawerComponent
        }
    })
    export default class AuthWhiteList extends Vue {
        @Prop({
            type: String,
            default: () => '白名单'
        })
        title: string
        @Prop({
            type: Object,
            default: () => ({})
        })
        modelInfo: any

        visible: boolean = false
        loading: boolean = false
        isConfirm: boolean = false
        panels: Array<{
            label: string,
            name: string
        }> = [
                {
                    label: '角色',
                    name: 'role'
                },
                {
                    label: '用户',
                    name: 'user'
                }
            ]
        active: string = 'role'
        pagination: Pagination = {
            current: 1,
            count: 0,
            limit: 20,
            small: true
        }
        groupColumns: Array<TableData> = [
            {
                type: 'selection'
            },
            {
                label: '角色名称',
                key: 'name'
            },
            {
                label: '角色描述',
                key: 'description'
            }
        ]
        userColumns: Array<TableData> = [
            {
                type: 'selection',
                selectable: (row) => {
                    return true
                }
            },
            {
                label: '中文名',
                key: 'lastName'
            },
            {
                label: '用户名',
                key: 'username'
            }
        ]
        searchValue: string = ''
        dataList: any = []
        selectedData: any = {}
        allSelected: any = []
        credentialsDetail: any = {}
        rolesList: any = []
        usersList: any = []
        allDataList: any = []
        authorizationInfo: any = {}
        get isGroup() {
            return this.active === 'role'
        }

        async showSlider(list, row?) {
            this.visible = true
            this.searchValue = ''
            this.credentialsDetail = row
            this.init(row)
        }

        handleAllSelected() {
            this.allSelected = []
            Object.keys(this.selectedData).forEach(key => {
                this.allSelected = this.allSelected.concat(this.selectedData[key].map(r => ({ ...r, type: key })))
            })
        }

        changeMenu(active) {
            this.active = active === 'init' ? 'role' : active
            this.pagination.current = 1
            this.pagination.limit = 20
            this.$refs.userTable?.updateColumns(this.isGroup ? this.groupColumns : this.userColumns)
            if (active === 'init') {
                this.dataList = this.rolesList
                this.pagination.count = this.rolesList.length
                this.switchSelect()
                return
            }
            this.getDataList()
        }

        init(row) {
            this.loading = true
            Promise.all([this.getRoleList(), this.getUserList(), this.getAuthorizationList(row)]).finally(() => {
                const originList = {
                    roles: this.authorizationInfo.roles || [],
                    users: this.authorizationInfo.users || [],
                    role: [],
                    user: []
                }
                originList.roles.forEach(name => {
                    const role = this.rolesList.find(role => role.name === name)
                    if (role) {
                        originList.role.push(role)
                    }
                })
                originList.users.forEach(name => {
                    const user = this.usersList.find(user => user.username === name)
                    if (user) {
                        originList.user.push(user)
                    }
                })
                const { role, user } = originList
                this.selectedData = {
                    role,
                    user
                }
                this.handleAllSelected()
                this.changeMenu('init')
                this.loading = false
            })
        }
        async getRoleList() {
            const params = this.getParams()
            const res = await this.$api.RoleManageMain.getRoleList(params)
            const { result, message, data } = res
            if (!result) {
                this.rolesList = []
                return this.$error(message)
            }
            this.rolesList = data || []
        }
        async getUserList() {
            const params = this.getParams()
            const res = await this.$api.UserManageMain.getUserList(params)
            const { result, message, data } = res
            if (!result) {
                this.usersList = []
                return this.$error(message)
            }
            this.usersList = data.users || []
        }
        async getAuthorizationList(row) {
            const params = { inst_id: row._id, model_id: this.modelInfo.model_id }
            const { result, data, message } = await this.$api.AssetData.getAuthorizationList(params)
            if (!result) {
                return this.$error(message)
            }
            this.authorizationInfo = data
        }
        getParams() {
            return {
                page: this.pagination.current,
                page_size: this.pagination.limit,
                search: this.searchValue
            }
        }

        async getDataList() {
            const params = this.getParams()
            this.loading = true
            try {
                const res = this.isGroup
                    ? await this.$api.RoleManageMain.getRoleList(params)
                    : await this.$api.UserManageMain.getUserList(params)
                if (!res.result) {
                    this.dataList = []
                    this.pagination.count = 0
                    return this.$error(res.message)
                }
                const data = (this.isGroup ? res.data : res.data.users) || []
                this.dataList = data
                this.allDataList = this.$copy(this.dataList)
                this.pagination.count = res.data.count || res.data.length
                this.switchSelect()
            } finally {
                this.loading = false
            }
        }

        handleConfirm() {
            this.imPower()
        }

        imPower() {
            this.isConfirm = true
            const params = this.getCredParams()
            this.$api.AssetData.credentialAuthorization(params).then(res => {
                const { result, message } = res
                if (!result) {
                    return this.$error(message)
                }
                this.$success('授权成功')
                this.handleClose()
            }).finally(() => {
                this.isConfirm = false
            })
        }

        getCredParams() {
            const params = {
                model_id: this.modelInfo.model_id,
                inst_id: this.credentialsDetail._id,
                roles: this.selectedData.role.map(item => item.name),
                users: this.selectedData.user.map(item => item.username)
            }
            return params
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

        handlePageChange(val) {
            this.pagination.current = val
            if (this.isGroup) {
                const { limit } = this.pagination
                this.dataList = this.allDataList.filter(item => item.name.includes(this.searchValue)).slice((val - 1) * limit, val * limit)
                this.switchSelect()
                return
            }
            this.getDataList()
        }

        handleLimitChange(val) {
            this.pagination.current = 1
            this.pagination.limit = val
            if (this.isGroup) {
                this.dataList = this.allDataList.filter(item => item.name.includes(this.searchValue)).slice(0, val)
                this.switchSelect()
                return
            }
            this.getDataList()
        }

        handleSearch() {
            if (this.isGroup) {
                this.dataList = this.allDataList.filter(item => item.name.includes(this.searchValue))
                this.pagination.count = this.dataList.length
                this.switchSelect()
                return
            }
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

        switchSelect() {
            const selectMap = Object.fromEntries((this.selectedData[this.active] || []).map(r => [r.id, r]))
            this.$nextTick(() => {
                this.dataList.forEach(item => {
                    if (selectMap[item.id]) {
                        this.$refs.userTable?.toggleRowSelection(item, true)
                    }
                })
            })
        }
    }
</script>

<style scoped lang="scss">
.auth-white-list {
    height: 100%;
    display: flex;

    .list-container {
        width: 60%;

        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
    }

    .selection-container {
        border: 1px solid #D1D7E1;
        border-bottom: none;
        background-color: #F6F8F9;
        padding: 12px 24px;
        height: 100%;
        flex: 1;
        margin-left: 10px;
        overflow-y: scroll;

        >p {
            justify-content: space-between;
            font-size: 12px;
            margin: 0 0 10px 0;
            color: #63656e;

            span {
                display: inline-block;
                color: #3A84FF;
            }

            .clear {
                float: right;
                cursor: pointer;
            }
        }

        ul {
            margin-top: 15px;

            li {
                background: #FFFFFF;
                padding: 10px;
                position: relative;
                border-bottom: 1px solid #D1D7E1;

                &:last-child {
                    border: none;
                }

                span {
                    float: right;
                    font-size: 12px;
                    color: #7588A3;
                    padding-right: 10px;
                }

                >i {
                    display: none;
                    position: absolute;
                    right: 5px;
                    top: 12px;
                    font-size: 12px;
                }

                &:hover {
                    cursor: pointer;

                    i {
                        display: inline-block;

                        &:hover {
                            color: #3A84FF;
                        }
                    }
                }
            }
        }
    }
}
</style>
