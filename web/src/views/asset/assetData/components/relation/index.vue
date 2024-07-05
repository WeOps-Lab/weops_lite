<template>
    <drawer-component
        title="关联关系"
        :size="800"
        :visible="visible"
        destroy-on-close
        custom-class="common-dialog-wrapper"
        :before-close="beforeCloseDialog">
        <div slot="content" class="content-box common-dialog-wrapper-main">
            <asso-info
                :group-list="groupList"
                :connect-type-list="connectTypeList"
                :model-info-list="modelInfoList"
                :user-list="userList"
                :property-list="propertyList"
                :inst-info="instInfo" />
        </div>
        <div slot="footer">
            <el-button
                size="small"
                @click="beforeCloseDialog">
                关闭
            </el-button>
        </div>
    </drawer-component>
</template>

<script lang="ts" >
    import { Component, Vue, Prop } from 'vue-property-decorator'
    import DrawerComponent from '@/components/comDrawer/index.vue'
    import AssoInfo from '../assoInfo/index/index.vue'
@Component({
    components: {
        DrawerComponent,
        AssoInfo
    }
})
export default class Relation extends Vue {
    @Prop({
        type: Array,
        default: () => []
    })
    groupList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    userList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    connectTypeList: Array<any>
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
        type: Object,
        default: () => ({})
    })
    instInfo: any

    visible: boolean = false

    beforeCloseDialog() {
        this.visible = false
    }
    show() {
        this.visible = true
    }
}
</script>
