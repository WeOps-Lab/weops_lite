import _ from 'lodash'
import { Vue, Component, Prop } from 'vue-property-decorator'
import ComTable from '@/components/comTable/index.vue'
import moment from 'moment'
import { Pagination, TableData } from '@/common/types'
import { AssetRecordList } from '@/common/types/asset/assetData'
import { ASSET_RECORD_COLUMNS } from '@/common/constants/asset/assetData'
import RecordDetial from '../recordDetial/index.vue'

@Component({
    name: 'asset-record',
    components: {
        ComTable,
        RecordDetial
    }
})
export default class AssetRecord extends Vue {
    @Prop({
        type: Array,
        default: () => []
    })
    modelInfoList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    propertyList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    userList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    groupList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    connectTypeList: Array<any>

    isLoading: boolean = false
    params = {
        operator: '',
        type: '',
        created_at_after: '',
        created_at_before: '',
        dateTime: [],
        page: 1,
        page_size: 20,
        model_id: this.$route.query.modelId,
        inst_id: this.$route.query.instId
    }
    typeList = []
    recordList: Array<AssetRecordList> = []
    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }
    columns: Array<TableData> = ASSET_RECORD_COLUMNS

    created() {
        this.getOperateTypeList()
        this.getLogs()
    }
    getOperator(id) {
        return this.userList.find(item => item.id === id)?.name || '--'
    }
    checkDetail(row) {
        const recordDetial: any = this.$refs.recordDetial
        recordDetial.showDialog(row, this.typeList)
    }
    getOperateType(id) {
        return this.typeList.find(item => item.id === id)?.name || '--'
    }
    searchDataByUser() {
        this.pagination.current = 1
        this.getLogs()
    }
    getRemote = _.debounce(function() {
        this.getLogs()
    }, 1000)

    searchDataByType() {
        this.pagination.current = 1
        this.getLogs()
    }
    getLogs() {
        this.params.page = this.pagination.current
        this.params.page_size = this.pagination.limit
        this.getLogsRequest()
    }
    async getOperateTypeList() {
        const res = await this.$api.AssetData.getRecordType()
        const { message, result, data } = res
        if (!result) {
            return this.$error(message)
        }
        this.typeList = Object.keys(data).map(key => ({ id: key, name: data[key] }))
    }
    async getLogsRequest() {
        try {
            this.isLoading = true
            const res = await this.$api.AssetData.getChangeRecordList(this.params)
            const { message, result, data } = res
            if (!result) {
                this.$error(message)
                this.recordList = []
                return false
            }
            this.recordList = data.data
            this.pagination.count = data.count
        } finally {
            this.isLoading = false
        }
    }
    resetSearch() {
        this.params = {
            operator: '',
            type: '',
            created_at_after: '',
            created_at_before: '',
            dateTime: [],
            page: 1,
            page_size: 20,
            model_id: this.$route.query.modelId,
            inst_id: this.$route.query.instId
        }
        this.getLogsRequest()
    }
    handlePageChange(page) {
        this.pagination.current = page
        this.getLogs()
    }
    handleLimitChange(limit) {
        this.pagination.limit = limit
        this.getLogs()
    }
    getDate(date) {
        this.pagination.current = 1
        if (!date?.length) {
            this.params.created_at_after = ''
            this.params.created_at_before = ''
        } else {
            this.params.created_at_after = moment(date[0]).format('YYYY-MM-DD HH:mm:ss')
            this.params.created_at_before = moment(date[1]).format('YYYY-MM-DD HH:mm:ss')
        }
        this.getLogs()
    }
}
