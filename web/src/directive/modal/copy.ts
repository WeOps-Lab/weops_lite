import Vue from 'vue'
const copy = {
    bind(el, { value }) {
        el.$value = value
        el.handler = () => {
            if (!el.$value) {
                // 值为空的时候，给出提示
                Vue.prototype.$warn('无复制内容')
                return
            }
            // 动态创建 textarea 标签
            const textarea = document.createElement('textarea')
            // 将该 textarea 设为 readonly 防止 iOS 下自动唤起键盘，同时将 textarea 移出可视区域
            textarea.readOnly = Boolean('readonly')
            textarea.style.position = 'absolute'
            textarea.style.left = '-9999px'
            // 将要 copy 的值赋给 textarea 标签的 value 属性
            textarea.value = el.$value
            // 将 textarea 插入到 body 中
            document.body.appendChild(textarea)
            // 选中值并复制
            textarea.select()
            const result = document.execCommand('Copy')
            if (result) {
                Vue.prototype.$success('复制成功')
            }
            document.body.removeChild(textarea)
        }
        // 绑定点击事件
        el.addEventListener('click', el.handler)
    },
    // 当传进来的值更新的时候触发
    componentUpdated(el, { value }) {
        el.$value = value
    },
    // 指令与元素解绑的时候，移除事件绑定
    unbind(el) {
        el.removeEventListener('click', el.handler)
    }
}

// export default copy

export default (Vue) => {
    Vue.directive('copy', copy)
}
