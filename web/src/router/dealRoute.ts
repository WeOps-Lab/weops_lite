import store from '@/store'

export default class DealRoute {
    public static async dealRouterByMenu(to: any, next: any) {
        await store.dispatch('getOtherMenus')
        next({ ...to, replace: true })
    }
}
