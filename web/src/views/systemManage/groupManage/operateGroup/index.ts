import { Vue, Component } from 'vue-property-decorator'
import { RulesForm } from '@/common/types/systemManage/groupManage'
import { COMMON_RULE } from '@/common/constants'
@Component
export default class OperateGroup extends Vue {
    visible: boolean = false
    loading: boolean = false
    roleInfo: any = ''
    type: string = ''
    formData = {
        group_name: '',
        id: ''
    }
    rules: RulesForm = {
        group_name: [
            COMMON_RULE
        ]
    }
    get title() {
        if (this.type === 'add') {
            return '新增组织'
        }
        if (this.type === 'edit') {
            return '编辑组织'
        }
        return '添加子组'
    }
    show(type, data) {
        const orgin = data?.data
        this.visible = true
        this.type = type
        this.formData.group_name = ''
        if (type === 'addSub') {
            this.formData.id = orgin?.id
        }
        if (['edit'].includes(this.type)) {
            this.roleInfo = orgin
            this.formData.group_name = orgin.name
            if (this.type === 'edit') {
                this.formData.id = orgin.id
            }
        }
    }
    close() {
        this.visible = false
    }
    confirm() {
        const organizationValidateForm: any = this.$refs.organizationValidateForm
        organizationValidateForm.validate((valid) => {
            if (valid) {
                let url = ''
                const params: any = {}
                if (['add', 'addSub'].includes(this.type)) {
                    url = 'addGroup'
                    params.group_name = this.formData.group_name
                    if (this.type === 'addSub') {
                        params.parent_group_id = this.formData.id
                    }
                } else {
                    url = 'editGroup'
                    params.id = this.formData.id
                    params.group_name = this.formData.group_name
                }
                this.loading = true
                this.$api.GroupManage[url](params).then(res => {
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
                this.close()
            }
        })
    }
    closeDialog() {
        // Object.assign(this.$data, this.$options.data.call(this))
        const organizationValidateForm: any = this.$refs.organizationValidateForm
        organizationValidateForm.clearValidate()
    }
}
