let tooltipDom

/** 鼠标移入事件 */
function handleMouseEnter(e) {
    if (!tooltipDom) {
    // 创建浮层元素
        tooltipDom = document.createElement('div')
        // 将浮层插入到body中
        document.body.appendChild(tooltipDom)
    }
    const maxWidth = 600
    let cssText = `
          max-width: ${maxWidth}px;
          overflow: auto;
          position: fixed;
          background: #262627;
          color: #fff;
          border-radius: 4px;
          line-height: 20px;
          padding: 10px;
          display: block;
          font-size: 12px;
          z-index: 99999;
          word-break: break-all;
        `
    // 根据鼠标移入位置判断浮层位于左侧还是右侧，避免遮挡
    if (window.innerWidth - e.clientX < maxWidth) {
        cssText += `right:${window.innerWidth - e.clientX}px;`
    } else {
        cssText += `left:${e.clientX + 20}px;`
    }
    // 根据鼠标移入位置判断浮层位于上方还是下方，避免遮挡
    if (window.innerHeight - e.clientY < 600) {
        cssText += `bottom:${window.innerHeight - e.clientY}px;`
    } else {
        cssText += `top:${e.clientY}px;`
    }

    tooltipDom.style.cssText = cssText
    // 浮层中的文字
    tooltipDom.innerHTML = e.currentTarget.innerText
}

function removeTooltip() {
    // 隐藏浮层
    if (tooltipDom) {
        tooltipDom.style.display = 'none'
    }
}

function bindEvent(el, bindings) {
    // 先移除上一次绑定的事件
    el.removeEventListener('mouseenter', handleMouseEnter)
    el.removeEventListener('mouseleave', removeTooltip)

    if (bindings.value === false) {
        return
    }
    // 给当前元素设置超出隐藏
    el.style.overflow = 'hidden'
    el.style.textOverflow = 'ellipsis'
    el.style.whiteSpace = 'nowrap'

    // 如果超出，绑定鼠标移入移出事件
    if (el.scrollWidth > el.offsetWidth) {
        el.addEventListener('mouseenter', handleMouseEnter)
        // 鼠标移出 将提示信息移除
        el.addEventListener('mouseleave', removeTooltip)
    }
}

export default (Vue) => {
    Vue.directive('overflow-tooltip', {
        inserted(el, bindings) {
            bindEvent(el, bindings)
        },
        componentUpdated(el, bindings) {
            bindEvent(el, bindings)
        },
        unbind() {
            removeTooltip()
        }
    })
}
