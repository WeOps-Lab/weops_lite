import { Vue, Component, Prop } from 'vue-property-decorator'
import { RulesForm } from '@/common/types/systemManage/roleManage'
import { COMMON_RULE } from '@/common/constants'
@Component
export default class OperateRole extends Vue {
    @Prop({
        type: Array,
        default: () => []
    })
    roleList: Array<any>

    visible: boolean = false
    loading: boolean = false
    roleInfo: any = ''
    type: string = ''
    formData = {
        role_name: '',
        describe: '',
        superior_role: '',
        id: ''
    }
    rules: RulesForm = {
        role_name: [
            COMMON_RULE
        ],
        superior_role: [
            COMMON_RULE
        ]
    }
    get title() {
        if (this.type === 'add') {
            return '新增角色'
        } else if (this.type === 'edit') {
            return '编辑角色'
        } else {
            return '拷贝角色'
        }
    }
    show(type, data) {
        this.visible = true
        this.type = type
        this.formData.role_name = ''
        this.formData.describe = ''
        this.formData.superior_role = ''
        if (['edit', 'copy'].includes(this.type)) {
            this.roleInfo = data
            this.formData.role_name = data.name
            this.formData.describe = data.description
            this.formData.superior_role = data.superior_role
            if (this.type === 'edit') {
                this.formData.id = data.id
            }
        }
    }
    close() {
        this.visible = false
    }
    confirm() {
        const roleValidateForm: any = this.$refs.roleValidateForm
        roleValidateForm.validate((valid) => {
            if (valid) {
                let url = ''
                const params: any = {
                    name: this.formData.role_name,
                    description: this.formData.describe,
                    superior_role: this.formData.superior_role
                }
                if (['add', 'copy'].includes(this.type)) {
                    url = 'createRole'
                } else {
                    url = 'editRole'
                }
                this.loading = true
                this.$api.RoleManageMain[url](params).then(res => {
                    if (!res.result) {
                        this.$error(res.message)
                        return false
                    }
                    this.$success(`${this.title}成功!`)
                    this.$emit('refreshList')
                    this.close()
                }).finally(() => {
                    this.loading = false
                })
            }
        })
    }
    closeDialog() {
        // Object.assign(this.$data, this.$options.data())
        const roleValidateForm: any = this.$refs.roleValidateForm
        roleValidateForm.clearValidate()
    }
}
