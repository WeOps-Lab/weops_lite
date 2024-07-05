import { Vue, Component } from 'vue-property-decorator'
import DrawerComponent from '../comDrawer/index.vue'
import { COMMON_RULE } from '@/common/constants'

@Component({
    components: {
        DrawerComponent
    }
})
export default class PersonalInfo extends Vue {
    isShow: boolean = false
    isPsdLoading: boolean = false
    passwordFormData = {
        password: '',
        confirmPassword: ''
    }
    passwordRules = {
        password: [
            COMMON_RULE
        ],
        confirmPassword: [
            {
                validator: (rule, value, callback) => {
                    if (value === '') {
                        callback(new Error('必填项'))
                    } else if (value !== this.passwordFormData.password) {
                        callback(new Error('两次输入密码不一致!'))
                    } else {
                        callback()
                    }
                },
                trigger: 'blur'
            }
        ]
    }

    get user() {
        return this.$store.state.permission.user
    }

    show() {
        this.isShow = true
    }

    onPasswordSubmit() {
        const validatePsdForm: any = this.$refs.validatePsdForm
        validatePsdForm.validate((valid) => {
            if (valid) {
                this.isPsdLoading = true
                const params = {
                    id: this.user.user_info?.sub,
                    password: this.passwordFormData.password
                }
                this.$api.UserManageMain.resetUserPassword(params).then(res => {
                    if (!res.result) {
                        this.$error(res.message)
                        return false
                    }
                    this.$success('重置密码成功!')
                    this.onPasswordCancel()
                }).finally(() => {
                    this.isPsdLoading = false
                })
            }
        })
    }

    onPasswordCancel() {
        this.passwordFormData.password = ''
        this.passwordFormData.confirmPassword = ''
        const validatePsdForm: any = this.$refs.validatePsdForm
        validatePsdForm.resetFields()
        this.isShow = false
    }

    changeVisible(val) {
        this.isShow = val
        this.onPasswordCancel()
    }
}
