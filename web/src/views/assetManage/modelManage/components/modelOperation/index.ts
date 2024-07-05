import SelectIcon from '@/views/assetManage/modelManage/components/selectIcon/index.vue'
import DrawerComponent from '@/components/comDrawer/index.vue'
import { Vue, Component, Prop } from 'vue-property-decorator'
import { COMMON_RULE } from '@/common/constants'
@Component({
    components: {
        SelectIcon,
        DrawerComponent
    }
})
export default class ModelOperation extends Vue {
    @Prop({
        type: Array,
        default: () => []
    })
    groupList: Array<any>
    isShow: boolean = false
    formData = {
        group: '',
        onlyMark: '',
        name: '',
        model_type: 'base'
    }
    rules = {
        name: [
            COMMON_RULE
        ],
        onlyMark: [
            COMMON_RULE
        ],
        group: [
            COMMON_RULE
        ],
        model_type: [
            COMMON_RULE
        ]
    }
    iconUrl: string = 'cc-default_默认'
    loading: boolean = false
    currentType: string = 'add'
    modelDetail: any = ''
    formDataV2 = {}
    typeList: Array<any> = [
        { id: 'base', name: '基础模型' },
        { id: 'credential', name: '凭据模型' }
    ]
    get isAdd() {
        return this.currentType === 'add'
    }
    setIcon(url) {
        this.iconUrl = url
    }
    show(type, data) {
        this.currentType = type
        this.isShow = true
        if (type === 'edit') {
            this.iconUrl = data.icn || 'cc-default_默认'
            this.modelDetail = data
            this.formData = {
                group: data.classification_id,
                onlyMark: data.model_id,
                name: data.model_name,
                model_type: data.model_type || 'base'
            }
        } else {
            this.iconUrl = 'cc-default_默认'
            this.initData()
        }
        this.formDataV2 = JSON.parse(JSON.stringify(this.formData))
    }
    confirm() {
        const validateForm: any = this.$refs.validateForm
        validateForm.validate(valid => {
            if (valid) {
                const params: any = {
                    model_name: this.formData.name,
                    model_id: this.formData.onlyMark,
                    icn: this.iconUrl,
                    model_type: this.formData.model_type,
                    classification_id: this.formData.group
                }
                this.createModel(params)
            }
        })
    }
    createModel(params) {
        this.loading = true
        this.$api.ModelManage[this.isAdd ? 'createModel' : 'updateModel'](params).then(res => {
            if (!res.result) {
                this.$error(res.message)
                return false
            }
            this.$success(`${this.isAdd ? '新增' : '编辑'}模型成功!`)
            this.isShow = false
            this.isAdd ? this.$emit('getAllModelList') : this.$emit('refreshModel', params)
            if (this.isAdd) {
                this.$store.dispatch('getOtherMenus')
            }
        }).finally(() => {
            this.loading = false
        })
    }
    cancel() {
        const flag = this.$compareFormData(this.formData, this.formDataV2)
        if (!flag) {
            this.$confirm('放弃将导致未保存信息丢失', '是否放弃本次操作？', {
                center: true
            }).then(() => {
                this.isShow = false
            })
        } else {
            this.isShow = false
        }
    }
    selectIcon() {
        const selectIcon: any = this.$refs.selectIcon
        selectIcon.show(this.isAdd ? '' : this.iconUrl)
    }
    initData() {
        this.modelDetail = ''
        this.formData = {
            group: '',
            onlyMark: '',
            name: '',
            model_type: 'base'
        }
    }
}
