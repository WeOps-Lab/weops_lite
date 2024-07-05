<template>
    <div class="asset-search" v-loading="pageLoading">
        <div v-if="onlySearchShow" class="asset-search-box">
            <el-input
                class="asset-search-input"
                placeholder="请输入关键字，点击或回车搜索"
                v-model="search"
                @keyup.enter.native="showTextSearch">
                <el-button
                    slot="append"
                    icon="el-icon-search"
                    type="primary"
                    @click="showTextSearch">
                    搜索
                </el-button>
            </el-input>
        </div>
        <div v-else class="asset-search-result">
            <el-input
                style="width: 400px;"
                class="mb10"
                placeholder="请输入关键字，点击或回车搜索"
                v-model="search"
                size="small"
                clearable
                @clear="handleClear"
                @keyup.enter.native="handleTextChange">
                <el-button
                    slot="append"
                    icon="el-icon-search"
                    type="primary"
                    @click="handleSearch">
                    搜索
                </el-button>
            </el-input>
            <div class="asset-list" v-loading="tableLoading">
                <el-tabs class="asset-model-tabs" v-model="currentModel" @tab-click="handleTabClick">
                    <el-tab-pane
                        v-for="(item,index) in instList"
                        :key="index"
                        :label="item.modelName"
                        :name="item.modelId">
                        <com-table
                            :ref="`comTable${item.modelId}`"
                            :data="getTableData(item.children || [])"
                            :columns="columns"
                            :pagination="pagination"
                            height="calc(100vh - 230px)"
                            @page-change="handlePageChange"
                            @page-limit-change="handleLimitChange"
                        >
                            <template slot="operation" slot-scope="{ row }">
                                <el-button
                                    type="text"
                                    size="small"
                                    @click="checkDetail(row)">
                                    详情
                                </el-button>
                            </template>
                            <template v-for="field in slotColumns" :slot="field.scopedSlots" slot-scope="{ row }">
                                <div :key="field.key">
                                    <el-tag
                                        v-if="field.attr_type === 'bool'"
                                        :type="row[field.key] ? 'success' : ''">
                                        {{getShowValue(field, row)}}
                                    </el-tag>
                                    <span
                                        v-else
                                        :class="{
                                            'fit-content': getShowValue(field, row).includes(search)
                                        }">
                                        {{ getShowValue(field, row) }}
                                    </span>
                                </div>
                            </template>
                        </com-table>
                    </el-tab-pane>
                </el-tabs>
                <el-empty
                    v-if="!instList.length"
                    :image-size="80"
                    class="exception-wrap-item exception-part"
                    description="暂无数据"
                >
                </el-empty>
            </div>
        </div>
        <drawer-component
            :title="`实例详情-${currentModelCfg.inst_name}`"
            :size="800"
            :visible="visible"
            destroy-on-close
            custom-class="common-dialog-wrapper"
            :before-close="beforeCloseDialog">
            <div slot="content" class="content-box common-dialog-wrapper-main">
                <el-button
                    class="see-more"
                    type="text"
                    @click="seeMore">
                    查看更多
                </el-button>
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

<script lang="ts" >
    import { Component, Vue } from 'vue-property-decorator'
    import { Pagination } from '@/common/types'
    import ComTable from '@/components/comTable/index.vue'
    import DrawerComponent from '@/components/comDrawer/index.vue'
    import BaseInfo from '@/views/asset/assetData/components/baseInfo/index.vue'
    import { getAssetAttrValue } from '@/controller/func/common'
@Component({
    components: {
        ComTable,
        DrawerComponent,
        BaseInfo
    }
})
export default class Relation extends Vue {
    search: string = ''
    onlySearchShow: boolean = true
    instList: Array<any> = []
    currentModel: string = ''
    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    columns: Array<any> = []
    propertyList: Array<any> = []
    userList: Array<any> = []
    groupList: Array<any> = []
    modelList: Array<any> = []
    pageLoading: boolean = false
    tableLoading: boolean = false
    visible: boolean = false
    currentModelCfg: any = {}

    get slotColumns() {
        return this.columns.filter(item => item.scopedSlots && item.scopedSlots !== 'operation')
    }

    created() {
        this.initPage()
    }

    mounted() {
        this.dealPageStyle(0, 'calc(100vh - 52px)')
    }

    beforeDestroy() {
        this.dealPageStyle(null, null)
    }

