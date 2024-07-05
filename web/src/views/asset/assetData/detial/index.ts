import { Component, Vue } from 'vue-property-decorator'
import { Panels } from '@/common/types'
import { ASSET_DTIAL_PANELS } from '@/common/constants/asset/assetData'
import BaseInfo from '../components/baseInfo/index.vue'
import AssoInfo from '../components/assoInfo/index/index.vue'
import AssetRecord from '../components/assetRecord/index/index.vue'
@Component({
    components: {
        BaseInfo,
        AssoInfo,
        AssetRecord
    }
})
export default class AssetDetial extends Vue {
    loading: boolean = false
    panels: Array<Panels> = ASSET_DTIAL_PANELS
    active: string = 'baseInfo'
    groupList: Array<any> = []
    connectTypeList: Array<any> = []
    modelInfoList: Array<any> = []
    propertyList: Array<any> = []
    userList: Array<any> = []

    created() {
        this.getConfigInfo()
    }

    getConfigInfo() {
        this.loading = true
        Promise.all([this.getGroups(), this.getUserList(), this.getConnectTypeList(), this.getModelInfoList(), this.getModelAttrList()]).finally(() => {
            this.loading = false
        })
    }

    handleTabClick(tab) {
        // console.log(tab)
    }

    async getConnectTypeList() {
        const { result, data } = await this.$api.ModelManage.getAssotypeList()
        if (!result) {
            return false
        }
        this.connectTypeList = data.map(item => {
            return {
                id: item.asst_id,
                label: item.asst_name,
                name: `${item.asst_name}(${item.asst_id})`
            }
        })
    }
    async getModelInfoList() {
        const { result, message, data } = await this.$api.ModelManage.getModel()
        if (!result) {
            return this.$error(message)
        }
        this.modelInfoList = data
    }
    async getModelAttrList() {
        const params = {
            id: this.$route.query.modelId
        }
        const { result, message, data } = await this.$api.ModelManage.getModelAttrList(params)
        if (!result) {
            return this.$error(message)
        }
        this.propertyList = data
    }
    async getUserList() {
        const { result, message, data } = await this.$api.UserManageMain.getAllUsers()
        if (!result) {
            return this.$error(message)
        }
        this.userList = data.map(item => {
            return {
                name: item.lastName,
                id: item.username
            }
        })
    }
    async getGroups() {
        this.loading = true
        const res = await this.$api.GroupManage.getGroups()
        const { result, message, data } = res
        if (!result) {
            return this.$error(message)
        }
        this.groupList = this.convertArray(data)
    }
    convertArray(arr) {
        const result = []
        arr.forEach(item => {
            const newItem = {
                value: item.id,
                label: item.name
            }
            if (item.subGroups && !!item.subGroups.length) {
                newItem.children = this.convertArray(item.subGroups)
            }
            result.push(newItem)
        })
        return result
    }
}
