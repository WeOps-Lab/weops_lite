<template>
    <div class="cw-login-dialog" v-if="isShow">
        <div class="cw-login-wrapper">
            <iframe id="iframeBox" :src="loginUrl" scrolling="no" border="0" :width="width" :height="height" @load="onLoad"></iframe>
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss">
@import "./index.scss"
</style>
