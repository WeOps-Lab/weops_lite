import { Vue, Component } from 'vue-property-decorator'
import DrawerComponent from '@/components/comDrawer/index.vue'
import { ExtenalChainRules } from '@/common/types/systemManage/sysSetting'
import { COMMON_RULE } from '@/common/constants'
import uuid from 'uuid'
@Component({
    name: 'external-chain',
    components: {
        DrawerComponent
    }
})
export default class ExternalChain extends Vue {
    isShow: boolean = false
    formData = {
        name: '',
        url: ''
    }
    rules: ExtenalChainRules = {
        name: [
            COMMON_RULE
        ],
        url: [
            COMMON_RULE,
            {
                type: 'url',
                message: '请输入正确外链地址',
                trigger: 'blur'
            }
        ]
    }
    type: string = ''
    detail: any = {}
    get isAdd() {
        return this.type === 'add'
    }
    show(type, data) {
        this.isShow = true
        this.type = type
        if (!this.isAdd) {
            this.formData.name = data.name
            this.formData.url = data.url
            this.detail = data
        } else {
            this.formData.name = ''
            this.formData.url = ''
        }
    }
    confirm() {
        const validateForm: any = this.$refs.validateForm
        validateForm.validate((valid) => {
            if (valid) {
                const params: any = {
                    ...this.formData,
                    isUrl: true,
                    isPage: true,
                    icon: 'cw-icon weops-lian-jie',
                    key: this.isAdd ? this.$random(5) : this.detail.key,
                    auth: [
                        {
                            key: 'checkAuth',
                            value: false,
                            label: '查看',
                            type: 'check'
                        }
                    ]
                }
                params.id = uuid()
                this.$emit('handle-external-chain', params, this.type)
                this.cancel()
            }
        })
    }
    cancel() {
        this.isShow = false
        const validateForm: any = this.$refs.validateForm
        validateForm.resetFields()
    }
    changeVisible(val) {
        this.isShow = val
    }
}
