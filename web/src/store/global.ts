import api from '@/api/index'

const state = {
    appName: '',
    winHeight: '',
    loginInfo: {},
    leftMenuActive: '',
    userList: [],
    breadCrumbs: {},
    funcMenus: {},
    privilege_version: '',
    application_topology: '',
    leftMenus: [],
    reloadLeftMenu: false,
    toggleIstrue: '',
    bizList: []
}
const getters = {
    appName: state => state.appName,
    winHeight: state => state.winHeight,
    loginInfo: state => state.loginInfo,
    version: state => {
        return state.loginInfo.version ? state.loginInfo.version : 'v3.2.x'
    },
    username: state => {
        return state.loginInfo.username ? state.loginInfo.username : ''
    },
    v: state => state.loginInfo.cc_api_version, // 用于区分导入导出 v4 和 v3 版本
    userList: state => state.userList,
    userMap: state => {
        let m = {}
        if (state.userList) {
            state.userList.forEach(user => {
                m[user.english_name] = user
            })
        }
        return m
    },
    breadCrumbs: state => state.breadCrumbs,
    application_topology: state => {
        return state.loginInfo.application_topology
    },
    privilege_version: state => {
        return state.loginInfo.privilege_version
    },
    leftMenus: state => state.leftMenus,
    reloadLeftMenu: state => state.reloadLeftMenu,
    bizList: state => state.bizList,
}
const mutations = {
    setAppName(state, data) {
        state.appName = data
    },
    setWinHeight(state, data) {
        state.winHeight = data
    },
    setLoginInfo(state, data) {
        state.loginInfo = data
    },
    setUserList(state, data) {
        state.userList = data
    },
    setBreadCrumbs(state, data) {
        state.breadCrumbs = data
    },
    toggleIstrue(state, data) {
        state.toggleIstrue = data
    },
    setLeftMenus(state, data) {
        state.leftMenus = data
    },
    setReloadLeftMenu(state, data) {
        state.reloadLeftMenu = data
    },
    setBizList(state, data) {
        state.bizList = data
    }
}
const actions = {
    async getLoginInfo({ commit }) {
        const res = await api.login.login_info()
        if (!res.result) return console.error(res.message)
        commit('setLoginInfo', res.data)
    },
    async getUserList({ commit }) {
        const res = await api.cc.user.get_user_list()
        if (!res.result) return console.error(res.message)
        commit('setUserList', res.data)
    },
    async getBizList({ commit }, params) {
        const res = await api.monitorAlarm.getBizList()
        if (!res.result) return console.error(res.message)
        commit('setBizList', res.data)
    }
}

export default {
    state,
    getters,
    mutations,
    actions
}
