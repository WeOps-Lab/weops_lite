import { Vue, Component, Prop } from 'vue-property-decorator'
import DrawerComponent from '@/components/comDrawer/index.vue'
@Component({
    name: 'import-resource',
    components: {
        DrawerComponent
    }
})
export default class ImportResource extends Vue {
    @Prop({
        type: String,
        default: () => ''
    })
    modelId: string

    visible: boolean = false
    loading: boolean = false
    formData: any = {
        fileList: []
    }
    formDataV2 = {}

    deleteFile(index) {
        this.formData.fileList.splice(index, 1)
    }
    handleUpload(data) {
        if ((data.file.size / (1024 * 1024)) > 20) {
            this.$error('文件大小不能超过20M')
            return
        }
        this.formData.fileList = [data.file]
    }
    showDialog() {
        this.visible = true
        this.formData.fileList = []
        this.formDataV2 = this.$copy(this.formData)
    }
    beforeCloseDialog() {
        const flag = this.$compareFormData(this.formData, this.formDataV2)
        if (!flag) {
            this.$confirm('放弃将导致未保存信息丢失', '是否放弃本次操作？', {
                center: true
            }).then(() => {
                this.visible = false
            })
            return
        }
        this.visible = false
    }
    handleDownload() {
        this.$api.AssetData.downloadTemplate({ id: this.modelId }).then((res) => {
            const blob = new Blob([res], { type: '.xlsx' })
            // 通过创建a标签实现
            const link = document.createElement('a')
            link.href = window.URL.createObjectURL(blob)
            // 对下载的文件命名
            link.download = `${this.modelId}资产模板.xlsx`
            document.body.appendChild(link)
            link.click()
            document.body.removeChild(link)
        })
    }
    async handleSubmit() {
        this.loading = true
        try {
            const paramsBody = new FormData()
            paramsBody.append('file', this.formData.fileList[0])
            const params = {
                id: this.modelId,
                body: paramsBody
            }
            const { result, message } = await this.$api.AssetData.importInst(params)
            if (!result) {
                return this.$error(message)
            }
            this.visible = false
            this.$success('已成功导入')
            this.$emit('on-success', params)
        } finally {
            this.loading = false
        }
    }
}
