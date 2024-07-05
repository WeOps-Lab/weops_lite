import { Component, Vue } from 'vue-property-decorator'
import addModel from '@/views/assetManage/modelManage/components/modelOperation/index.vue'
import groupOperation from '@/views/assetManage/modelManage/components/groupOperation/index.vue'
import PageExplanation from '@/components/pageExplanation/index.vue'
@Component({
    components: {
        addModel,
        groupOperation,
        PageExplanation
    }
})
export default class ModelManage extends Vue {
    searchKey: string = ''
    loading: boolean = false
    modelList: Array<any> = []
    groupList: Array<any> = []
    allModelList: Array<any> = []
    dragStartParent: any = ''
    dragEndParent: any = ''
    oldData: any = ''
    dragStartId: number = 0
    dragEndId: number = 0
    dragStartIndex: string | number = ''
    dragEndIndex: string | number = ''
    mounted() {
        this.getAllModelList()
    }
    get modelGroupList() {
        return this.groupList
    }
    dragstart(parentValue, value, index) {
        this.dragStartParent = parentValue
        this.oldData = value
        this.dragStartId = value.id
        this.dragStartIndex = index
    }
    dragenter(parentValue, value, index) {
        this.dragEndParent = parentValue
        this.dragEndId = value.id
        this.dragEndIndex = index
    }
    dragover(e) {
        e.preventDefault()
    }
    getDragend() {
        if (this.dragStartId !== this.dragEndId && this.dragStartParent.id === this.dragEndParent.id) {
            const oldIndex = this.dragStartParent.list.findIndex(item => item.id === this.dragStartId)
            const newIndex = this.dragStartParent.list.findIndex(item => item.id === this.dragEndId)
            // 删除之前DOM节点
            this.dragStartParent.list.splice(oldIndex, 1)
            // 在拖拽结束目标位置增加新的DOM节点
            this.dragStartParent.list.splice(newIndex, 0, this.oldData)
            this.setModelIndex()
        }
        this.initDragData()
    }
    async setModelIndex() {
        try {
            const params = {}
            this.modelList.forEach(item => {
                const obj = {}
                item.list.forEach((tex, index) => {
                    obj[tex.bk_obj_id] = index
                })
                params[item.bk_classification_id] = obj
            })
            this.loading = true
            const { result, message } = await this.$api.modelSetting.setModelIndex(params)
            if (!result) {
                this.$error(message)
                return false
            }
            this.$success('修改成功')
        } catch (e) {
            console.error(e)
        } finally {
            this.loading = false
        }
    }
    initDragData() {
        this.dragStartParent = ''
        this.dragEndParent = ''
        this.oldData = ''
        this.dragStartId = 0
        this.dragEndId = 0
        this.dragStartIndex = ''
        this.dragEndIndex = ''
    }
    handleTipsConfig(item) {
        return {
            placement: 'left-start',
            content: '内置模型组不支持删除和修改',
            disabled: item.classification_id.startsWith('ex_')
        }
    }
    goAssetRecord(item, tex) {
        if (item.bk_classification_id === 'bk_file') {
            return false
        }
        if (item.bk_classification_id === 'bk_host_manage') {
            this.$router.push({
                name: 'AssetRecordsHost'
            })
        } else {
            this.$router.push({
                name: item.bk_classification_id,
                params: {
                    activeId: tex.bk_obj_id
                }
            })
        }
    }
    checkModelDetail(tex) {
        this.$router.push({
            name: 'ModelDetail',
            query: {
                modelInfo: JSON.stringify(tex)
            }
        })
    }
    getAllModelList() {
        this.loading = true
        Promise.all([this.getClassification(), this.getModelInfoList()]).then(res => {
            const [classifyRes, modelListRes] = res
            if (!classifyRes.result) {
                this.$error(classifyRes.message)
                this.modelList = []
                return false
            }
            if (!modelListRes.result) {
                this.$error(modelListRes.message)
                this.modelList = []
                return false
            }
            this.groupList = classifyRes.data || []
            if (classifyRes.result && modelListRes.result) {
                let modelList = this.groupList.map(item => {
                    item.list = modelListRes.data.filter(tex => tex.classification_id === item.classification_id && tex.model_name.includes(this.searchKey))
                    return item
                })
                if (this.searchKey) {
                    modelList = modelList.filter(item => item.list.length)
                }
                this.modelList = modelList
            }
            if (!this.searchKey) {
                this.allModelList = JSON.parse(JSON.stringify(this.modelList))
            }
        }).finally(() => {
            this.loading = false
        })
    }
    addModel() {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: 'ModelManage_create'
        })) {
            return false
        }
        const addModel: any = this.$refs.addModel
        addModel.show('add')
    }
    groupOperation(type, data = {}) {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: type === 'edit' ? 'ModelManage_edit' : 'ModelManage_create'
        })) {
            return false
        }
        const groupOperation: any = this.$refs.groupOperation
        groupOperation.show(type, data)
    }
    getIconUrl(tex) {
        try {
            return require(`@/assets/svg/model/${tex.icn || 'cc-default_默认'}.svg`)
        } catch (e) {
            return require('@/assets/svg/model/cc-default_默认.svg')
        }
    }
    getModelInfoList() {
        return this.$api.ModelManage.getModel({
            bk_obj_name: this.searchKey
        })
    }
    getClassification() {
        return this.$api.ModelManage.getClassification()
    }
    // 删除分组
    handleDelete(row) {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: 'ModelManage_delete'
        })) {
            return false
        }
        const params: any = {
            id: row.classification_id,
            classification_name: row.classification_name
        }
        this.$confirm('确认要删除此分组？', '提示', {
            center: true
        }).then(() => {
            this.confirmDeleteGroup(params)
        })
    }
    async confirmDeleteGroup(params) {
        this.loading = true
        const res = await this.$api.ModelManage.deleteClassification(params)
        if (!res.result) {
            this.$error(res.message)
            this.loading = false
            return
        }
        this.$success('删除成功')
        this.getAllModelList()
    }
}
