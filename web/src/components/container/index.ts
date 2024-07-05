import BreadCrumb from '@/components/breadCrumb/index.vue'
import { Component, Prop, Vue } from 'vue-property-decorator'

@Component({
    components: {
        BreadCrumb
    }
})
export default class MainContainer extends Vue {
    @Prop({ type: Object, default: () => ({}) }) user: any

    get routerKey() {
        return this.$route.params.renderKey
    }

    get menuList() {
        return this.$store.getters.cacheRouter
    }
}
