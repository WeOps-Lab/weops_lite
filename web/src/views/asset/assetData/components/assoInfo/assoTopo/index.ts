import G6 from '@antv/g6'
import { Vue, Component, Prop } from 'vue-property-decorator'
import registerFactory from '@/views/asset/assetData/components/assoInfo/utils/registerFactory/exports'
import DrawerComponent from '@/components/comDrawer/index.vue'
import BaseInfo from '@/views/asset/assetData/components/baseInfo/index.vue'
@Component({
    components: {
        DrawerComponent,
        BaseInfo
    }
})
export default class AssoTopo extends Vue {
    @Prop({
        type: Array,
        default: () => []
    })
    modelInfoList: Array<any>
    @Prop({
        type: Array,
        default: () => []
    })
    connectTypeList: Array<any>
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
        type: Object,
        default: () => ({})
    })
    instInfo: any

    graph: any = null
    loading: boolean = false
    visible: boolean = false
    topoData: any = {}
    currentModelCfg: any = {}
    isEmpty: boolean = false

    mounted() {
        registerFactory(G6, this)
        this.initGraph()
    }

    beforeDestroy() {
        if (this.graph && this.graph.destroyed) {
            this.graph.destroyed()
        }
    }

    beforeCloseDialog() {
        this.visible = false
    }
    async initGraph() {
        const container: any = this.$refs['canvasRef']
        const { clientWidth: width, clientHeight: height } = this.$el
        await this.getInstanceTopo()
        const grid = new G6.Grid()
        const minimap = new G6.Minimap({
            size: [200, 120],
            className: 'minimap',
            type: 'delegate'
        })
        this.graph = new G6.TreeGraph({
            container,
            width,
            height,
            plugins: [grid, minimap],
            fitView: true,
            minZoom: 0.1,
            modes: {
                default: [
                    'drag-canvas',
                    'zoom-canvas',
                    {
                        type: 'tooltip',
                        offset: 15,
                        formatText: function formatText(node) {
                            const re = /^(\d+)\.(\d+)\.(\d+)\.(\d+)$/
                            const showTip = `
                                    <span
                                        style="background-color: #333;
                                        padding: 5px 10px;
                                        color: #fff;
                                        border-radius: 3px;
                                        font-size: 12px;"
                                    >
                                        ${node.inst_name}
                                    </span>
                                `
                            if (re.test(node.inst_name)) {
                                if (node.inst_name.split('').length > 13) {
                                    return showTip
                                }
                                return ''
                            }
                            if (typeof node.inst_name === 'string') {
                                const res = /^[\u4e00-\u9fa5]/
                                const MAX_COUNT_LENGTH = res.test(node.inst_name) ? 8 : 13
                                return node.inst_name.split('').length > MAX_COUNT_LENGTH ? showTip : ''
                            }
                            return showTip
                        },
                        shouldUpdate: function shouldUpdate(e) {
                            return true
                        },
                        shouldBegin(e) {
                            return true
                        }
                    }
                ]
            },
            defaultNode: {
                type: 'asso-node',
                size: [170, 52]
            },
            defaultEdge: {
                type: 'cubic-horizontal',
                label: '属于',
                labelCfg: {
                    autoRotate: true,
                    position: 'center',
                    style: {
                        fill: '#B2BDCC',
                        fontSize: 8,
                        background: {
                            fill: '#fff',
                            padding: [2, 2, 2, 2],
                            radius: 2
                        },
                        opacity: 1
                    }
                }
            },
            layout: {
                type: 'mindmap',
                direction: 'H',
                dropCap: false,
                getHeight: () => {
                    return 40
                },
                getWidth: () => {
                    return 200
                },
                getSide: (node) => {
                    if (node.data.isSource) {
                        return 'right'
                    }
                    return 'left'
                }
            }
        })
        this.graph.data(this.topoData)
        this.graph.render()
        this.initEvent()
    }
    initEvent() {
        this.graph.on('node:click', this.handleExpand)
    }
    handleExpand(e) {
        const model = e.item.getModel()
        if (e.target.get('name') === 'collapse-icon') {
            model.collapsed = !model.collapsed
            this.graph.setItemState(e.item, 'collapsed', !!model.collapsed)
            this.graph.layout()
            return
        }
        this.currentModelCfg = model
        this.visible = true
    }
    async getInstanceTopo() {
        this.loading = true
        const { modelId, instId } = this.$route.query
        const params = {
            model_id: modelId || this.instInfo.modelId,
            inst_id: instId || this.instInfo.instId
        }
        try {
            const { result, message, data } = await this.$api.AssetData.getInstanceTopo(params)
            if (!result) {
                this.isEmpty = true
                return this.$error(message)
            }
            this.isEmpty = false
            const srcData = data.src_result.children.map(item => this.dealArrow(item, 'src'))
            const dstData = data.dst_result.children.map(item => this.dealArrow(item, 'dst'))
            const currentNode = this.$copy(data.src_result)
            delete currentNode.children
            const topoData = {
                ...currentNode,
                children: [...dstData, ...srcData]
            }
            this.topoData = this.dealTopoData(topoData)
        } catch {
            this.isEmpty = true
        } finally {
            this.loading = false
        }
    }
    dealArrow(data, type) {
        data.isSource = type === 'src'
        data.collapsed = true
        if (data.children?.length) {
            data.children.forEach(item => this.dealArrow(item, type))
        }
        return data
    }
    dealTopoData(data) {
        if (data.model_id) {
            const targetModel = this.modelInfoList.find(item => item.model_id === data.model_id)
            data.model_name = targetModel?.model_name || '--'
            data.icn = targetModel?.icn || 'cc-default_默认'
            data.asst_name = this.connectTypeList.find(item => item.id === data.asst_id)?.label || '--'
            data.inst_id = data._id
            data.id = data._id.toString()
        }
        if (data.children?.length) {
            data.children.forEach(item => this.dealTopoData(item))
        }
        return data
    }
}
