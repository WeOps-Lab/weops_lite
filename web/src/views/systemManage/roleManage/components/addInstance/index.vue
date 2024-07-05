<template>
    <drawer-component
        title="新增实例"
        :visible="visible"
        :size="800"
        destroy-on-close
        append-to-body
        :before-close="beforeCloseDialog">
        <div slot="content" class="common-dialog-wrapper-main">
            <div class="choose-inst-container">
                <div class="container-content">
                    <selectInput
                        class="mb20"
                        :property-list="attrList"
                        :group-list="groupList"
                        :user-list="userList"
                        @change="changeFeild" />
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
                    >
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
            type: Array,
            default: () => []
        })
        slotColumns: any[]
        @Prop({
            type: Array,
            default: () => []
        })
        groupList: any
        @Prop({
            type: Array,
            default: () => []
        })
        userList: any
        @Prop({
            type: Array,
            default: () => []
        })
        instanceColumns: any[]
        @Prop({
            type: Array,
            default: () => []
        })
        attrList: any[]
        @Prop({
            type: String,
            default: () => ''
        })
        modelId: string
        @Prop({
            type: Object,
            default: () => ({})
        })
        role: any
        visible: boolean = false
        tableData: any[] = []
        tableLoading: boolean = false
        pagination = {
            current: 1,
            count: 0,
            limit: 20
        }
        selectList: any[] = []
        condition: any = null

        get tableHeight() {
            return 'calc(100vh - 250px)'
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
            this.updateColumns()
            this.getList()
            this.selectList = this.$Copy(data)
        }
        filterList() {
            this.pagination.current = 1
            this.getList()
        }
        confirm() {
            if (!this.selectList.length) {
                this.$warn('实例列表不能为空！')
                return
            }
            this.$emit('change-list', this.selectList)
            this.beforeCloseDialog()
        }
        updateColumns() {
            this.$nextTick(() => {
                const comTable: any = this.$refs.comTable
                comTable.updateColumns(this.instanceColumns.filter(item => item.key !== 'operation'))
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
.choose-inst-container {
    height: 100%;
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
