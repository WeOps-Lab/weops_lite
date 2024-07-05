import { Vue, Component, Prop } from 'vue-property-decorator'
import DrawerComponent from '@/components/comDrawer/index.vue'
import ComTable from '@/components/comTable/index.vue'
import SelectInput from '../selectInput/index.vue'
import { Pagination, TableData } from '@/common/types'
import { getAssetAttrValue } from '@/controller/func/common'
@Component({
    components: {
        DrawerComponent,
        ComTable,
        SelectInput
    }
})
export default class AddRelation extends Vue {
    @Prop({
        type: Array,
        default: () => []
    })
    connectTypeList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    modelInfoList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    groupList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    userList: Array<any>
    @Prop({
        type: Object,
        default: () => ({})
    })
    instInfo: any

    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    instanceList: Array<TableData> = []
    tableLoading: boolean = false
    loading: boolean = false
    condition: any = null
    visible: boolean = false
    pageOccupiedHeight: number = 320
    relation: string = '{}'
    relateLoading: boolean = false
    relationData: Array<any> = []
    relatedList: Array<any> = []
    columns: Array<any> = []
    propertyList: Array<any> = []

    get classifyId() {
        return this.$route.query.fromPage || this.instInfo.classifyId
    }

    get slotColumns() {
        return this.columns.filter(item => item.scopedSlots && item.scopedSlots !== 'operation')
    }

    get atrrList() {
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

    async getModelAttrList() {
        const params = this.getAttrParams()
        const { result, message, data } = await this.$api.ModelManage.getModelAttrList(params)
        if (!result) {
            return this.$error(message)
        }
        this.propertyList = data
        this.columns = this.getColumns(data)
        this.$nextTick(() => {
            const table: any = this.$refs.comTable
            table.updateColumns(this.columns)
        })
    }
    getAttrParams() {
        const relation = JSON.parse(this.relation)
        let { modelId } = this.$route.query
        if (!modelId) {
            modelId = this.instInfo.modelId
        }
        const { dst_model_id: dstModelId, src_model_id: srcModelId } = relation
        const params = {}
        if (modelId === dstModelId) {
            params.id = srcModelId
        }
        if (modelId === srcModelId) {
            params.id = dstModelId
        }
        return params
    }
    getColumns(data) {
        const operateColumn = {
            label: '操作',
            key: 'operation',
            align: 'left',
            width: '140px',
            fixed: 'right',
            scopedSlots: 'operation'
        }
        data.forEach(item => {
            item.key = item.attr_id
            item.label = item.attr_name
            item.minWidth = '100px'
            item.align = 'left'
            item.scopedSlots = item.attr_id
        })
        return [
            ...data,
            operateColumn
        ]
    }

    async show(relatedList) {
        this.visible = true
        this.relatedList = relatedList
        await this.getModelAssoList()
        if (!this.relation.length) {
            return
        }
        this.getColumnsAndData()
    }
    getColumnsAndData() {
        this.tableLoading = true
        Promise.all([this.getModelAttrList(), this.getInstanceList('init')]).finally(() => {
            this.tableLoading = false
        })
    }
    searchRelationData() {
        this.pagination.current = 1
        this.getColumnsAndData()
    }
    showModelName(id) {
        return this.modelInfoList.find(item => item.model_id === id)?.model_name || '--'
    }
    showConnectType(id, key) {
        return this.connectTypeList.find(item => item.id === id)?.[key] || '--'
    }
    getShowValue(field, tex) {
        return getAssetAttrValue(field, tex, {
            groupList: this.groupList,
            userList: this.userList
        })
    }
    async handleRelate(row) {
        const relation = JSON.parse(this.relation)
        const params = {
            model_asst_id: relation.model_asst_id,
            src_model_id: relation.src_model_id,
            dst_model_id: relation.dst_model_id,
            asst_id: relation.asst_id
        }
        let { modelId, instId } = this.$route.query
        if (!modelId) {
            modelId = this.instInfo.modelId
        }
        if (!instId) {
            instId = this.instInfo.instId
        }
        if (relation.dst_model_id === modelId) {
            params.dst_inst_id = instId
            params.src_inst_id = row._id
        } else {
            params.dst_inst_id = row._id
            params.src_inst_id = instId
        }
        const { result, message } = await this.$api.AssetData.createInstAsso(params)
        if (!result) {
            return this.$error(message)
        }
        this.$success('已成功关联')
        this.$emit('refreshList', 'update')
    }
    updateInstanceList(data) {
        this.relatedList = data
        this.getInstanceList()
    }
    async getModelAssoList() {
        this.relateLoading = true
        try {
            const params = {
                id: this.$route.query.modelId || this.instInfo.modelId,
                body: {
                    model_type: this.instInfo.model_type || 'base'
                }
            }
            const { result, message, data } = await this.$api.ModelManage.getModelAssoList(params)
            if (!result) {
                return this.$error(message)
            }
            this.relationData = data.map(item => {
                return {
                    name: `${this.showModelName(item.src_model_id)}-${this.showConnectType(item.asst_id, 'label')}-${this.showModelName(item.dst_model_id)}`,
                    id: JSON.stringify(item)
                }
            })
            this.relation = JSON.stringify(data[0]) || ''
        } finally {
            this.relateLoading = false
        }
    }
    changeFeild(condition) {
        this.pagination.current = 1
        this.condition = condition
        this.getInstanceList()
    }
    async getInstanceList(type?) {
        this.tableLoading = true
        try {
            const params = this.getParams()
            const { result, message, data } = await this.$api.AssetData.getInstanceList(params)
            if (!result) {
                return this.$error(message)
            }
            this.instanceList = data.insts.map(item => {
                const target = this.relatedList.find(rel => rel._id === item._id)
                return {
                    ...item,
                    relatedId: target?.inst_asst_id || '',
                    isRelated: !!target
                }
            })
            this.pagination.count = data.count
        } finally {
            this.tableLoading = type === 'init'
        }
    }
    cancelRelate(row) {
        this.$confirm('确定取消关联吗？', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            center: true
        }).then(async() => {
            try {
                const res = await this.$api.AssetData.deleteInstAsso({
                    id: row.relatedId
                })
                if (!res.result) {
                    return this.$error(res.message)
                } else {
                    this.$success('已成功取消关联!')
                    this.$emit('refreshList', 'update')
                }
                return true
            } catch (e) {
                return false
            }
        })
    }
    getParams() {
        const attrParams = this.getAttrParams()
        const params = {
            query_list: [],
            page: this.pagination.current,
            page_size: this.pagination.limit,
            order: '',
            model_id: attrParams.id
        }
        if (this.condition) {
            params.query_list = [this.condition]
        }
        return params
    }
    beforeCloseDialog() {
        this.visible = false
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
