<template>
    <div id="confirm">
    </div>
</template>

<script>
    export default {
        /**
         * 参考: https://www.iviewui.com/components/modal
         * @param {string|number} title 弹框标题
         * @param {string|number} content 弹框内容
         * @param {string} type 弹出框类型 可选值有：'edit'、'del'
         * @param {string} okText 确认按钮文字内容
         * @param {string} cancelText 取消按钮文字内容
         * @param promiseStatus 构造promise函数，释放两个出口
         */
        name: 'confirm'
    }
</script>
