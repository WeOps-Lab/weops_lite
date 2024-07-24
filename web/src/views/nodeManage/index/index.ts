import ComTable from '@/components/comTable/index.vue'
import { Vue, Component } from 'vue-property-decorator'
import PageExplanation from '@/components/pageExplanation/index.vue'
import AddInstance from '../components/addInstance/index.vue'
import HandMovement from '../components/handMovement/index.vue'
import { Pagination, TableData } from '@/common/types'
import { NODE_MANAGE_COLUMNS } from '@/common/constants/nodeManage/nodeManage'
@Component({
    name: 'node-manage',
    components: {
        ComTable,
        PageExplanation,
        AddInstance,
        HandMovement
    }
})
export default class NodeManage extends Vue {
    tableLoading: boolean = false
    dataList: Array<any> = []
    modelList: Array<any> = []
    columns: Array<TableData> = NODE_MANAGE_COLUMNS
    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    fieldKey: string = 'node_name'
    fieldValue: string = ''
    sidecarStatus: string = ''
    statusList: Array<any> = []
    attrList: Array<any> = [
        {id: 'node_name', name: '实例名'},
        {id: 'model_id', name: '资产模型'},
        {id: 'node_ip', name: 'IP地址'}
    ]
    get user() {
        return this.$store.state.permission.user
    }
    created() {
        this.initPage()
    }
    changeFieldKey() {
        this.fieldValue = ''
    }
    changeFieldvaule() {
        this.handlerIconClick()
    }
    showModelName(id) {
        return this.modelList.find(item => item.model_id === id)?.model_name || '--'
    }
    showStatus(id) {
        return this.statusList.find(item => item.value === id)?.text || '--'
    }
    getStatusStyle(id) {
        const styleMaps = {
            'not_installed': 'info',
            'abnormal': 'warning',
            'normal': 'success'
        }
        return styleMaps[id] || 'danger'
    }
    async createNode(list) {
        this.tableLoading = true
        const params = {
            body: list
        }
        const res = await this.$api.NodeManage.createNodes(params)
        const { result, message } = res
        if (!result) {
            this.tableLoading = false
            return this.$error(message)
        }
        this.getNodeList()
    }
    filterChange(val) {
        this.sidecarStatus = Object.values(val)[0]?.[0] || ''
        this.getNodeList()
    }
    initPage() {
        this.tableLoading = true
        Promise.all([this.getNodeList('init'), this.getAllModelList(), this.getNodeEnum()]).finally(() => {
            this.tableLoading = false
        })
    }
    async getAllModelList() {
        const res = await this.$api.ModelManage.getModel()
        const { result, message, data } = res
        if (!result) {
            this.modelList = []
            return this.$error(message)
        }
        this.modelList = data.filter(item => item.model_type !== 'credential')
    }
    async getNodeEnum() {
        const res = await this.$api.NodeManage.getNodeEnum()
        const statusList = []
        const { result, message, data } = res
        if (!result) {
            this.statusList = []
            return this.$error(message)
        }
        for (const key in data.sidecar_status) {
            statusList.push({
                text: data.sidecar_status[key],
                value: key
            })
        }
        this.statusList = statusList
        const target = this.columns.find(item => item.key === 'sidecar_status')
        if (target) {
            target.filters = this.statusList
        }
        this.$nextTick(() => {
            const comTable: any = this.$refs.comTable
            comTable.updateColumns(this.columns)
        })
    }
    addNode() {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: 'NodeManage_manage'
        })) {
            return false
        }
        const addInstance: any = this.$refs.addInstance
        const nodeInfo = {
            selection: [],
            modelList: this.modelList
        }
        addInstance.show(nodeInfo)
    }
    handleInstall() {
        const handMovement: any = this.$refs.handMovement
        const nodeInfo = {
            selection: [],
            modelList: this.modelList
        }
        handMovement.show(nodeInfo)
    }
    handlerIconClick() {
        this.pagination.current = 1
        this.getNodeList()
    }
    refreshList() {
        this.getNodeList()
    }
    deleteNode(row) {
        if (!this.$BtnPermission({
            id: this.$route.name,
            type: 'NodeManage_manage'
        })) {
            return false
        }
        this.$confirm('请确定已经手动卸载控制器？', {
            center: true
        }).then(() => {
            this.confirmDelete(row.id)
        })
    }
    async confirmDelete(id) {
        this.tableLoading = true
        const res = await this.$api.NodeManage.deleteNode({id})
        if (!res.result) {
            this.tableLoading = false
            return this.$error(res.message)
        }
        this.$success('删除成功!')
        if (this.pagination.current > 1 && this.dataList.length === 1) {
            this.pagination.current--
        }
        this.getNodeList()
    }
    getParams() {
        const params = {
            page: this.pagination.current,
            page_size: this.pagination.limit,
            sidecar_status: this.sidecarStatus
        }
        params[this.fieldKey] = this.fieldValue
        return params
    }
    async getNodeList(type?) {
        this.tableLoading = true
        try {
            const params = this.getParams()
            const res = await this.$api.NodeManage.getNodeList(params)
            if (!res.result) {
                return this.$error(res.message)
            }
            this.dataList = res.data.data
            this.pagination.count = res.data.count
        } finally {
            this.tableLoading = type === 'init'
        }
    }
    handlePageChange(val) {
        this.pagination.current = val
        this.getNodeList()
    }
    limitChange(val) {
        this.pagination.current = 1
        this.pagination.limit = val
        this.getNodeList()
    }
}
