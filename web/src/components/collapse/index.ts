import { Vue, Component, Prop } from 'vue-property-decorator'
@Component({
    name: 'collapse'
})
export default class Collapse extends Vue {
    @Prop({
        type: Array,
        default: () => ([
            {
                label: '分组1',
                id: 'group1',
                isExpand: true
            },
            {
                label: '分组2',
                id: 'group2',
                isExpand: true
            }
        ])
    })
    collapseList: Array<any>
}
