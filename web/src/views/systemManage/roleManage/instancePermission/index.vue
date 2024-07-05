<template>
    <div class="instance-permission">
        <div class="header mt10">
            <el-button size="small" :type="'primary'" @click="addInstPermission('add')">
                新增权限
            </el-button>
        </div>
        <com-table
            v-loading="tableLoading"
            class="mt20 table-container"
            ref="instTable"
            :data="dataList"
            height="calc(100vh - 324px)"
            :pagination="pagination"
            :columns="userColumns"
            @page-change="handlePageChange"
            @page-limit-change="handleLimitChange">
            <template slot="model_id" slot-scope="{ row }">
                {{ getModelName(row) }}
            </template>
            <template slot="permission_type" slot-scope="{ row }">
                {{ row.permission_type === 'manage' ? '查询，管理' : '查询' }}
            </template>
            <template slot="resource_type" slot-scope="{ row }">
                {{ row.resource_type === 'fixed' ? '指定资产' : '条件筛选' }}
            </template>
            <template slot="operation" slot-scope="{ row }">
                <el-button
                    type="text"
                    size="small"
                    @click="addInstPermission('edit',row)">
                    编辑
                </el-button>
                <el-button
                    type="text"
                    size="small"
                    @click="handleDelete(row)">
                    删除
                </el-button>
            </template>
        </com-table>
        <add-resource-auth
            ref="addResourceAuth"
            :role="role"
            :model-list="modelList"
            @updateList="getInstList" />
    </div>
</template>
<script lang="ts">
    import { Component, Vue, Prop } from 'vue-property-decorator'
    import { Pagination, TableData } from '@/common/types'
    import ComTable from '@/components/comTable/index.vue'
    import AddResourceAuth from '../components/addResourceAuth'
    import { ASSET_AUTH_COLUMNS } from '@/common/constants/systemManage/roleManage'

@Component({
    components: {
        ComTable,
        AddResourceAuth
    }
})
export default class userAndGroup extends Vue {
    @Prop({
        type: Object,
        default: () => ({})
    })
    role: any

    tableLoading: boolean = false
    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    userColumns: Array<TableData> = ASSET_AUTH_COLUMNS
    dataList: any = [] // 表格展示数据
    search: string = ''
    modelList: Array<any> = [] // 所有模型列表

    created() {
        this.tableLoading = true
        Promise.all([this.handleSearch(), this.getAllModelList()]).finally(() => {
            this.tableLoading = false
        })
    }

    getInstList() {
        this.pagination.current = 1
        this.getInstPermissionList()
    }
    getModelName(row) {
        return this.modelList.find(item => item.model_id === row.model_id)?.model_name || '--'
    }
    handleDelete(row) {
        this.$confirm('确认要删除此实例权限？', '提示', {
            center: true
        }).then(() => {
            this.deleteInstPermission(row)
        })
    }
    async deleteInstPermission({id}) {
        this.tableLoading = true
        const params = {
            id
        }
        const res = await this.$api.InstancePermission.deleteInstPermissionList(params)
        const { result, message } = res
        if (!result) {
            this.tableLoading = false
            return this.$error(message)
        }
        this.getInstList()
    }
    addInstPermission(type, row = {}) {
        const addResourceAuth: any = this.$refs.addResourceAuth
        addResourceAuth.show({
            type,
            row
        })
    }
    handlePageChange(page) {
        this.pagination.current = page
        this.getInstPermissionList()
    }
    handleLimitChange(size) {
        this.pagination.current = 1
        this.pagination.limit = size
        this.getInstPermissionList()
    }
    handleSearch() {
        this.pagination.current = 1
        this.getInstPermissionList('init')
    }
    async getInstPermissionList(type?) {
        this.tableLoading = true
        try {
            const params = this.getParams()
            const res = await this.$api.InstancePermission.getInstPermissionList(params)
            const { result, message, data } = res
            if (!result) {
                this.dataList = []
                return this.$error(message)
            }
            this.dataList = data.data
            this.pagination.count = data.count
        } finally {
            this.tableLoading = type === 'init'
        }
    }
    async getAllModelList() {
        const res = await this.$api.ModelManage.getModel()
        const { result, message, data } = res
        if (!result) {
            this.modelList = []
            return this.$error(message)
        }
        this.modelList = data
    }
    getParams() {
        const params = {
            role_id: this.role.name,
            page: this.pagination.current,
            page_size: this.pagination.limit,
            permission_type: '',
            model_id: ''
        }
        return params
    }
}
</script>
<style lang="scss" scoped>
.instance-permission {
    height: 100%;
    padding: 10px 10px 0 10px;
}
</style>
