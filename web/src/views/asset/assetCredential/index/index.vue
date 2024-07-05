<template>
    <div class="asset-credential page-container" v-loading="loading">
        <el-tabs class="asset-credential-tabs" v-model="currentModel" @tab-click="handleTabClick">
            <el-tab-pane
                v-for="(item,index) in modelList"
                :key="index"
                :label="item.model_name"
                :name="item.model_id">
            </el-tab-pane>
        </el-tabs>
        <div class="instance-list">
            <div class="operate-box">
                <div class="operate-box-left">
                    <el-dropdown size="small">
                        <el-button
                            size="small"
                            type="primary">
                            新建
                            <i class="el-icon-arrow-down el-icon--right"></i>
                        </el-button>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item
                                v-permission="operatePower"
                                @click.native="addResource('add')">
                                手动创建
                            </el-dropdown-item>
                        </el-dropdown-menu>
                    </el-dropdown>
                    <el-dropdown class="mr10 ml10" size="small">
                        <el-button size="small">
                            操作
                            <i class="el-icon-arrow-down el-icon--right"></i>
                        </el-button>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item
                                v-permission="operatePower"
                                :disabled="!selectedInstances.length"
                                @click.native="deleteInstance(selectedInstances)">
                                批量删除
                            </el-dropdown-item>
                            <el-dropdown-item
                                v-permission="operatePower"
                                :disabled="!selectedInstances.length"
                                @click.native="addResource('batchUpdate')">
                                批量更新
                            </el-dropdown-item>
                        </el-dropdown-menu>
                    </el-dropdown>
                </div>
                <div class="operate-box-right">
                    <selectInput
                        :property-list="atrrList"
                        :group-list="groupList"
                        :user-list="userList"
                        @change="changeFeild" />
                </div>
            </div>
            <com-table
                v-show="columns.length"
                v-loading="tableLoading"
                ref="comTable"
                :data="instanceList"
                :columns="columns"
                :pagination="pagination"
                height="calc(100vh - 230px)"
                :settings-fields="displayFields"
                @page-change="handlePageChange"
                @page-limit-change="handleLimitChange"
                @select="handleSelect"
                @select-all="handleSelect"
                @handle-setting-change="handleSettingChange"
            >
                <template slot="operation" slot-scope="{ row }">
                    <el-button
                        type="text"
                        size="small"
                        @click="checkDetail(row)">
                        详情
                    </el-button>
                    <el-button
                        type="text"
                        size="small"
                        :disabled="row._creator !== user"
                        @click="empower(row)">
                        授权
                    </el-button>
                    <el-button
                        v-permission="operatePower"
                        type="text"
                        size="small"
                        :disabled="row._creator !== user"
                        @click="addResource('edit',row)">
                        编辑
                    </el-button>
                    <el-button
                        type="text"
                        size="small"
                        @click="checkRelate(row)">
                        关联
                    </el-button>
                    <el-button
                        v-permission="operatePower"
                        type="text"
                        size="small"
                        :disabled="row._creator !== user"
                        @click="deleteInstance([row])">
                        删除
                    </el-button>
                </template>
                <template v-for="field in slotColumns" :slot="field.scopedSlots" slot-scope="{ row }">
                    <div :key="field.key">
                        <el-tag
                            v-if="field.attr_type === 'bool'"
                            :type="row[field.key] ? 'success' : ''">
                            {{getShowValue(field, row)}}
                        </el-tag>
                        <span v-else>{{ getShowValue(field, row) }}</span>
                    </div>
                </template>
            </com-table>
        </div>
        <add-instance
            ref="addInstance"
            :model-id="currentModel"
            :group-list="groupList"
            :user-list="userList"
            :current-node="currentNode"
            :connect-type-list="connectTypeList"
            :model-info-list="modelInfoList"
            @on-success="updateInstanceList" />
        <relation ref="relation"
            :group-list="groupList"
            :connect-type-list="connectTypeList"
            :model-info-list="modelInfoList"
            :user-list="userList"
            :property-list="propertyList"
            :inst-info="instInfo"
        />
        <auth-white-list
            title="凭据授权"
            :model-info="{
                model_id: currentModel
            }"
            ref="authWhiteList" />
        <drawer-component
            :title="`实例详情-${currentModelCfg.inst_name}`"
            :size="800"
            :visible="visible"
            destroy-on-close
            custom-class="common-dialog-wrapper"
            :before-close="beforeCloseDialog">
            <div slot="content" class="content-box common-dialog-wrapper-main">
                <base-info
                    :group-list="groupList"
                    :user-list="userList"
                    :current-model-cfg="currentModelCfg"
                    display-percent="50%"
                    :allow-edit="false"
                >
                </base-info>
            </div>
            <div slot="footer">
                <el-button
                    size="small"
                    @click="beforeCloseDialog">
                    关闭
                </el-button>
            </div>
        </drawer-component>
    </div>
</template>

