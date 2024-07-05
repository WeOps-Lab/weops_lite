import { Vue, Component } from 'vue-property-decorator'
@Component({
    name: 'logo-set'
})
export default class LogoSettings extends Vue {
    imgData: any = ''
    isEdit: boolean = false
    basicLoading: boolean = false
    reShow: boolean = true
    src: string = 'data:image/png;base64,'
    file: any = [
        {
            name: 'image.png',
            status: 'done',
            url: ''
        }
    ]
    fileData: any = ''
    get powerParams() {
        return {
            id: this.$route.name,
            type: 'SysSetting_logo_change'
        }
    }
    created() {
        this.getLogo()
    }
    async uploadLogo() {
        if (!this.$BtnPermission(this.powerParams) || !this.fileData) {
            return false
        }
        const file = this.fileData
        const fileTypes = ['.jpg', '.png', '.jpeg', '.svg']
        const filePath = file.origin.name
        if (file.origin.size > 1048576 * 10) {
            this.$warn('图片大小请不要超过10M')
            return
        }
        // 当括号里面的值为0、空字符、false 、null 、undefined的时候就相当于false
        if (filePath) {
            let isNext = false
            const fileEnd = filePath.substring(filePath.lastIndexOf('.'))
            for (let i = 0; i < fileTypes.length; i++) {
                if (fileTypes[i] === fileEnd) {
                    isNext = true
                    break
                }
            }
            if (!isNext) {
                file.value = ''
                return false
            }
        } else {
            return false
        }
        const fileData = new FormData()
        fileData.append('file', this.fileData.origin)
        this.basicLoading = true
        try {
            const res = await this.$api.Server.updateLogo(fileData)
            if (res.result) {
                this.$success('上传成功')
                // this.$store.commit('changeLogo')
                this.$bus.$emit('updateLogo')
            } else {
                this.$error('上传失败')
            }
            this.fileData = ''
        } finally {
            this.basicLoading = false
        }
    }
    initLogo() {
        if (!this.$BtnPermission(this.powerParams)) {
            return false
        }
        this.$confirm('确定恢复默认吗？', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            center: true
        }).then(async() => {
            try {
                const res = await this.$api.Server.resetlogo()
                if (res.result) {
                    this.$success('恢复默认成功!')
                    this.$bus.$emit('updateLogo')
                    this.getLogo()
                } else {
                    this.$error('恢复默认失败!')
                }
                return true
            } catch (e) {
                return false
            }
        })
    }
    getLogo() {
        this.reShow = false
        this.$api.Server.getLogo().then(res => {
            if (res.result) {
                this.file = [
                    {
                        name: 'image.png',
                        status: 'done',
                        url: 'data:image/png;base64,' + res.data.value
                    }
                ]
                this.reShow = true
                this.$store.commit('changeLogo')
            }
        })
    }
    handleUpload(el) {
        this.reShow = false
        // element-ui数据格式不一样，更改
        if (!el.hasOwnProperty('fileObj')) {
            el.fileObj = {}
        }
        el.fileObj.origin = el.file

        this.fileData = el.fileObj
        this.toBase64(el.fileObj.origin).then(res => {
            this.file = [
                {
                    name: 'image.png',
                    status: 'done',
                    url: res
                }
            ]
            this.$nextTick(() => {
                this.reShow = true
            })
        })
    }
    toBase64(file) {
        const reader = new FileReader()
        reader.readAsDataURL(file)
        return new Promise((resolve, reject) => {
            reader.onload = function(e) {
                if (this.result) {
                    resolve(this.result)
                } else {
                    reject(new Error('转换预览图片失败'))
                }
            }
        })
    }
}
