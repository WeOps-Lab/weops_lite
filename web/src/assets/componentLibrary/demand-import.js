import Vue from 'vue'
import { Message } from 'element-ui'

export const $error = (message, delay = 3000) => {
    if (message === 'cancelRequest') {
        return false
    }
    Message({
        message,
        duration: delay,
        type: 'error'
    })
}

export const $success = (message, delay = 3000) => {
    Message({
        message,
        duration: delay,
        type: 'success'
    })
}

export const $info = (message, delay = 3000) => {
    Message({
        message,
        duration: delay,
        type: 'info'
    })
}

export const $warn = (message, delay = 3000) => {
    Message({
        message,
        duration: delay,
        type: 'warning',
        showClose: true
    })
}

// Vue prototype mount
Vue.prototype.$error = $error
Vue.prototype.$success = $success
Vue.prototype.$info = $info
Vue.prototype.$warn = $warn
