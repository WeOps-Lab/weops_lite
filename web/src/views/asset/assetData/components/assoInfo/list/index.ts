import { Vue, Component, Prop } from 'vue-property-decorator'
import ComTable from '@/components/comTable/index.vue'
import { Pagination } from '@/common/types'
import Collapse from '@/components/collapse/index.vue'
import AddRelation from '../../addRelation/index.vue'
import { getAssetAttrValue } from '@/controller/func/common'
@Component({
    name: 'asso-list',
    components: {
        ComTable,
        Collapse,
        AddRelation
    }
})
export default class AssoList extends Vue {
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
    propertyList: Array<any>
    @Prop({
        type: Object,
        default: () => ({})
    })
    instInfo: any

    resourcList: Array<any> = []
    loading: boolean = false
    assoData: Array<any> = []
    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    tableMaxHeight: number = 300
    relatedList: Array<any> = []

    get classifyId() {
        return this.$route.query.fromPage || this.instInfo.classifyId
    }

    get operatePower() {
        return {
            id: this.classifyId,
            type: `${this.classifyId}_manage`
        }
    }

    mounted() {
        this.initData()
    }

    showTable(item) {
        return !!item.columns?.length
    }
    addRelation() {
        if (!this.$BtnPermission(this.operatePower)) {
            return false
        }
        const addRelation: any = this.$refs.addRelation
        addRelation.show(this.relatedList)
    }
    cancelRelate(row) {
        if (!this.$BtnPermission(this.operatePower)) {
            return false
        }
        this.$confirm('确定取消关联吗？', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            center: true
        }).then(async() => {
            try {
                const res = await this.$api.AssetData.deleteInstAsso({
                    id: row.inst_asst_id
                })
                if (!res.result) {
                    return this.$error(res.message)
                } else {
                    this.$success('已成功取消关联!')
                    this.initData()
                }
                return true
            } catch (e) {
                return false
            }
        })
    }
    expandAll(bool) {
        this.resourcList.forEach(item => {
            item.isExpand = bool
        })
    }
    async initData(type?) {
        this.loading = true
        try {
            const { instId, modelId } = this.$route.query
            const params = {
                inst_id: instId || this.instInfo.instId,
                model_id: modelId || this.instInfo.modelId,
                body: {
                    model_type: this.instInfo.model_type || 'base'
                }
            }
            const { result, message, data } = await this.$api.AssetData.getAssoInstList(params)
            if (!result) {
                this.loading = false
                return this.$error(message)
            }
            this.assoData = data
            this.resourcList = this.assoData.filter(row => row.inst_list?.length).map((item, index) => {
                return {
                    label: this.showConnectName(item),
                    attrId: this.getAttrId(item),
                    id: index,
                    list: item.inst_list,
                    isExpand: true
                }
            })
            this.relatedList = this.resourcList.reduce((pre, cur) => {
                return pre.concat(cur.list)
            }, [])
            Promise.all(this.resourcList.map(item => this.getModelAttrList(item, { id: item.attrId }))).finally(() => {
                this.loading = false
            })
            if (type === 'update') {
                const addRelation: any = this.$refs.addRelation
                addRelation?.updateInstanceList(this.relatedList)
            }
        } catch {
            this.loading = false
        }
    }
    getAttrId(item) {
        const { modelId } = this.$route.query
        const { dst_model_id: dstModelId, src_model_id: srcModelId } = item
        let id = modelId || this.instInfo.modelId
        if (modelId === dstModelId) {
            id = srcModelId
        }
        if (modelId === srcModelId) {
            id = dstModelId
        }
        return id
    }
    async getModelAttrList(item, params) {
        const { result, message, data } = await this.$api.ModelManage.getModelAttrList(params)
        if (!result) {
            return this.$error(message)
        }
        const columns = this.getColumns(data)
        this.$set(item, 'columns', columns)
        this.$set(item, 'slotColumns', columns.filter(item => item.scopedSlots && item.scopedSlots !== 'operation'))
    }
    getShowValue(field, tex) {
        return getAssetAttrValue(field, tex, {
            groupList: this.groupList,
            userList: this.userList
        })
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
        const propertyList = this.$copy(data)
        propertyList.forEach(item => {
            item.key = item.attr_id
            item.label = item.attr_name
            item.minWidth = '100px'
            item.align = 'left'
            item.scopedSlots = item.attr_id
        })
        return [
            ...propertyList,
            operateColumn
        ]
    }
    showModelName(id) {
        return this.modelInfoList.find(item => item.model_id === id)?.model_name || '--'
    }
    showConnectType(id, key) {
        return this.connectTypeList.find(item => item.id === id)?.[key] || '--'
    }
    showConnectName(row) {
        const sourceName = this.showModelName(row.src_model_id)
        const targetName = this.showModelName(row.dst_model_id)
        const relation = this.showConnectType(row.asst_id, 'name')
        return `${sourceName} ${relation} ${targetName}`
    }
}
