import { Vue, Component, Prop } from 'vue-property-decorator'
@Component({})
export default class PageExplanation extends Vue {
    @Prop({ type: String, default: '' }) title: string
    @Prop({ type: String, default: '' }) content: string
}
