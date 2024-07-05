// initial state
import { menuList, subsMenuList } from '@/router/frameRouter'
import { getMenuIdsAndOperateIds } from '@/common/dealMenu'
import vue from 'vue'

import api from '@/api/index'
const state = {
    navLists: [],
    addNavLists: [],
    user: {},
    menuList: [],
    completeDynamicRoute: false,
    ticketCount: 0,
    activationMenu: [],
    updateCustomMenu: false
}
// 遍历 projects 目录下的所有文件和子目录
// @ts-ignore
const files = require.context('@/projects', true, /\.\/[^/]+\/.*/)
const hasCommonFolder = (fileName) => {
    return files.keys().some(key => key.indexOf(`/${fileName}/`) !== -1)
}

function handleMenuList(userInfo) {
    const handleNeedMenuList = handleActivationMenu(userInfo, 'custom')
    const userMenus = userInfo.menus
    return userInfo.is_super ? handleNeedMenuList : setMenuPurview(handleNeedMenuList, userMenus)
}

function handleActivationMenu(userInfo, type) {
    let customMenu = JSON.parse(JSON.stringify(menuList))
    // 若weops_menu自定义菜单选择是默认，则使用menulist内置菜单
    const weopsMenu = userInfo?.weops_menu
    if (type === 'custom' && weopsMenu && weopsMenu.length) {
        customMenu = weopsMenu
        if (hasCommonFolder('common')) {
            // @ts-ignore
            const commonFiles = require.context('@/projects', true, /\.ts$/)
            const module = commonFiles('./common/common/dynamicMenus.ts')
            if (module?.default) {
                module.default.dealDynamicMenus(JSON.parse(JSON.stringify(menuList)), customMenu)
            }
        }
    }
    handleAllMenus(customMenu)
    const handleNeedMenuList = handleBelongModule(userInfo.applications, JSON.parse(JSON.stringify(customMenu)))
    return handleNeedMenuList
}

function handleBelongModule(moduleInfo, menuList) {
    let newMenuList = menuList
    newMenuList.forEach(item => {
        if (item.children) {
            item.children.forEach(nev => {
                if (nev.children) {
                    nev.children = nev.children.filter(tex => !tex.belongModule || (tex.belongModule && moduleInfo.includes(tex.belongModule)))
                    if (nev.children.length === 0) {
                        nev.needDel = true
                    }
                }
            })
            item.children = item.children.filter(tex => (!tex.belongModule && !tex.needDel) || (tex.belongModule && moduleInfo.includes(tex.belongModule)))
        }
    })
    newMenuList = newMenuList.filter(item => !item.belongModule || (item.belongModule && moduleInfo.includes(item.belongModule))).filter(item => !item.children || (item.children && item.children.length))
    if (!moduleInfo.includes('repository')) {
        newMenuList = newMenuList.filter(item => item.id !== 'lore')
    }
    return newMenuList
}

function setMenuPurview(list, purviewList) {
    list.forEach(item => {
        if (item.children) {
            item.children = setMenuPurview(item.children, purviewList)
        }
        item.purview = !item.sonMenuIds.every(tex => !purviewList.find(nev => nev === tex))
    })
    return list.filter(item => item.purview)
}

function handleAllMenus(list) {
    list.forEach(item => {
        item.sonMenuIds = [item.id]
        for (const k in subsMenuList) {
            if (subsMenuList[k].includes(item.id)) {
                item.belongModule = k
            }
        }
        if (item.children) {
            handleAllMenus(item.children)
            getSonMenuId(item.sonMenuIds, item.children)
        }
    })
}

function getSonMenuId(ids, list) {
    list.forEach(item => {
        if (item.children) {
            getSonMenuId(ids, item.children)
        } else {
            ids.push(item.id)
        }
    })
}

// 降序排列
function compare(p) {
    return function(m, n) {
        const a = m[p]
        const b = n[p]
        return a - b
    }
}
// getters
const getters = {
    addNavLists: () => {
        return state.addNavLists
    },
    navLists: () => {
        return state.navLists.sort(compare('sort'))
    },
    getUser: () => {
        return state.user
    }
}

// mutations
const mutations = {
    setNavLists(state, lists) {
        state.addNavLists = lists
        state.navLists = lists
    },
    setUser(state, user) {
        state.user = user
    },
    setMenuList(state, lists) {
        state.menuList = lists
    },
    setDynamicRoute(state, value) {
        state.completeDynamicRoute = value
    },
    setDynamicMenus(state, value) {
        state.dynamicMenus = value
    },
    setTicketCount(state, value) {
        state.ticketCount = value
    },
    setActivationMenu(state, value) {
        state.activationMenu = value
    },
    setCustomMenuStatus(state) {
        state.updateCustomMenu = !state.updateCustomMenu
    },
    setLoginStatus(state) {
        state.user = {}
        state.ticketCount = 0
        state.menuList = []
        state.activationMenu = []
    }
}

// actions
const actions = {
    async GenerateNavLists1({commit}) {
        setTimeout(() => {
            vue.prototype.$bus.$emit('setAppLoading', true)
        }, 0)
        const promise = new Promise((resolve, reject) => {
            api.User.homeInfo().then(async res => {
                if (res.result) {
                    const { data: userData } = res
                    if (userData.user_info?.preferred_username !== 'grade_admin' && !userData.is_super) {
                        // 非超管，或者非grade_admin不能看到角色管理菜单
                        if (userData?.menus_permissions) {
                            const targetIndex = userData.menus_permissions.findIndex(item => item === 'SysRole_view')
                            userData.menus_permissions.splice(targetIndex, 1)
                        }
                    }
                    const homeInfo = getMenuIdsAndOperateIds(userData?.menus_permissions || [])
                    userData.menus = homeInfo.menus_ids // 查看权限的菜单id
                    // 处理只有查看权限，没操作权限的菜单
                    const operateSet = new Set(homeInfo.operate_ids.map(item => item.menuId))
                    const operateIds = []
                    userData.menus.forEach(item => {
                        if (!operateSet.has(item)) {
                            operateIds.push({
                                menuId: item,
                                operate_ids: []
                            })
                        }
                    })
                    userData.operate_ids = [...homeInfo.operate_ids, ...operateIds] // 操作权限的id
                    userData.applications = []
                    userData.chname = userData.user_info?.name || '--'
                    sessionStorage.setItem('loginInfo', JSON.stringify(userData))
                    window['$store'].commit('setLoginInfo', userData)
                    commit('setUser', { ...userData })
                    commit('setMenuList', handleMenuList(userData))
                    commit('setActivationMenu', handleActivationMenu(userData, ''))
                    if (userData.applications.includes('chat_ops') && hasCommonFolder('common')) {
                        // @ts-ignore
                        const commonFiles = require.context('@/projects', true, /\.ts$/)
                        const module = commonFiles('./common/common/loadBot.ts')
                        if (module?.default) {
                            await module.default.loadChatBot()
                        }
                    }
                    resolve(userData)
                } else {
                    reject(res.message)
                }
            }).finally(() => {
                setTimeout(() => {
                    vue.prototype.$bus.$emit('setAppLoading', false)
                }, 0)
            })
        })
        return promise
    },
    updateMenuList({commit}, userInfo) {
        commit('setMenuList', handleMenuList(userInfo))
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
