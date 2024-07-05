<template>
    <div id="main-container">
        <bread-crumb></bread-crumb>
        <keep-alive :include="menuList">
            <router-view v-bind="$attrs"></router-view>
        </keep-alive>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