<script lang="ts">
    import { Component, Vue } from 'vue-property-decorator'
    import ComTable from '@/components/comTable/index.vue'
    import { Pagination, TableData } from '@/common/types'
    import AddInstance from '@/views/asset/assetData/components/addInstance/index.vue'
    import SelectInput from '@/views/asset/assetData/components/selectInput/index.vue'
    import Relation from '@/views/asset/assetData/components/relation/index.vue'
    import { getAssetAttrValue } from '@/controller/func/common'
    import authWhiteList from '@/views/asset/assetCredential/components/authWhiteList/index.vue'
    import BaseInfo from '@/views/asset/assetData/components/baseInfo/index.vue'
    import DrawerComponent from '@/components/comDrawer/index.vue'

@Component({
    name: 'asset-data',
    components: {
        ComTable,
        AddInstance,
        SelectInput,
        Relation,
        authWhiteList,
        BaseInfo,
        DrawerComponent
    },
    beforeRouteLeave(to, from, next) {
        this.$handleKeepAlive(to, from)
        next()
    },
    activated() {
        this.getInstanceList()
    }
})
export default class AssetData extends Vue {
    loading: boolean = false
    modelList: Array<any> = []
    treeList: Array<any> = []
    propertyList: Array<any> = []
    instanceList: Array<any> = []
    columns: Array<TableData> = []
    currentModel: string = ''
    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    tableLoading: boolean = false
    selectedInstances: Array<any> = []
    search: string = ''
    groupList: Array<any> = []
    currentNode: any = {}
    condition: any = null
    userList: Array<any> = []
    displayFields: Array<any> = []
    selecteFieldsKeys: Array<string> = []
    modelInfoList: Array<any> = []
    connectTypeList: Array<any> = []
    instInfo: any = {}
    classifyId: string = 'AssetCredential'
    visible: boolean = false
    currentModelCfg: any = {}

    get atrrList() {
        return this.propertyList.filter(item => item.attr_type !== 'pwd').map(item => {
            if (item.attr_type === 'bool') {
                item.option = [
                    { name: '是', id: true },
                    { name: '否', id: false }
                ]
            }
            return item
        })
    }

    get slotColumns() {
        return this.columns.filter(item => item.scopedSlots && item.scopedSlots !== 'operation')
    }

    get operatePower() {
        return {
            id: this.classifyId,
            type: `${this.classifyId}_manage`
        }
    }
    get user() {
        return this.$store.state.permission.user.user_info?.preferred_username
    }

    created() {
        this.getConnectTypeList()
    }

    async mounted() {
        this.loading = true
        await this.getAllModelList()
        Promise.all([this.getGroups(), this.getUserList(), this.getModelAttrList(), this.getShowFields(), this.getInstanceList('init')]).finally(() => {
            this.updateTable()
            this.loading = false
        })
    }

