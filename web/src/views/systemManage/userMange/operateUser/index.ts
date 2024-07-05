import { Vue, Component } from 'vue-property-decorator'
import { OperateUserRules, OperateUserFormData } from '@/common/types/systemManage/userMange'
import { COMMON_RULE } from '@/common/constants'

@Component({
    name: 'operate-user'
})
export default class OperateUser extends Vue {
    visible: boolean = false
    loading: boolean = false
    userInfo: any = {}
    type: string = ''
    formData: OperateUserFormData = {
        username: '',
        lastName: '',
        email: '',
        password: '',
        confirmPassword: ''
    }
    rules: OperateUserRules = {
        username: [
            COMMON_RULE
        ],
        lastName: [
            COMMON_RULE
            // {
            //     validator: (rule, value, callback) => {
            //         if (!/^$|^[\u4e00-\u9fa5]+$/.test(value)) {
            //             callback(new Error('必须是中文'))
            //         } else {
            //             callback()
            //         }
            //     },
            //     trigger: 'blur'
            // }
        ],
        password: [
            COMMON_RULE
        ],
        confirmPassword: [
            COMMON_RULE,
            {
                validator: (rule, value, callback) => {
                    if (value !== this.formData.password) {
                        callback(new Error('两次输入密码不一致'))
                    } else {
                        callback()
                    }
                },
                trigger: 'blur'
            }
        ]
    }

    show(type, data) {
        this.visible = true
        this.type = type
        if (this.type === 'edit') {
            this.userInfo = data
            this.formData.username = data.username
            this.formData.lastName = data.lastName
            this.formData.email = data.email
        }
    }
    close() {
        this.visible = false
        const validateUserForm: any = this.$refs.validateUserForm
        validateUserForm.resetFields()
    }
    confirm() {
        const validateUserForm: any = this.$refs.validateUserForm
        validateUserForm.validate((valid) => {
            if (valid) {
                let url = 'createUser'
                let params: any = {
                    username: this.formData.username,
                    lastName: this.formData.lastName,
                    email: this.formData.email,
                    password: this.formData.password
                }
                if (this.formData.email) params.email = this.formData.email
                if (this.type !== 'add') {
                    url = 'editUser'
                    params = {
                        id: this.userInfo.id,
                        lastName: this.formData.lastName,
                        email: this.formData.email
                    }
                }
                this.loading = true
                this.$api.UserManageMain[url](params).then(res => {
                    if (!res.result) {
                        this.$error(res.message)
                        return false
                    }
                    this.$success(`${this.type === 'add' ? '新增' : '编辑'}用户成功!`)
                    this.$emit('refreshList')
                    // this.$store.dispatch('getAllUserList')
                    this.close()
                }).finally(() => {
                    this.loading = false
                })
            }
        })
    }
    closeDialog() {
        const validateUserForm: any = this.$refs.validateUserForm
        validateUserForm.clearValidate()
        validateUserForm.resetFields()
    }
}
