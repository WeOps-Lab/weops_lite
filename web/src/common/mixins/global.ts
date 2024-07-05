export default {
    data() {
        return {
            tableMaxHeight: 0,
            pageOccupiedHeight: 314 // 默认的表格高度
        }
    },
    created() {
        this.calculateMaxHeight()
        window.addEventListener('resize', this.calculateMaxHeight)
    },
    destroyed() {
        window.removeEventListener('resize', this.calculateMaxHeight)
    },
    methods: {
        calculateMaxHeight() {
            this.tableMaxHeight = window.innerHeight - this.pageOccupiedHeight
        }
    }
}
