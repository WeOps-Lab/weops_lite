import { Component, Vue, Watch } from 'vue-property-decorator'
import Container from '../container/index.vue'
import PersonalInfo from '../personalInfo/index.vue'
import { mapState } from 'vuex'
import { removeItemsWithId } from '@/common/dealMenu'
@Component({
    components: {
        Container,
        PersonalInfo
    },
    computed: {
        ...mapState({
            permission: item => item.permission
        })
    }
})
export default class NavFrame extends Vue {
    renderKey: number = 0
    clickFlag: boolean = false
    activeTopNav: string = ''
    leftNavList: Array<any> = []
    title: string = this.$route.meta.title
    nav = {
        list: [],
        name: '',
        id: 'HomeFirst',
        toggle: false,
        submenuActive: false,
        title: 'WeOps',
        // 图片base64格式
        logo: ''
    }
    defaultActive: string = ''
    refreshNavKey: string = 'leftNavkey'
    ticketIconVisible = false
    defaultOpen: boolean = true // 是否展开左侧栏
    open: boolean = true // 图标控制，一直展开
    isShowTooltip: boolean = false
    get user() {
        const user = this.permission.user
        if (user.is_super) {
            this.ticketIconVisible = true
        } else {
            this.ticketIconVisible = user.menus?.includes('Ticket') && user.applications.includes('itsm')
        }
        return user
    }
    get menuList() {
        return this.permission.menuList
    }
    get ticketCount() {
        return this.permission.ticketCount
    }
    get updateCustomMenu() {
        return this.permission?.updateCustomMenu
    }
    get needLeftNav() {
        if (this.$route.name === 'Login') {
            return false
        }
        const target = this.menuList.find(item => item.id === this.activeTopNav)
        return !!(target && target.children)
    }
    get headerHight() {
        return this.$route.name === 'Login' ? '0' : '52'
    }
    @Watch('$route', {
        immediate: true,
        deep: true
    })
    @Watch('updateCustomMenu', {
        deep: true
    })
    on$routeChanged(val) {
        let routeValue = val
        // 若watch的变量updateCustomMenu，则为布尔值，即该菜单改变时处理如下
        if (typeof val === 'boolean') {
            routeValue = this.$route
        }
        if (this.clickFlag) {
            this.clickFlag = false
            this.renderKey++
        }
        this.menuList.forEach(item => {
            if (item.id === routeValue.name || (item.sonMenuIds || []).includes(routeValue.name)) {
                this.activeTopNav = item.id
                if ((item.sonMenuIds || []).includes(routeValue.name)) {
                    this.leftNavList = item.children
                }
            } else {
                if (!routeValue.meta?.parentIds) {
                    return false
                }
                const morePage = item.sonMenuIds.map(tex => routeValue.meta.parentIds.find(nev => nev === tex))
                if (!morePage.every(tex => !tex)) {
                    this.activeTopNav = item.id
                    this.leftNavList = item.children
                }
            }
        })
        this.defaultActive = this.setDefaultActive()
    }
    @Watch('leftNavList', {
        immediate: true,
        deep: true
    })
    onLeftNavListChanged(val) {
        // 超管或者分级管理员才能展示系统管理的界面[角色管理]
        if (!this.user.is_super && this.user.user_info?.preferred_username !== 'grade_admin') {
            const ONLY_ADMIN_HAS_MENUS = ['SysRole']
            removeItemsWithId(val, ONLY_ADMIN_HAS_MENUS)
        }
    }
    created() {
        if (document.body.clientWidth > 1440) {
            this.defaultOpen = true
        }
    }
    mounted() {
        this.$bus.$on('updateLogo', () => {
            this.getLogo()
        })
        this.$bus.$on('refreshNav', from => {
            this.defaultActive = this.setDefaultActive()
            this.refreshNavKey = Vue.prototype.$random(5)
            const topNav = this.menuList.find(item => item.sonMenuIds.includes(from.name) || item.sonMenuIds.includes(from.meta.activeMenu))
            if (topNav) {
                this.activeTopNav = topNav.id
                this.leftNavList = topNav.children
            }
        })
        this.getLogo()
        this.title = this.$route.meta.title
    }
    beforeDestroy() {
        this.$bus.$off('updateLogo')
    }
    checkPersonalInfo() {
        const personalInfo: any = this.$refs.personalInfo
        personalInfo.show()
    }
    setDefaultActive() {
        if (this.$route.meta.hasOwnProperty('parentIds')) {
            if (this.$route.meta.activeMenu) {
                return this.$route.meta.activeMenu
            } else {
                const activeMenuId = sessionStorage.getItem('activeMenuId')
                if (activeMenuId) {
                    return JSON.parse(activeMenuId)
                }
            }
        }
        return this.$route.name
    }
    outLogin() {
        this.$confirm('是否退出登录', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            center: true
        }).then(() => {
            sessionStorage.clear()
            document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/;'
            localStorage.removeItem('loginToken')
            this.$store.commit('setLoginStatus')
            this.$keycloak.logoutFn()
        })
    }
    handleSelect(id, item) {
        this.nav.id = id
    }
    getLogo() {
        this.$api.Server.getLogo({}, {
            cancelWhenRouteChange: false
        }).then(res => {
            if (res.result) {
                this.nav.logo = res.data.value
            }
        })
    }
    changeTopNav(item) {
        if (item.isUrl) {
            window.open(item.url, '_blank')
        } else {
            this.activeTopNav = item.id
            if (!item.children) {
                this.clickFlag = true
                this.$router.push({
                    name: this.activeTopNav
                })
                return false
            }
            this.leftNavList = item.children
            if (this.leftNavList.every(item => item.isUrl)) {
                return false
            }
            this.$router.push({
                name: this.findFirstNonUrlId(this.leftNavList)
            })
        }
    }
    findFirstNonUrlId(arr) {
        for (const item of arr) {
            if (item.isUrl) {
                continue
            }
            if (item.children && item.children.length > 0) {
                const childResult = this.findFirstNonUrlId(item.children)
                if (childResult !== null) {
                    return childResult
                }
            } else {
                return item.id
            }
        }
        return null
    }
    goHome() {
        this.$router.push('/')
        this.nav.name = this.$route.meta.title
    }
    handleToggle(v) {
        this.nav.toggle = v
    }
    // beforeNavChange(item) {
    //     const result = this.findItemById(this.leftNavList, item)
    //     return !result.isUrl
    // }
    // findItemById(arr, id) {
    //     for (const item of arr) {
    //         if (item.id === id) {
    //             return item
    //         }
    //         if (item.children) {
    //             const found = this.findItemById(item.children, id)
    //             if (found) {
    //                 return found
    //             }
    //         }
    //     }
    //     return null
    // }
    // 点击菜单
    handleNavItemClick(item) {
        if (item.isUrl) {
            window.open(item.url, '_blank')
        } else {
            this.clickFlag = true
            if (this.$route.name !== item.id) {
                this.nav.name = item.name
                sessionStorage.setItem('activeMenuId', JSON.stringify(item.id))
                this.$router.push({
                    name: item.id,
                    params: item.params || {}
                })
            }
        }
    }
    handleIconCLick() {
        this.open = !this.open
    }
    // 内容超出，显示文字提示内容
    onMouseOver() {
        const tag = this.$refs['strRef']
        const parentWidth = tag.parentNode.offsetWidth // 获取元素父级可视宽度
        const contentWidth = tag.offsetWidth // 获取元素可视宽度
        this.isShowTooltip = contentWidth <= parentWidth
    }
}
