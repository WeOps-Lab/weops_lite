import { Component, Prop, Vue } from 'vue-property-decorator'

@Component({})
export default class HeaderSub extends Vue {
    @Prop({ type: String, default: '' }) title: string
    @Prop({ type: Boolean, default: false }) operationShow: boolean
    @Prop({ type: Object, default: () => ({}) }) extStyle: any
    @Prop({ type: Boolean, default: false }) isBack: boolean
    isExpand: boolean = true
    isFirst: boolean = true
    isFixed: boolean = false

    get topValue(): number {
        const breadCrumb = this.$route.meta?.breadCrumb
        return breadCrumb ? 18 : -20
    }

    activated(): void {
        this.isExpand = true
    }

    toPrev(): void {
        this.$router.go(-1)
    }

    handleScroll(): void {
        const scrollTop: number = document.querySelector('.container-content').scrollTop
        if (scrollTop > 100) {
            this.isFixed = true
            this.isExpand = false
        }
        if (scrollTop === 0) {
            this.isFixed = false
            if (this.isFirst) {
                this.isExpand = true
            }
        }
        if (this.isFirst) this.isFirst = !this.isFirst
    }
}
