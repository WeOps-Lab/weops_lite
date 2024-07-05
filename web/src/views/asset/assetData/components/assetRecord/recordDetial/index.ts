import { Vue, Component, Prop } from 'vue-property-decorator'
import DrawerComponent from '@/components/comDrawer/index.vue'
import ComTable from '@/components/comTable/index.vue'
import { getAssetAttrValue } from '@/controller/func/common'

@Component({
    name: 'record-detial',
    components: {
        DrawerComponent,
        ComTable
    }
})
export default class RecordDetial extends Vue {
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
        type: Array,
        default: () => []
    })
    userList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    groupList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    connectTypeList: Array<any>

    visible: boolean = false
    loading: boolean = false
    formData: any = {
        list: [
            { label: '动作', id: 'type' },
            { label: '模型类型', id: 'model_id' },
            { label: '操作实例', id: 'inst_id' },
            // { label: '操作描述', id: 'label' },
            { label: '操作时间', id: 'created_at' },
            { label: '操作账号', id: 'operator' }
        ],
        attrList: [],
        attrColumns: [
            {
                label: '属性',
                key: 'attr',
                align: 'left',
                minWidth: '50'
            },
            {
                label: '变更前',
                key: 'before',
                align: 'left',
                minWidth: '100px'
            },
            {
                label: '变更后',
                key: 'after',
                align: 'left',
                minWidth: '100px'
            }
        ]
    }
    recordRow: any = {}
    typeList: Array<any> = []

    getShowValue(field, tex) {
        return getAssetAttrValue(field, tex, {
            groupList: this.groupList,
            userList: this.userList
        })
    }
    showDialog(row, typeList) {
        this.visible = true
        this.recordRow = row
        this.typeList = typeList
        if (this.recordRow.label === 'instance_association') {
            this.formData.attrColumns[0] = {
                label: '对象类型',
                key: 'attr',
                align: 'left',
                minWidth: '50'
            }
        }
        this.getChangeRecordDetail()
    }
    getDisplayName(id) {
        let label: any = this.recordRow[id] || '--'
        switch (id) {
            case 'type':
                label = this.getOperateType(label)
                break
            case 'model_id':
                label = this.getModelName(label)
                break
            case 'inst_id':
                label = this.$route.query.inst_name || '--'
                break
        }
        return label
    }
    getOperateType(id) {
        return this.typeList.find(item => item.id === id)?.name || '--'
    }
    getModelName(id) {
        return this.modelInfoList.find(item => item.model_id === id)?.model_name || '--'
    }
    async getChangeRecordDetail() {
        try {
            this.loading = true
            const res = await this.$api.AssetData.getChangeRecordDetail({ id: this.recordRow.id })
            const { message, result, data } = res
            if (!result) {
                this.$error(message)
                this.formData.attrList = []
                return false
            }
            const { before_data: beforeData, after_data: afterData, label, type } = data
            if (label === 'instance') {
                const list = type === 'delete_entity' ? [] : afterData
                this.formData.attrList = Object.keys(list).map(item => {
                    const field = this.propertyList.find(prop => prop.attr_id === item)
                    if (field) {
                        field.key = field.attr_id
                        const beforTex = {}
                        beforTex[item] = beforeData[item]
                        const afterTex = {}
                        afterTex[item] = afterData[item]
                        return {
                            attr: field.attr_name,
                            before: this.getShowValue(field, beforTex),
                            after: this.getShowValue(field, afterTex)
                        }
                    }
                    return {
                        attr: null
                    }
                }).filter(attr => !!attr.attr)
            } else {
                let before = '--'
                let after = '--'
                this.formData.attrList = data
                if (type === 'delete_edge') {
                    before = `${this.showModelName(beforeData.edge.src_model_id)}(${beforeData.src.inst_name})${this.showConnectType(beforeData.edge.asst_id)}${this.showModelName(beforeData.edge.dst_model_id)}(${beforeData.dst.inst_name})`
                } else {
                    after = `${this.showModelName(afterData.edge.src_model_id)}(${afterData.src.inst_name})${this.showConnectType(afterData.edge.asst_id)}${this.showModelName(afterData.edge.dst_model_id)}(${afterData.dst.inst_name})`
                }
                this.formData.attrList = [{
                    attr: '关联关系',
                    before,
                    after
                }]
            }
        } catch {
            this.formData.attrList = []
        } finally {
            this.loading = false
        }
    }
    showModelName(id) {
        return this.modelInfoList.find(item => item.model_id === id)?.model_name || '--'
    }
    showConnectType(id) {
        return this.connectTypeList.find(item => item.id === id)?.label || '--'
    }
    beforeCloseDialog() {
        Object.assign(this.$data, this.$options.data.call(this))
        this.visible = false
    }
}
