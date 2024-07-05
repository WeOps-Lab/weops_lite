import { Vue, Component } from 'vue-property-decorator'
import DrawerComponent from '../comDrawer/index.vue'
import ResetPassword from './resetPassword.vue'

@Component({
    components: {
        DrawerComponent,
        ResetPassword
    }
})
export default class PersonalInfo extends Vue {
    isShow: boolean = false
    isEdit: boolean = false
    rawFormData: any = ''
    formData = {
        id: '',
        username: '',
        display_name: '',
        email: ''
    }
    formRules = {
        display_name: [
            {
                regex: /^[\u4e00-\u9fa5]+$/,
                message: '必须为中文',
                trigger: 'blur'
            }
        ]
    }
    isInfoLoading: boolean = false
    pageLoading: boolean = false

    get user() {
        return this.$store.state.permission.user
    }

    show() {
        this.formData.id = this.user.user_info?.sub
        this.isShow = true
        this.getUserInfo(this.formData.id)
    }

    updateFormData() {
        this.isEdit = true
    }

    async onFormSubmit() {
        this.$refs.validateForm.validate((valid) => {
            if (valid) {
                this.editUser()
            }
        })
    }

    async getUserInfo(id) {
        this.pageLoading = true
        try {
            const res = await this.$api.UserManageMain.getUserInfo({ id })
            const { data, message, result } = res
            if (!result) {
                return this.$error(message)
            }
            this.formData.username = data.username
            this.formData.display_name = data.lastName
            this.formData.email = data.email
            this.rawFormData = { ...this.formData }
        } finally {
            this.pageLoading = false
        }
    }

    async editUser() {
        this.isInfoLoading = true
        const params = {
            id: this.formData.id,
            lastName: this.formData.display_name,
            email: this.formData.email
        }
        const res = await this.$api.UserManageMain.editUserInfo(params)
        if (!res.result) {
            this.$error(res.message)
        } else {
            this.$success('修改成功!')
            this.isEdit = false
        }
        await this.$store.dispatch('GenerateNavLists1')
        this.isInfoLoading = false
    }

    onFormCancel() {
        this.formData = { ...this.rawFormData }
        const validateForm: any = this.$refs.validateForm
        validateForm.clearValidate()
        this.isEdit = false
    }

    showPasswordForm() {
        const resetPassword: any = this.$refs.resetPassword
        resetPassword.show()
    }

    beforeClose() {
        this.isEdit = false
        this.isShow = false
    }
}
