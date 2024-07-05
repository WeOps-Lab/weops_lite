import { Component, Prop, Vue } from 'vue-property-decorator'
import ComTable from '@/components/comTable/index.vue'

@Component({
    name: 'drawer-component',
    components: {
        ComTable
    }
})
export default class DrawerComponent extends Vue {
    @Prop({
        type: String,
        default: () => '标题'
    })
    title: string

    @Prop({
        type: Boolean,
        default: () => false
    })
    visible: boolean

    get drawerVisible() {
        return this.visible
    }
    set drawerVisible(val) {
        // 如果组件引用时没有配置beforeClose这个属性，则组件要加changeVisible这个方法去关闭这个抽屉
        this.$emit('changeVisible', val)
    }
    handleClose() {
        const drawer: any = this.$refs.drawer
        if (drawer.beforeClose) {
            drawer.beforeClose()
            return
        }
        this.drawerVisible = false
    }
}
