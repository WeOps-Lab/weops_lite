import store from '@/store/index'

export const btnPermission = {
    inserted(el, { value }) {
        const user = store.state.permission.user
        if (user.is_super) {
            return false
        }
        const target = user.operate_ids?.find(item => item.menuId === value.id)
        if (target) {
            const flag = target.operate_ids.find(item => item === value.type || item === value.secondAuth)
            if (flag) {
                return false
            }
        }
        const isBtn = [...el.classList].find(item => item === 'bk-button')
        const isTextBtn = [...el.classList].find(item => item === 'bk-button-text')
        if (isBtn && !isTextBtn) {
            el.style.backgroundColor = '#fafafa'
            el.style.borderColor = '#e6e6e6'
        }
        el.style.cursor = 'pointer'
        el.style.color = '#ccc'
        el.onmouseenter = (e) => {
            removeCustomNode()
            const img = document.createElement('img')
            img.id = 'permission-img'
            img.src = require('@/assets/svg/lock.svg')
            img.classList.add('custom-img')
            img.style.left = (e.pageX + 10) + 'px'
            img.style.top = (e.pageY + 5) + 'px'
            document.body.appendChild(img)
            const tip = document.createElement('div')
            document.body.appendChild(tip)
            tip.innerText = '当前操作无权限，请联系管理员'
            tip.id = 'permission-tip'
            tip.classList.add('custom-tip')
            const content = document.createElement('div')
            content.classList.add('custom-content')
            tip.appendChild(content)
            const tail = document.createElement('div')
            tail.classList.add('custom-tail')
            const leftTarget = window.innerWidth - (el.getBoundingClientRect().left + el.offsetWidth / 2) < tip.offsetWidth / 2
            const topTarget = el.getBoundingClientRect().top > tip.offsetHeight + 15
            if (topTarget) {
                tip.style.top = el.getBoundingClientRect().top - tip.offsetHeight - 10 + 'px'
                tail.classList.add('custom-tail-bottom')
            } else {
                tip.style.top = el.getBoundingClientRect().top + tip.offsetHeight + 20 + 'px'
                tail.classList.add('custom-tail-top')
            }
            tip.appendChild(tail)
            if (leftTarget) {
                tip.style.left = el.getBoundingClientRect().left + el.offsetWidth - tip.offsetWidth + 'px'
                tail.style.left = '90%'
            } else {
                tip.style.left = el.getBoundingClientRect().left + (el.offsetWidth - tip.offsetWidth) / 2 + 'px'
            }
        }
        el.onmousemove = (e) => {
            const img = document.getElementById('permission-img')
            if (img) {
                img.style.left = (e.pageX + 10) + 'px'
                img.style.top = (e.pageY + 5) + 'px'
            }
        }
        el.onmouseleave = () => {
            removeCustomNode()
        }
    }
}

function removeCustomNode() {
    if (document.getElementById('permission-tip')) {
        document.getElementById('permission-tip').remove()
    }
    if (document.getElementById('permission-img')) {
        document.getElementById('permission-img').remove()
    }
}

export default (Vue) => {
    Vue.directive('permission', btnPermission)
}
