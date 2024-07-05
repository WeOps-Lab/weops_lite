import _ from 'lodash'
import { Vue, Component } from 'vue-property-decorator'
import PageExplanation from '@/components/pageExplanation/index.vue'
import ComTable from '@/components/comTable/index.vue'
import moment from 'moment'
import { Pagination, TableData } from '@/common/types'
import { LogList } from '@/common/types/systemManage/logManage'
import { LOG_COLUMNS } from '@/common/constants/systemManage/logManage'

@Component({
    name: 'log-manage',
    components: {
        PageExplanation,
        ComTable
    }
})
export default class LogManage extends Vue {
    isLoading: boolean = false

    params = {
        operator: '',
        operate_type: '',
        create_time_after: '',
        create_time_before: '',
        dateTime: [],
        page: 1,
        page_size: 10
    }

    typeList = []

    logList: Array<LogList> = []

    pagination: Pagination = {
        current: 1,
        count: 0,
        limit: 20
    }

    columns: Array<TableData> = LOG_COLUMNS

    created() {
        this.getOperateTypeList()
        this.getLogs()
    }
    getOperateType(id) {
        return this.typeList.find(item => item.id === id)?.name || '--'
    }
    searchDataByUser() {
        this.pagination.current = 1
        this.getRemote()
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
        const res = await this.$api.Server.getOperateType()
        const { message, result, data } = res
        if (!result) {
            return this.$error(message)
        }
        this.typeList = Object.keys(data).map(key => ({ id: key, name: data[key] }))
    }
    async getLogsRequest() {
        try {
            this.isLoading = true
            const res = await this.$api.Server.getLogs(this.params)
            const { message, result, data } = res
            if (!result) {
                this.$error(message)
                this.logList = []
                return false
            }
            this.logList = data.data
            this.pagination.count = data.count
        } finally {
            this.isLoading = false
        }
    }
    resetSearch() {
        this.params = {
            operator: '',
            operate_type: '',
            create_time_after: '',
            create_time_before: '',
            page: 1,
            page_size: 10,
            dateTime: []
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
            this.params.create_time_after = ''
            this.params.create_time_before = ''
        } else {
            this.params.create_time_after = moment(date[0]).format('YYYY-MM-DD HH:mm:ss')
            this.params.create_time_before = moment(date[1]).format('YYYY-MM-DD HH:mm:ss')
        }
        this.getLogs()
    }
}
