import { Component, Vue, Watch } from 'vue-property-decorator'
import { frameRouter, menuList } from '@/router/frameRouter'
@Component({
    name: 'bread-crumb'
})
export default class BreadCrumb extends Vue {
    menuList: any[] = []
    parentMenus: any[] = []
    nextRoute: string = ''
    get subTitle() {
        return this.$route.query?.subTitle || this.$route.query?.ip
    }
    get dynamicRoutes() {
        return this.$store.state.menu?.dynamicRoutes
    }
    @Watch('$route', {
        immediate: true,
        deep: true
    })
    on$routeChange() {
        this.getBreadcrumb()
    }
    getBreadcrumb() {
        const meta = this.$route.meta
        if (!meta?.parentIds) {
            this.menuList = []
            return false
        }
        const allRoutes = frameRouter.concat(this.dynamicRoutes)
        const formPage = this.$route.query?.formPage
        const menus = [formPage || meta.parentIds[0], this.$route.name]
        this.menuList = menus.map(item => {
            return allRoutes.find(row => row.name === item)
        })
        const parent = meta.parentIds[0]
        const fn = (menu: any) => {
            return menu?.children?.some((child: any) => child.id === parent)
        }
        const parentMenus: any[] = []
        const addMenu = (menu: any) => {
            const { name, id } = menu
            parentMenus.push({
                name,
                id
            })
        }
        menuList.forEach(menu => {
            if (fn(menu)) {
                addMenu(menu)
            } else {
                const current = (menu?.children || []).find((item: any) => fn(item))
                if (current) {
                    addMenu(menu)
                    addMenu(current)
                }
            }
        })
        this.parentMenus = parentMenus
    }
    getTitle(item: any) {
        if (this.$route.query['subName']) {
            return item.meta.title.replace('新增', '编辑')
        }
        return item?.meta?.title
    }
    toLink(item: any) {
        if (item.name === this.$route.name) {
            return false
        }
        this.$router.push({
            name: item.name
        })
    }
    toPrev() {
        let preRoute = this.$route.meta?.preRoute
        if (!preRoute?.name) {
            preRoute = this.menuList.at(-2)
        }
        this.$router.push({
            name: preRoute?.name,
            query: preRoute?.query
        })
    }
}
