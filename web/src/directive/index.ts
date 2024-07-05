import confirm from './modal/confirm'
// 统一处理，
// const methods = [
//     confirm
// ]
const install = function(Vue) {
    Vue.prototype.$CWConfirm = confirm.install
}

export default install
