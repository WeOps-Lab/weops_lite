import { Component, Vue, Watch } from 'vue-property-decorator'
import AddModel from '@/views/assetManage/modelManage/components/modelOperation/index.vue'
import MenuTab from '@/components/menuTab/index.vue'
import ComTable from '@/components/comTable/index.vue'
import AttributesOperation from '@/views/assetManage/modelManage/components/attributesOperation/index.vue'
import ConnectOperation from '@/views/assetManage/modelManage/components/connectOperation/index.vue'
import { TableData } from '@/common/types'
import { PROPERTY_COLUMNS, OPERATE_TYPE_LIST, RELATION_COLUMNS, TARGET_BIND_LIST, MODEL_DETAIL_PANELS } from '@/common/constants/assetManage/modelManage'

@Component({
    components: {
        AddModel,
        MenuTab,
        ComTable,
        AttributesOperation,
        ConnectOperation
    }
})
export default class ModelManage extends Vue {
    panels: Array<any> = MODEL_DETAIL_PANELS
    active: string = 'property'
    columns: Array<TableData> = PROPERTY_COLUMNS
    relateColumns: Array<TableData> = RELATION_COLUMNS
    propertyData: Array<any> = []
    relationData: Array<any> = []
    loading: boolean = false
    relateLoading: boolean = false
    pageOccupiedHeight: number = 400
    modelGroupList: Array<any> = []
    modelList: Array<any> = []
    modelInfoList: Array<any> = []
    connectTypeList: Array<any> = []

    get modelInfo() {
        const modelInfo: any = this.$route.query.modelInfo || '{}'
        return JSON.parse(modelInfo)
    }

    get classifyId() {
        return 'ModelManage'
    }

    @Watch('active')
    onAlreadyAddListChanged(val) {
        if (val) {
            val === 'property' ? this.getModelAttrList() : this.getModelAssoList()
        }
    }

    mounted() {
        this.getAllModelList()
    }

    showMapping(row) {
        return TARGET_BIND_LIST.find(item => item.id === row.mapping)?.name || '--'
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
    getAllModelList() {
        this.loading = true
        Promise.all([this.getClassification(), this.getModelInfoList(), this.getModelAttrList('init'), this.getConnectTypeList()]).finally(() => {
            this.modelList = this.modelGroupList.map(item => {
                item.list = this.modelInfoList.filter(tex => tex.classification_id === item.classification_id)
                return item
            })
            this.loading = false
        })
    }

    showAttrType(type) {
        if (type === 'organization') return '组织'
        return OPERATE_TYPE_LIST.find(item => item.id === type)?.name || '--'
    }

    relationOperate(type, row = {}) {
        if (!this.$BtnPermission({
            id: this.classifyId,
            type: type === 'edit' ? 'ModelManage_edit' : 'ModelManage_create'
        })) {
            return false
        }
        const connectOperation: any = this.$refs.connectOperation
        connectOperation.show(type, row)
    }
    async getModelAssoList() {
        try {
            const params = {
                id: this.modelInfo.model_id
            }
            this.relateLoading = true
            const { result, message, data } = await this.$api.ModelManage.getModelAssoList(params)
            if (!result) {
                return this.$error(message)
            }
            this.relationData = data
        } catch (e) {
            console.error(e)
        } finally {
            this.relateLoading = false
        }
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

    async getModelAttrList(type?) {
        try {
            const params = {
                id: this.modelInfo.model_id
            }
            this.loading = true
            const { result, message, data } = await this.$api.ModelManage.getModelAttrList(params)
            if (!result) {
                return this.$error(message)
            }
            this.propertyData = data
        } catch (e) {
            console.error(e)
        } finally {
            this.loading = type === 'init'
        }
    }

    toTabMenu(item) {
        this.active = item.name
    }

    editAttr(row) {
        if (!this.$BtnPermission({
            id: this.classifyId,
            type: row ? 'ModelManage_edit' : 'ModelManage_create'
        })) {
            return false
        }
        const attributesOperation: any = this.$refs.attributesOperation
        attributesOperation.show({
            id: this.modelInfo.model_id,
            type: row ? '编辑' : '添加',
            rowData: row,
            groupList: []
        })
    }

    editModel() {
        if (!this.$BtnPermission({
            id: this.classifyId,
            type: 'ModelManage_edit'
        })) {
            return false
        }
        const editModel: any = this.$refs.editModel
        editModel.show('edit', this.modelInfo)
    }

    async getClassification() {
        const { result, message, data } = await this.$api.ModelManage.getClassification()
        if (!result) {
            return this.$error(message)
        }
        this.modelGroupList = data
    }

    async getModelInfoList() {
        const { result, message, data } = await this.$api.ModelManage.getModel()
        if (!result) {
            return this.$error(message)
        }
        this.modelInfoList = data
    }

    refreshModel(params) {
        this.$router.replace({
            name: 'ModelDetail',
            query: {
                modelInfo: JSON.stringify(params)
            }
        })
    }

    // 删除模型
    handleDelete(row) {
        if (!this.$BtnPermission({
            id: this.classifyId,
            type: 'ModelManage_delete'
        })) {
            return false
        }
        const params: any = {
            id: this.modelInfo.model_id
        }
        this.$confirm('确认要删除此模型？', '提示', {
            center: true
        }).then(() => {
            this.deleteModel(params)
        })
    }

    async deleteModel(params) {
        const res = await this.$api.ModelManage.deleteModel(params)
        if (!res.result) {
            return this.$error(res.message)
        }
        this.$success('删除成功')
        this.$router.go(-1)
    }
    // 删除关联
    deleteAsso(row) {
        if (!this.$BtnPermission({
            id: this.classifyId,
            type: 'ModelManage_delete'
        })) {
            return false
        }
        const params: any = {
            id: row.model_asst_id
        }
        this.$confirm('确认要删除此关联？', '提示', {
            center: true
        }).then(() => {
            this.deleteModelAsso(params)
        })
    }

    async deleteModelAsso(params) {
        const res = await this.$api.ModelManage.deleteAssociation(params)
        if (!res.result) {
            return this.$error(res.message)
        }
        this.$success('删除成功')
        this.getModelAssoList()
    }

    // 删除属性
    deleteAtrr(row) {
        if (!this.$BtnPermission({
            id: this.classifyId,
            type: 'ModelManage_delete'
        })) {
            return false
        }
        const params: any = {
            id: this.modelInfo.model_id,
            attr_id: row.attr_id
        }
        this.$confirm('确认要删除此属性？', '提示', {
            center: true
        }).then(() => {
            this.deleteModelAttr(params)
        })
    }

    async deleteModelAttr(params) {
        const res = await this.$api.ModelManage.deleteModelAttr(params)
        if (!res.result) {
            return this.$error(res.message)
        }
        this.$success('删除成功')
        this.getModelAttrList()
    }

    handlerChange() {
        this.getModelAttrList()
    }
}
