<template>
    <drawer-component
        title="资产选择"
        :visible="visible"
        :size="800"
        destroy-on-close
        append-to-body
        :before-close="beforeCloseDialog">
        <div slot="content" class="common-dialog-wrapper-main" v-loading="pageLoading">
            <div class="search-bar">
                <el-select
                    class="model-list"
                    v-model="modelId"
                    placeholder="请选择资产模型"
                    size="small"
                    @change="handleModelChange">
                    <el-option
                        v-for="item in modelList"
                        :key="item.model_id"
                        :label="item.model_name"
                        :value="item.model_id">
                    </el-option>
                </el-select>
                <selectInput
                    class="mb20"
                    :key="selectInputKey"
                    :property-list="attrList"
                    :group-list="groupList"
                    :user-list="userList"
                    @change="changeFeild" />
            </div>
            <div class="choose-inst-container">
                <div class="container-content">
                    <com-table
                        v-show="instanceColumns.length"
                        v-loading="tableLoading"
                        ref="comTable"
                        :data="tableData"
                        :columns="instanceColumns"
                        :height="tableHeight"
                        :pagination="pagination"
                        @select-all="selectAllTableData"
                        @select="selectTableData"
                        @page-change="handlePageChange"
                        @page-limit-change="limitChange"
                        @filter-change="sourceFilterMethod"
                    >
                        <template v-for="field in instanceColumns" :slot="field.scopedSlots" slot-scope="{ row }">
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
                <div class="container-result">
                    <div class="header-title">
                        <span class="txt">已选择</span>
                        <span class="number">(共<label>{{ selectList.length }}</label>条)</span>
                        <div class="clear-button" @click="clearSelect">清空</div>
                    </div>
                    <div class="result-list">
                        <div
                            class="result-item"
                            v-for="(item, index) in selectList"
                            :key="item.id">
                            <div class="result-item-txt hide-text">
                                <span class="main">{{ item.inst_name }}</span>
                            </div>
                            <i class="cw-icon weops-close" @click="removeSelect(item, index)"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <template slot="footer">
            <el-button
                type="primary"
                size="small"
                @click="confirm">
                确定
            </el-button>
            <el-button
                type="default"
                size="small"
                @click="beforeCloseDialog">
                取消
            </el-button>
        </template>
    </drawer-component>
</template>

