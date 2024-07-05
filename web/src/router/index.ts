import Vue from 'vue'
import store from '@/store'
import Router from 'vue-router'
import { frameRouter } from './frameRouter'
import httpConfig from '@/api/axiosconfig/request'
import { findFirstUrl, findIdsWithNoChildren, hasPathInChildren, underscoreToCamelCase } from '@/common/dealMenu'

// 遇到路由重读点击报错时，取消注释解决
// const originalPush = Router.prototype.push
// Router.prototype.push = function push(location) {
//     return originalPush.call(this, location).catch(err => err)
// }

// 遍历 projects 目录下的所有文件和子目录
// @ts-ignore
const files = require.context('@/projects', true, /\.\/[^/]+\/.*/)

// 判断是否包含了 common 文件夹
const hasCommonFolder = (fileName) => {
    return files.keys().some(key => key.indexOf(`/${fileName}/`) !== -1)
}

Vue.use(Router)

// 路由切换时取消请求
const cancelRequest = async() => {
    const allRequest = httpConfig.queue.get()
    const requestQueue = allRequest.filter(request => request.cancelWhenRouteChange)
    await httpConfig.cancel(requestQueue.map(request => request.requestId))
}

// frameRouter ：参数；框架路由；不需要的话就直接注释

// 解决编程式路由往同一地址跳转时会报错的情况
const originalPush = Router.prototype.push
const originalReplace = Router.prototype.replace
// push
// @ts-ignore
Router.prototype.push = function push(location, onResolve, onReject) {
    if (onResolve || onReject) return originalPush.call(this, location, onResolve, onReject)
    return originalPush.call(this, location).catch(err => err)
}
// replace
// @ts-ignore
Router.prototype.replace = function push(location, onResolve, onReject) {
    if (onResolve || onReject) return originalReplace.call(this, location, onResolve, onReject)
    return originalReplace.call(this, location).catch(err => err)
}

const router = new Router({
    mode: 'history',
    routes: frameRouter // 替换到这里
})
const handleRouteAuthorization = async(to, from, next) => {
    const permission = store.state.permission
    if ((!permission.user || JSON.stringify(permission.user) === '{}')) {
        await store.dispatch('GenerateNavLists1')
    }
    checkRouteAccess(to, from, next)
}

function checkRouteAccess(to, from, next) {
    const permission = store.state.permission
    const isDefinedRoute = frameRouter.some(item => item.name === to?.name)
    const menuList = permission.menuList
    const defaultName = findFirstUrl(menuList)
    const ids = findIdsWithNoChildren(permission.menuList).concat(['404', '403', 'AuthPermissionFail'])
    // // 资产实例详情添加动态的parentIds，避免页面403
    if (to.name === 'AssetDetail') {
        const dynamicMenus = store.state.menu.dynamicMenus
        to.meta.parentIds = dynamicMenus.map(item => underscoreToCamelCase(item.classification_id)) || []
    }
    const isHasPermission = ids.includes(to.name) || (to?.meta?.parentIds || []).filter(r => ids.includes(r)).length || ids.includes(to?.meta?.relatedMenu)
    // 不包含在全定义路由中,即是不存在该页面
    if (!isDefinedRoute && !ids.includes(to.name)) {
        // 首页需要特殊处理,若defaultName存在,则跳转到该页面
        if ((to.fullPath === '/' || to.fullPath.includes('#iss=http')) && defaultName) {
            // 兼容keycloak登录后返回的首页url和默认的首页url'/'
            next({ name: defaultName })
            return
        }
        next({ name: '404' })
    }
    // 判断是否存在在定义的路由中,存在但没有访问权限,则isRead为false,若不在isRead为true,且跳转到404
    const isRead = isDefinedRoute ? isHasPermission : true
    if (!isRead) {
        if (to.fullPath.includes('#iss=http') && defaultName) {
            next({ name: defaultName })
            return
        }
        next({ name: '403' })
    }
    dealRouterByPermission(to, from, next)
}

function dealRouterByPermission(to, from, next) {
    const permission = store.state.permission
    const userInfo = permission.user
    const menuList = permission.menuList
    if (to.name === 'AuthPermissionFail' && menuList.length === 0) {
        next()
    } else {
        const menus = userInfo.menus || []
        // 处理自定义菜单的默认路由的逻辑
        const weopsMenu = userInfo?.weops_menu
        if (weopsMenu?.length) {
            // 若自定义菜单中不存在url='/'的数据,则默认访问第一个路由
            if (to.fullPath === '/' && !hasPathInChildren(weopsMenu, '/')) {
                const defaultName = findFirstUrl(weopsMenu)
                next({ name: defaultName })
            }
        }
        if (userInfo.is_super) {
            next()
        } else {
            // 处理非管理组用户的路由逻辑
            if (to.fullPath === '/') {
                if (menus.includes('Home')) {
                    next()
                } else {
                    // 访问的path='/'若不存在home页面,则获取第一个id
                    if (menuList.length === 0) {
                        next({name: 'AuthPermissionFail'})
                    } else {
                        const defaultName = findFirstUrl(menuList)
                        next({ name: defaultName })
                    }
                }
            }
            next()
        }
    }
}

router.beforeEach(async(to, from, next) => {
    await cancelRequest()
    const permission = store.state.permission
    const menu = store.state.menu
    const completeDynamicRoute = permission.completeDynamicRoute
    const completeLoadChildApp = menu?.completeLoadChildApp
    // 处理其他菜单 如:资产的动态和基础监控的动态菜单时,需要走以下的公共逻辑
    if (!completeDynamicRoute) {
        // @ts-ignore
        const commonFiles = require.context('@/router', true, /\.ts$/)
        const module = commonFiles('./dealRoute.ts')
        if (module?.default) {
            await module.default.dealRouterByMenu(to, next)
        } else {
            await handleRouteAuthorization(to, from, next)
        }
    } else if (!completeLoadChildApp && hasCommonFolder('common')) {
        // 处理加载外部资源子应用
        // @ts-ignore
        const commonFiles = require.context('@/projects', true, /\.ts$/)
        const module = commonFiles('./common/router/dealRoute.ts')
        if (module?.default) {
            await module.default.dealRouterByChildApp(to, from, next, router)
        } else {
            await handleRouteAuthorization(to, from, next)
        }
    } else {
        await handleRouteAuthorization(to, from, next)
    }
})

export default router
