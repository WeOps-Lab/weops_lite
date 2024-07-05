// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import '@/assets/componentLibrary/demand-import'
// 完整引入element-ui
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// 几何图
import * as Echarts from 'echarts'
// 引用API文件
import api from './api/index'
// 公共方法
import './controller/func/common'
// 统一样式引入
import './assets/index'
// 引入自定义方法
const Dire:any = require('./directive')
// 引入自定义组件
import Component from './components/index'
// vuex
import store from './store/index'
import globalMixin from './common/mixins/global'
import 'jquery'
// const copy:any = require('./directive/modal/copy')
import copy from './directive/modal/copy'
import cwMessage from './prototype/message'
import uploader from 'vue-simple-uploader'
import btnPermission from './directive/modal/btn-permissions'
import overflowTooltip from './directive/modal/overflow-tooltip'
import './assets/icon/bk_icon_font/cw-icon'
import './assets/icon/bk_icon_font/style.css'
import Keycloak from '@dsb-norge/vue-keycloak-js'


Vue.use(ElementUI)
Vue.use(uploader)
// @ts-ignore
Vue.use(Echarts)
Vue.use(Dire)
Vue.use(copy)
Vue.use(btnPermission)
Vue.use(overflowTooltip)
Vue.use(Component)
Vue.prototype.$message = cwMessage
Vue.prototype.$echarts = Echarts
// 将API方法绑定到全局
Vue.prototype.$http = axios
Vue.prototype.$api = api
const headTheme = 'light' // 选择 light 或 blue
Vue.prototype.headTheme = headTheme

// 应用CMDB依赖
Vue.prototype.$copy = function(val) {
    if (!val) return {}
    return JSON.parse(JSON.stringify(val))
}
Vue.prototype.$apply = function(data) {
    return (<any>Object).assign({}, data, data)
}
Vue.prototype.$deepClone = function(val) {
    if (!val) return {}
    const a: any = {}
    a.o = val
    return JSON.parse(JSON.stringify(a.o))
}

Vue.prototype.$t = function(val) {
    return val
}
// 在template中使用可选链
Vue.prototype.$optionalChaining = (obj, ...rest) => {
    let tmp = obj
    for (const key in rest) {
        const name = rest[key]
        tmp = tmp?.[name]
    }
    if (tmp === 0) return tmp
    else return tmp || '--'
}
// 时间戳与时间互相转换
Vue.prototype.$stampToTime = (timeStamp) => {
    const date = new Date(timeStamp)
    const year = date.getFullYear()
    const month = date.getMonth() + 1
    const day = date.getDate()
    const clockTime = date.toString().split(' ')[4]
    return year + '/' + (month < 10 ? '0' + month : month) + '/' + (day < 10 ? '0' + day : day) + ' ' + clockTime
}

// 混入
Vue.mixin(globalMixin);

// 自动导入子应用中的main.js文件
// @ts-ignore
const appFiles = require.context('@/projects', true, /\/main$/)
appFiles.keys().forEach(key => {
    appFiles(key)
})

/* eslint-disable no-new */

const initApp = () => new Vue({
    el: '#app',
    router,
    store,
    components: {App},
    data() {
        return {
            website: '我是全局变量'
        }
    },
    template: '<App/>'
})

if (process.env.USE_MOCK) {
    // mock模式不需要登录
    initApp()
} else {
    Vue.use(Keycloak, {
        init: {
          onLoad: 'login-required',
          checkLoginIframe: false
        },
        config: {
          url: window.KEYCLOAK_URL,
          realm: window.KEYCLOAK_REALM,
          clientId: window.KEYCLOAK_UI_CLIENT_ID
        },
        onReady: (keycloak) => {
            initApp()
        },
        onInitError:(err)=>{
            console.log('初始化失败===',err);
        }
    })
}
