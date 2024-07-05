import Vue from 'vue'
import Confirm from './confirm.vue'

const ConfirmBox = Vue.extend(Confirm)

Confirm.install = function(options) {
    const instance = new ConfirmBox({
        data: options
    }).$mount()

    document.body.appendChild(instance.$el) // 把生成的提示的dom插入body中

    return instance.confirm() // 执行confirm函数，初始化promise
}

export default Confirm