    beforeCloseDialog() {
        this.visible = false
    }
    checkDetail(row) {
        this.currentModelCfg = {
            ...row,
            inst_id: row._id
        }
        this.visible = true
    }
    empower(row) {
        const authWhiteList: any = this.$refs.authWhiteList
        authWhiteList.showSlider([], row)
    }
    checkRelate(row) {
        this.instInfo = {
            instId: row._id,
            modelId: this.currentModel,
            classifyId: this.classifyId,
            model_type: 'credential'
        }
        const relation: any = this.$refs.relation
        relation.show(row)
    }
    async getUserList() {
        const { result, message, data } = await this.$api.UserManageMain.getAllUsers()
        if (!result) {
            return this.$error(message)
        }
        this.userList = data.map(item => {
            return {
                name: item.lastName,
                id: item.username
            }
        })
    }
    async getConnectTypeList() {
        const { result, data } = await this.$api.ModelManage.getAssotypeList()
        if (!result) {
            return false
        }
        this.connectTypeList = data.map(item => {
            return {
                id: item.asst_id,
                label: item.asst_name,
                name: `${item.asst_name}(${item.asst_id})`
            }
        })
    }
    updateTable() {
        this.$nextTick(() => {
            const resourceTable: any = this.$refs.comTable
            this.displayFields = this.selecteFieldsKeys.length ? this.getColumns(this.getDisplayFields(this.selecteFieldsKeys)) : this.$Copy(this.columns)
            if (resourceTable) {
                resourceTable.updateColumns(this.displayFields)
                resourceTable.updateFields(this.columns)
            }
        })
    }
    async handleSettingChange(list) {
        this.tableLoading = true
        try {
            const params = {
                model_id: this.currentModel,
                body: list.map(item => item.key)
            }
            const { result, message, data } = await this.$api.AssetData.setShowFields(params)
            if (!result) {
                return this.$error(message)
            }
            this.$success('设置成功！')
            this.selecteFieldsKeys = data.show_fields || []
            this.updateTable()
        } finally {
            this.tableLoading = false
        }
    }
    changeFeild(condition) {
        this.condition = condition
        this.getInstanceList()
    }
    addResource(mode, row = {}) {
        if (!this.$BtnPermission(this.operatePower)) {
            return false
        }
        const addInstance: any = this.$refs.addInstance
        addInstance.showDialog({
            mode,
            row,
            propertyList: this.propertyList,
            inst_ids: mode === 'add' ? [] : mode === 'batchUpdate' ? this.selectedInstances : [row]
        })
    }
    updateInstanceList() {
        this.pagination.current = 1
        this.getInstanceList()
    }
    getShowValue(field, tex) {
        return getAssetAttrValue(field, tex, {
            groupList: this.groupList,
            userList: this.userList
        })
    }
    handleSelect(selections) {
        this.selectedInstances = selections
    }
    selectGroup(node, row) {
        this.currentNode = { ...node, level: row.level }
        this.pagination.current = 1
        this.getInstanceList()
    }
    handleTabClick(tab, event) {
        this.pagination.current = 1
        this.loading = true
        Promise.all([this.getModelAttrList(), this.getInstanceList('init'), this.getShowFields()]).finally(() => {
            this.updateTable()
            this.loading = false
        })
    }
    async getAllModelList() {
        const res = await this.$api.ModelManage.getModel()
        const { result, message, data } = res
        if (!result) {
            this.modelList = []
            return this.$error(message)
        }
        this.modelInfoList = data
        this.modelList = data.filter(item => item.model_type === 'credential')
        this.currentModel = this.$route.query.modelId || this.modelList[0]?.model_id || ''
    }
    async getShowFields() {
        const res = await this.$api.AssetData.getShowFields({
            model_id: this.currentModel
        })
        const { result, message, data } = res
        if (!result) {
            return this.$error(message)
        }
        this.selecteFieldsKeys = data?.show_fields || []
    }
    // 根据展示字段的key返回columns
    getDisplayFields(keys) {
        const fields = []
        keys.forEach(key => {
            const target = this.columns.find(item => item.key === key)
            target && fields.push(target)
        })
        return fields
    }
    async getGroups() {
        const res = await this.$api.GroupManage.getGroups()
        const { result, message, data } = res
        if (!result) {
            return this.$error(message)
        }
        this.treeList = data
        this.currentNode = {
            ...data[0],
            level: 1
        }
        this.groupList = this.convertArray(data)
    }
    convertArray(arr) {
        const result = []
        arr.forEach(item => {
            const newItem = {
                value: item.id,
                label: item.name
            }
            if (item.subGroups && !!item.subGroups.length) {
                newItem.children = this.convertArray(item.subGroups)
            }
            result.push(newItem)
        })
        return result
    }
    async getModelAttrList() {
        const params = {
            id: this.currentModel
        }
        const { result, message, data } = await this.$api.ModelManage.getModelAttrList(params)
        if (!result) {
            return this.$error(message)
        }
        this.propertyList = data
        const propertyList = this.$copy(this.propertyList)
        propertyList.forEach(item => {
            item.key = item.attr_id
            item.label = item.attr_name
            item.minWidth = '100px'
            item.align = 'left'
            item.scopedSlots = item.attr_id
        })
        this.columns = this.getColumns(propertyList)
    }
    getColumns(list) {
        const operateColumn = {
            label: '操作',
            key: 'operation',
            align: 'left',
            width: '210px',
            fixed: 'right',
            scopedSlots: 'operation'
        }
        return [
            {
                type: 'selection',
                fixed: true
            },
            ...list,
            operateColumn
        ]
    }
    async getInstanceList(type?) {
        this.tableLoading = type !== 'init'
        try {
            const params = this.getParams()
            const { result, message, data } = await this.$api.AssetData.getInstanceList(params)
            if (!result) {
                return this.$error(message)
            }
            this.instanceList = data.insts
            this.pagination.count = data.count
        } finally {
            this.tableLoading = false
        }
    }
    getParams() {
        const params = {
            query_list: [],
            page: this.pagination.current,
            page_size: this.pagination.limit,
            order: '',
            model_id: this.currentModel
        }
        const { id, level } = this.currentNode
        const groupCondition = {
            field: 'organization',
            type: 'str=',
            value: id
        }
        if (this.condition) {
            if (level !== 1) {
                params.query_list = [
                    groupCondition,
                    this.condition
                ]
            } else {
                params.query_list = [this.condition]
            }
        } else if (id && level !== 1) {
            params.query_list = [
                groupCondition
            ]
        }
        return params
    }
    // 批量删除
    deleteInstance(list) {
        if (!this.$BtnPermission(this.operatePower)) {
            return false
        }
        this.$confirm('确认要删除该资产？', '提示', {
            center: true
        }).then(() => {
            this.deleteInstanceRequest(list)
        })
    }
    async deleteInstanceRequest(list) {
        this.tableLoading = true
        const params = {
            body: list.map(item => item._id)
        }
        const { result, message } = await this.$api.AssetData.deleteInstance(params)
        if (!result) {
            this.tableLoading = false
            return this.$error(message)
        }
        this.$success('删除成功！')
        this.getInstanceList()
    }
    handlePageChange(page) {
        this.pagination.current = page
        this.getInstanceList()
    }

    handleLimitChange(size) {
        this.pagination.current = 1
        this.pagination.limit = size
        this.getInstanceList()
    }
}
</script>

<style lang="scss" scoped>
.asset-credential {
    height: 100%;
    .asset-credential-tabs {
        min-height: 54px;
        margin-top: -14px;
    }
    .instance-list {
        width: 100%;
        background: #fff;
    }
}
</style>
