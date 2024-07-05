import Vuex from 'vuex'
import Vue from 'vue'
import permission from './modules/permisson'
import global from './global'
import product from './modules/product'
import menu from './modules/menu'

// @ts-ignore
Vue.use(Vuex)

const modules = {
    permission,
    global,
    product,
    menu
}

// @ts-ignore
const appFiles = require.context('@/projects', true, /\/store$/)

appFiles.keys().forEach(key => {
    const module = appFiles(key).default
    Object.keys(module).forEach(name => {
        modules[name] = module[name]
    })
})

const store: any = new Vuex.Store({
    modules,
    state: {
        routerRenderKey: 0,
        frameUrls: [],
        logoChange: 1
    },
    mutations: {
        updateRouterRenderKey(state, data) {
            state.routerRenderKey++
        },
        addUrls(state, value) {
            state.frameUrls = value
        },
        changeLogo(state, value) {
            state.logoChange++
        }
    }
})

window['$store'] = store
export default store
