import { Component, Emit, Vue } from 'vue-property-decorator'
@Component
export default class SelectIcon extends Vue {
    visible: boolean = false
    iconList: {
        url: string,
        describe: string
    }[] = []
    activeIndex: number = 15
    selectIconUrl: string = ''
    mounted() {
        this.iconList = this.$getSvgIcon().map(item => {
            return {
                url: item,
                describe: item.split('_')[1]
            }
        }).filter(item => item.url && item.describe)
    }
    cancel() {
        this.setIcon()
        this.visible = false
    }
    selectIcon(item, index) {
        this.activeIndex = index
    }
    show(icon) {
        this.visible = true
        if (icon) {
            const index = this.iconList.findIndex(item => item.url === icon)
            if (index !== -1) {
                this.activeIndex = index
            }
        }
    }
    @Emit('setIcon')
    setIcon() {
        this.selectIconUrl = this.iconList[this.activeIndex].url
        return this.selectIconUrl
    }
}
