import { Vue, Component, Prop } from 'vue-property-decorator'
import Collapse from '@/components/collapse/index.vue'
import { getAssetAttrValue } from '@/controller/func/common'
@Component({
    name: 'add-resource',
    components: {
        Collapse
    }
})
export default class AddResource extends Vue {
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
    propertyList: Array<any>
    @Prop({
        type: Object,
        default: () => ({})
    })
    currentModelCfg: any
    @Prop({
        type: String,
        default: () => '33%'
    })
    displayPercent: string
    @Prop({
        type: Boolean,
        default: () => true
    })
    allowEdit: boolean

    resourcList: Array<any> = [
        {
            label: '组织信息',
            id: 'group',
            list: [],
            isExpand: true
        },
        {
            label: '基础信息',
            id: 'base',
            list: [],
            isExpand: true
        }
    ]
    instDetail: any = {}
    loading: boolean = false
    formData: any = {}
    rules = {}
    formDataV2 = {}
    attrList: Array<any> = []

    get classifyId() {
        return this.$route.query.fromPage
    }

    get instId() {
        return this.currentModelCfg.inst_id || this.$route.query.instId
    }

    get operatePower() {
        return {
            id: this.classifyId,
            type: `${this.classifyId}_manage`
        }
    }

    async mounted() {
        if (this.currentModelCfg.model_id) {
            await this.getModelAttrList()
        } else {
            this.attrList = this.propertyList
        }
        this.getInstDetial()
    }
    async getModelAttrList() {
        const params = {
            id: this.currentModelCfg.model_id
        }
        const { result, message, data } = await this.$api.ModelManage.getModelAttrList(params)
        if (!result) {
            return this.$error(message)
        }
        this.attrList = data
    }
    async getInstDetial() {
        this.loading = true
        try {
            const params = {
                id: this.instId
            }
            const { result, message, data } = await this.$api.AssetData.getInstDetial(params)
            if (!result) {
                return this.$error(message)
            }
            this.instDetail = data
            this.initData(data)
        } finally {
            this.loading = false
        }
    }
    // 编辑信息
    editInfo(tex) {
        if (!this.$BtnPermission(this.operatePower)) {
            return false
        }
        this.$set(tex, 'isEdit', true)
    }
    getShowValue(field) {
        field.key = field.attr_id
        return getAssetAttrValue(field, this.formData, {
            groupList: this.groupList,
            userList: this.userList
        })
    }
    initData(data) {
        const propertyList = this.$copy(this.attrList)
        propertyList.forEach(item => {
            if (item.is_required) {
                this.$set(this.rules, item.attr_id, {
                    required: true,
                    message: '必填项',
                    trigger: 'blur'
                })
            }
            const defaultVal = item.attr_type === 'bool' ? false : ''
            this.$set(this.formData, item.attr_id, data[item.attr_id] || defaultVal)
        })
        const baseInfo = this.resourcList.find(item => item.id === 'base')
        const groupInfo = this.resourcList.find(item => item.id === 'group')
        baseInfo.list = propertyList.filter(item => item.attr_id !== 'organization')
        groupInfo.list = propertyList.filter(item => item.attr_id === 'organization')
        this.formDataV2 = this.$copy(this.formData)
    }
    confirmEdit(tex) {
        if (!this.$BtnPermission(this.operatePower)) {
            return false
        }
        const addResourceForm: any = this.$refs.addResourceForm
        addResourceForm.validateField([tex.attr_id], async errMsg => {
            if (!errMsg) {
                const info = this.$copy(this.formDataV2)
                info[tex.attr_id] = this.formData[tex.attr_id]
                const params = {
                    id: this.instId,
                    body: {}
                }
                params.body[tex.attr_id] = this.formData[tex.attr_id]
                try {
                    this.loading = true
                    const { result, message } = await this.$api.AssetData.updateInstance(params)
                    if (!result) {
                        return this.$error(message)
                    }
                    this.$success('修改成功！')
                    this.formDataV2[tex.attr_id] = this.formData[tex.attr_id]
                    tex.isEdit = false
                } finally {
                    this.loading = false
                }
            }
        })
    }
    // 取消编辑
    cancelEdit(tex) {
        this.formData[tex.attr_id] = this.formDataV2[tex.attr_id]
        tex.isEdit = false
        const addResourceForm: any = this.$refs.addResourceForm
        addResourceForm.clearValidate()
    }
}
