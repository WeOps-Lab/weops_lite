import { Component, Emit, Vue } from 'vue-property-decorator'
import DrawerComponent from '@/components/comDrawer/index.vue'
import { GROUP_OPETATE_RULE } from '@/common/constants/assetManage/modelManage'
@Component({
    components: {
        DrawerComponent
    }
})
export default class ModelOperation extends Vue {
    visible: boolean = false
    formData: any = {
        onlyMark: '',
        name: ''
    }
    formDataCopy: any = {}
    groupDetial: any = {}
    rules = GROUP_OPETATE_RULE
    loading: boolean = false
    currentType: string = 'add'
    get isAdd() {
        return this.currentType === 'add'
    }
    show(type, data) {
        this.currentType = type
        this.visible = true
        if (type === 'edit') {
            this.formData = {
                onlyMark: data.classification_id,
                name: data.classification_name
            }
            this.groupDetial = data
            this.formDataCopy = this.$copy(this.formData)
            return
        }
        this.initData()
    }
    confirm() {
        this.$refs.validateForm.validate(valid => {
            if (valid) {
                const params: any = {
                    classification_name: this.formData.name,
                    classification_id: this.formData.onlyMark
                }
                this.createOrEditGroup(params)
            }
        })
    }
    async createOrEditGroup(params) {
        this.loading = true
        const url = this.isAdd ? 'createClassification' : 'updateClassification'
        try {
            const res = await this.$api.ModelManage[url](params)
            if (!res.result) {
                this.$error(res.message)
                return
            }
            this.$success(`${this.isAdd ? '新增' : '编辑'}分组成功!`)
            this.visible = false
            this.getAllModelList()
        } finally {
            this.loading = false
        }
    }
    cancel() {
        const result = this.$compareFormData(this.formData, this.formDataCopy)
        if (!result) {
            this.$confirm('放弃将导致未保存信息丢失', '是否放弃本次操作？', {
                center: true
            }).then(() => {
                this.visible = false
            })
            return
        }
        this.visible = false
    }
    initData() {
        this.groupDetial = {}
        this.formData = {
            onlyMark: '',
            name: ''
        }
        this.formDataCopy = this.$copy(this.formData)
    }
    @Emit('getAllModelList')
    getAllModelList() {
        return ''
    }
}
