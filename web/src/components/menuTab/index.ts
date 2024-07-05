import { Panel } from '@/types/index'
import * as _ from 'lodash'
import { EleResize } from '@/common/esresize'
import { Component, Prop, Model, Vue, Watch } from 'vue-property-decorator'

@Component({})
export default class NavHeader extends Vue {
    @Model('change', { type: String }) value: string
    @Prop({ type: Array, default: [] }) panels: any
    @Prop({ type: String, default: '' }) activePanel: string
    @Prop({ type: Boolean, default: false }) border: boolean
    // type类型为 card,line,text,capsule
    @Prop({ type: String, default: 'card' }) type: string
    @Prop({ type: Boolean, default: false }) hideArrow: boolean
    @Prop({ type: Function, default: null }) beforeLeave: null
    active: string = ''
    showOperation: boolean = false
    clientWidth: number = 0
    totalWidth: number = 0
    showTabsCount: number = 0
    unoccupied: number = 0
    moveX: number = 0

    @Watch('activePanel')
    activePanelChange(val) {
        this.active = val
    }

    mounted() {
        this.active = this.activePanel || (this.panels[0] && this.panels[0].name)
        const dom = this.$refs.container
        const changeOperation = () => {
            this.clientWidth = dom?.clientWidth
            const liEle = dom.querySelectorAll('li')
            this.totalWidth = 0
            for (let i = 0; i < liEle.length; i++) {
                const distanceWidth = liEle.length - 1 === i ? 0 : 8
                this.totalWidth += liEle[i].clientWidth + distanceWidth
            }
            this.showOperation = !this.hideArrow && this.totalWidth > this.clientWidth
            // 可视区域能放入多少个元素 = 可视区域的宽度 循环全部tab,合计宽度当超过内容宽度
            setTimeout(() => {
                let isCalculated = false
                const contentWidth = dom.querySelector(`.${this.type}-content`).clientWidth
                let computedWidth = 0
                for (let i = 0; i < liEle.length; i++) {
                    const distanceWidth = liEle.length - 1 === i ? 0 : 8
                    computedWidth += liEle[i].clientWidth + distanceWidth
                    if (computedWidth > contentWidth && !isCalculated) {
                        this.showTabsCount = i
                        isCalculated = true
                        // 被遮挡tab元素的可见部分的宽度 = 可见区域的宽度 - 显示完全的tab宽度
                        this.unoccupied = contentWidth - computedWidth + liEle[i].clientWidth + 8
                    }
                }
            }, 0)
        }
        this.$nextTick(() => changeOperation())
        if (dom) {
            EleResize.on(dom, _.throttle(() => changeOperation(), 500))
        }
    }
    toClick(item: Panel) {
        if (item.disabled) {
            return
        }
        if (this.beforeLeave) {
            const func: any = this.beforeLeave
            func({
                that: this,
                current: this.active,
                target: item.name
            })
            return
        }
        this.active = item.name
        this.$emit('change', this.active)
        this.$emit('click', item)
    }
    next() {
        this.$nextTick(() => {
            const contentWidth = this.$refs.container.querySelector(`.${this.type}-content`).clientWidth
            // 可视区域 < 滚动区域（滚动区域大于可视区域才可以移动）
            // 移动距离 + 可视区域 = 滚动区域的宽度（上一次的宽度，当点击时才是实际宽度）< 滚动区域
            if (contentWidth < this.totalWidth && this.moveX + contentWidth < this.totalWidth) {
                // this.moveX为0减去空余空间的宽度
                // this.moveX += this.moveX ? this.width : this.width - this.unoccupied
                this.moveX += 50
                this.translateX(this.moveX)
            }
        })
    }
    previous() {
        if (this.moveX > 0) {
            this.moveX -= 50
            this.translateX(this.moveX)
        }
    }
    translateX(x) {
        this.moveX = x < 0 ? 0 : x
        const dom = this.$refs.container.querySelector('ul')
        dom.style.transform = `translateX(-${this.moveX}px)`
    }
}