    seeMore() {
        const routeObj: any = {
            name: 'AssetInstDetial',
            query: {
                fromPage: this.modelList.find(item => item.model_id === this.currentModel)?.classification_id || '',
                inst_name: this.currentModelCfg.inst_name || '--',
                modelId: this.currentModel,
                instId: this.currentModelCfg._id
            }
        }
        const route = this.$router.resolve(routeObj)
        window.open(route.href, '_blank')
    }
    beforeCloseDialog() {
        this.visible = false
    }
    getTableData(data) {
        return data.slice((this.pagination.current - 1) * this.pagination.limit, this.pagination.current * this.pagination.limit)
    }
    initPage() {
        this.pageLoading = true
        Promise.all([this.getAllModelList(), this.getGroups(), this.getUserList()]).finally(() => {
            this.pageLoading = false
        })
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
    getShowValue(field, tex) {
        return getAssetAttrValue(field, tex, {
            groupList: this.groupList,
            userList: this.userList
        })
    }
    getModelName(item) {
        return (this.modelList.find(model => model.model_id === item.modelId)?.model_name || '--') + `(${item.children.length})`
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
    async getModelAttrList() {
        this.tableLoading = true
        try {
            if (!this.currentModel) {
                return
            }
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
            this.$nextTick(() => {
                const resourceTable: any = this.$refs[`comTable${this.currentModel}`][0]
                resourceTable.updateColumns(this.columns)
            })
        } finally {
            this.tableLoading = false
        }
    }

    getColumns(list) {
        const operateColumn = {
            label: '操作',
            key: 'operation',
            align: 'left',
            width: '170px',
            fixed: 'right',
            scopedSlots: 'operation'
        }
        return [
            ...list,
            operateColumn
        ]
    }
    handleTabClick(val) {
       this.getModelAttrList()
       this.pagination.count = this.instList.find(item => item.modelId === this.currentModel)?.children?.length || 0
       this.pagination.current = 1
    }
    checkDetail(row) {
        this.currentModelCfg = {
            ...row,
            inst_id: row._id
        }
        this.visible = true
    }
    handlePageChange(page) {
        this.pagination.current = page
    }
    handleLimitChange(size) {
        this.pagination.current = 1
        this.pagination.limit = size
    }
    showTextSearch() {
        if (!this.search) {
            return
        }
        this.onlySearchShow = false
        this.handleSearch()
    }
    handleTextChange() {
        this.instList = []
        if (!this.search) {
            this.onlySearchShow = true
            return
        }
        this.handleSearch()
    }
    handleClear() {
        this.instList = []
    }
    async handleSearch() {
        this.instList = []
        if (!this.search) {
            this.onlySearchShow = true
            return
        }
        if (this.tableLoading) {
            return
        }
        this.tableLoading = true
        const { result, message, data } = await this.$api.AssetSearch.getFulltextSearchList({
            search: this.search
        })
        if (!result) {
            this.tableLoading = false
            return this.$error(message)
        }
        this.instList = this.getAssetList(data)
        const defaultList = this.instList.at() || {}
        this.currentModel = defaultList.modelId || ''
        this.pagination.count = defaultList.children?.length || 0
        this.getModelAttrList()
    }
    getAssetList(data) {
        const result = data.reduce((acc, item) => {
            const { model_id: modelId } = item
            if (acc[modelId]) {
              acc[modelId].children.push(item)
            } else {
              acc[modelId] = { modelId, children: [item] }
            }
            return acc
        }, {})
        return Object.values(result).map(item => ({
            modelName: this.getModelName(item),
            ...item
        }))
    }
    dealPageStyle(padding, height) {
        const containerDom = document.querySelector('#main-container')
        const el = document.querySelector('.el-main')
        containerDom.style.height = containerDom.style.maxHeight = height
        containerDom.style.paddingBottom = padding
        el.style.padding = padding
    }
}
</script>
<style lang="scss" scoped>
.asset-search {
    width: 100%;
    height: 100%;
    background-color: #fff;
    .asset-search-box {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 100%;
        background: url(~@/assets/img/search_bg.png) no-repeat;
        background-size: contain;
        background-position: 50% 200px;
        background-color: #f5f7fa;
        .asset-search-input {
            width: 800px;
            align-self: flex-start;
            margin-top: 120px;
        }
    }
    .asset-search-result {
        padding: 20px;
        .asset-list {
            height: calc(100vh - 250px);
        }
    }
    .fit-content {
        color: #409EFF;
    }
}
.content-box {
    .see-more {
        position: absolute;
        top: 70px;
        right: 30px;
    }
}
/* stylelint-disable selector-class-pattern */
/deep/ .el-input-group__append, .el-input-group__prepend {
    background-color: #409EFF;
    color: #FFF;
    border-top: 1px solid #409EFF;
    border-bottom: 1px solid #409EFF;
}

</style>