<script lang="ts">
    import {Vue, Component, Prop} from 'vue-property-decorator'
    import ComTable from '@/components/comTable/index.vue'
    import DrawerComponent from '@/components/comDrawer/index.vue'
    import { getAssetAttrValue } from '@/controller/func/common'
    import SelectInput from '@/views/asset/assetData/components/selectInput/index.vue'
    @Component({
        components: {
            ComTable,
            DrawerComponent,
            SelectInput
        }
    })
    export default class addInstance extends Vue {
        @Prop({
            type: Object,
            default: () => ({})
        })
        role: any
        groupList: any[] = []
        userList: any[] = []
        propertyList: any[] = []
        instanceColumns: any[] = []
        modelId: string = ''
        visible: boolean = false
        tableData: any[] = []
        tableLoading: boolean = false
        pageLoading: boolean = false
        pagination = {
            current: 1,
            count: 0,
            limit: 20
        }
        selectList: any[] = []
        modelList: any[] = []
        condition: any = null
        selectInputKey: number = 0

        get tableHeight() {
            return 'calc(100vh - 250px)'
        }
        get attrList() {
            return this.propertyList.map(item => {
                if (item.attr_type === 'bool') {
                    item.option = [
                        { name: '是', id: true },
                        { name: '否', id: false }
                    ]
                }
                return item
            })
        }
        created() {
            this.getGroups()
            this.getUserList()
        }
        sourceFilterMethod(val) {
            console.log(val)
        }
        async handleModelChange() {
            this.pageLoading = true
            this.selectInputKey = +new Date()
            this.condition = null
            this.getModelAttrList()
        }
        changeFeild(condition) {
            this.condition = condition
            this.pagination.current = 1
            this.getList()
        }
        getShowValue(field, tex) {
            return getAssetAttrValue(field, tex, {
                groupList: this.groupList,
                userList: this.userList
            })
        }
        beforeCloseDialog() {
            this.visible = false
        }
        handleSearch(data) {
            this.getList()
        }
        handleChange(data) {
            this.getList()
        }
        show(data) {
            this.visible = true
            const { selection, modelList } = data
            this.selectList = this.$Copy(selection)
            this.modelList = modelList
            this.modelId = modelList[0]?.model_id || ''
            if (this.modelId) {
                this.handleModelChange()
            }
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
        async getGroups() {
            const res = await this.$api.GroupManage.getGroups()
            const { result, message, data } = res
            if (!result) {
                return this.$error(message)
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
                id: this.modelId
            }
            const { result, message, data } = await this.$api.ModelManage.getModelAttrList(params)
            if (!result) {
                this.pageLoading = false
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
            this.instanceColumns = [
                {
                    type: 'selection',
                    fixed: true
                },
                ...propertyList
            ]
            this.updateColumns()
            this.getList()
        }
        filterList() {
            this.pagination.current = 1
            this.getList()
        }
        confirm() {
            if (!this.selectList.length) {
                this.$warn('资产列表不能为空！')
                return
            }
            const selectList = this.selectList.map(item => ({
                model_id: item.model_id,
                node_id: item._id,
                node_name: item.inst_name || '',
                node_ip: item.ip_addr || ''
            }))
            this.$emit('createNode', selectList)
            this.beforeCloseDialog()
        }
        updateColumns() {
            this.$nextTick(() => {
                const comTable: any = this.$refs.comTable
                comTable.updateColumns(this.instanceColumns)
            })
        }
        selectTableData(selection, row) {
            if (!this.selectList.map(item => item._id).includes(row._id)) {
                this.selectList.push(row)
            } else {
                this.selectList.splice(this.selectList.findIndex(item => item._id === row._id), 1)
            }
        }
        selectAllTableData(selection) {
            if (selection.length === 0) {
                this.selectList = this.selectList.filter(item => !this.tableData.some(tex => item._id === tex._id))
            } else {
                selection.forEach(item => {
                    if (!this.selectList.map(item => item._id).includes(item._id)) {
                        this.selectList.push(item)
                    }
                })
            }
        }
        async getList() {
            this.tableLoading = true
            try {
                const params = {
                    page: this.pagination.current,
                    page_size: this.pagination.limit,
                    order: '',
                    model_id: this.modelId,
                    role: this.role.superior_role
                }
                params.query_list = this.condition ? [this.condition] : []
                const res = await this.$api.AssetData.getInstanceList(params)
                const { result, data, message } = res
                if (!result) {
                    return this.$error(message)
                }
                this.tableData = data.insts
                this.pagination.count = data.count
                this.$nextTick(() => {
                    if (this.selectList.length > 0) {
                        this.tableData.forEach(item => {
                            const target = this.selectList.find(tex => tex._id === item._id)
                            if (target) {
                                const comTable: any = this.$refs.comTable
                                comTable.toggleRowSelection(item, true)
                            }
                        })
                    }
                })
            } finally {
                this.pageLoading = false
                this.tableLoading = false
            }
        }
        handlePageChange(page) {
            this.pagination.current = page
            this.getList()
        }
        // 当每页展示条数发生变化时触发
        limitChange(size) {
            this.pagination.current = 1
            this.pagination.limit = size
            this.getList()
        }
        clearSelect() {
            this.selectList = []
            const comTable: any = this.$refs.comTable
            comTable.clearSelection()
        }
        removeSelect(item, index) {
            this.selectList.splice(index, 1)
            this.$nextTick(() => {
                this.tableData.forEach(tex => {
                    if (tex._id === item._id) {
                        const comTable: any = this.$refs.comTable
                        comTable.toggleRowSelection(tex, false)
                    }
                })
            })
        }
    }
</script>

<style lang="scss" scoped>
.search-bar {
    display: flex;
    .model-list {
        width: 250px;
        margin-right: 10px;
    }
}
.choose-inst-container {
    height: calc(100% - 40px);
    width: 100%;
    display: flex;
    .container-content {
        width: calc(100% - 260px);
        padding-right: 16px;
        border-right: 1px solid #ccc;
        .operator-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
            .search-select {
                flex: 1;
            }
        }
    }
    .container-result {
        padding-left: 8px;
        width: 260px;
        flex-basis: 280px;
        display: flex;
        flex-direction: column;
        .header-title {
            display: flex;
            margin-bottom: 12px;
            .txt {
                color: #000;
                font-size: 12px;
            }
            .number {
                color: #b2bdcc;
                label {
                    color: #409EFF;
                    margin: 0 2px;
                }
            }
            .clear-button {
                cursor: pointer;
                color: #409EFF;
                font-size: 12px;
                flex: 1;
                text-align: right;
            }
        }
        .result-list {
            overflow-y: auto;
            .result-item {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0 8px;
                min-height: 35px;
                .result-item-txt {
                    .main {
                        color: #000;
                        font-size: 12px;
                        margin: 0;
                    }
                    .sub {
                        color: #b2bdcc;
                        font-size: 12px;
                    }
                }
                .weops-close {
                    color: #b2bdcc;
                    cursor: pointer;
                }
                &:hover {
                    cursor: pointer;
                    background: #f4f4f4;
                }
            }
        }
    }
}
</style>
