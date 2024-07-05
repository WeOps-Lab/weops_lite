import { Vue, Component, Prop } from 'vue-property-decorator'
import DrawerComponent from '@/components/comDrawer/index.vue'
import { TARGET_BIND_LIST } from '@/common/constants/assetManage/modelManage'
@Component({
    components: {
        DrawerComponent
    }
})
export default class connectOperation extends Vue {
    @Prop({
        type: Array,
        default: () => []
    })
    modelList: Array<any>
    @Prop({
        type: String,
        default: () => ''
    })
    modelId: string
    @Prop({
        type: Array,
        default: () => []
    })
    connectTypeList: Array<any>

    hostDetail: any = ''
    isShow: boolean = false
    formData = {
        src_model_id: '',
        dst_model_id: '',
        asst_id: '',
        mapping: '',
        model_asst_id: ''
    }
    formDataV2 = {}
    rules = {
        src_model_id: [
            {
                required: true,
                message: '必填项',
                trigger: 'blur'
            }
        ],
        dst_model_id: [
            {
                required: true,
                message: '必填项',
                trigger: 'blur'
            }
        ],
        asst_id: [
            {
                required: true,
                message: '必填项',
                trigger: 'blur'
            }
        ],
        mapping: [
            {
                required: true,
                message: '必填项',
                trigger: 'blur'
            }
        ],
        name: [
            {
                required: true,
                validator: (rule, value, callback) => this.validateName(rule, value, callback),
                trigger: 'blur'
            }
        ]
    }
    loading: boolean = false
    protocolList = [
        {
            id: 'rdp',
            name: 'RDP'
        },
        {
            id: 'ssh',
            name: 'SSH'
        }
    ]
    targetBindList = TARGET_BIND_LIST
    type: string = ''
    relDetail: any = ''
    sourceModelDetail: any = null
    targetModelDetail: any = null
    connectTypeDetail: any = null
    connectTypeMap = {
        belong: '常用与组织或管理层级的连接',
        group: '设备部件和整体之间的连接',
        bk_mainline: '系统内置类型，仅用于业务拓扑的节点关系，仅限系统使用',
        run: '程序与操作系统之间的连接',
        connect: '常用与网络设备之间的连接',
        default: '资产节点之间的连接',
        install_on: '数据库/中间库等与主机之间的连接'
    }
    get isAdd() {
        return this.type === 'add'
    }
    get assoName() {
        if (this.connectTypeDetail && this.sourceModelDetail && this.targetModelDetail) {
            return `${this.sourceModelDetail.model_name} ${this.connectTypeDetail.name} ${this.targetModelDetail.model_name}`
        }
        return ''
    }
    validateName(rule, value, callback) {
        if (!this.assoName) {
            callback(new Error('必填项'))
        } else {
            callback()
        }
    }
    getIconUrl(tex) {
        try {
            return require(`@/assets/svg/model/${tex.icn || 'cc-default_默认'}.svg`)
        } catch (e) {
            return require('@/assets/svg/model/cc-default_默认.svg')
        }
    }
    changeConnectType() {
        this.getConnectTypeDetail()
    }
    exchangeSource() {
        const target = JSON.parse(JSON.stringify(this.formData.src_model_id))
        this.formData.src_model_id = JSON.parse(JSON.stringify(this.formData.dst_model_id))
        this.formData.dst_model_id = target
        this.getModelDetail()
    }
    changeSourceModel() {
        if (!this.formData.src_model_id) {
            this.formData.dst_model_id = this.modelId
        }
        this.getModelDetail()
    }
    changeTargetModel() {
        if (!this.formData.dst_model_id) {
            this.formData.src_model_id = this.modelId
        }
        this.getModelDetail()
    }
    show(type, data) {
        for (const key in this.formData) {
            this.formData[key] = ''
        }
        this.type = type
        this.isShow = true
        this.formData.src_model_id = this.modelId
        if (!this.isAdd) {
            this.relDetail = data
            for (const key in data) {
                if (this.formData.hasOwnProperty(key)) {
                    this.formData[key] = data[key]
                }
            }
        }
        this.getModelDetail()
        this.getConnectTypeDetail()
        this.formDataV2 = JSON.parse(JSON.stringify(this.formData))
    }
    getConnectTypeDetail() {
        this.connectTypeDetail = this.connectTypeList.find(item => item.id === this.formData.asst_id)
    }
    getModelDetail() {
        this.sourceModelDetail = null
        this.targetModelDetail = null
        for (const item of this.modelList) {
            if (!this.sourceModelDetail) {
                this.sourceModelDetail = item.list.find(tex => tex.model_id === this.formData.src_model_id)
            }
            if (!this.targetModelDetail) {
                this.targetModelDetail = item.list.find(tex => tex.model_id === this.formData.dst_model_id)
            }
            // 如果两者都找到了，提前退出循环
            if (this.sourceModelDetail && this.targetModelDetail) {
                break
            }
        }
    }
    confirm() {
        this.$refs.validateForm.validate().then(validator => {
            const params = this.formData
            params.model_asst_id = `${this.formData.src_model_id}_${this.formData.asst_id}_${this.formData.dst_model_id}`
            if (!this.isAdd) {
                params.id = this.relDetail.id
            }
            this.save(params)
        })
    }
    save(params) {
        this.loading = true
        const url = this.isAdd ? 'createAssociation' : 'updateAssociation'
        this.$api.ModelManage[url](params).then(res => {
            if (!res.result) {
                this.$error(res.message)
                return false
            }
            this.$success(`${this.isAdd ? '新增' : '编辑'}模型关系成功`)
            this.isShow = false
            this.$emit('refreshRel')
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
}
