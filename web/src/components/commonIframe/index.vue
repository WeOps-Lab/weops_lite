<template>
    <div class="report-page">
        <div style="height: 100%;" v-loading="loading">
            <iframe id="frame-box" @load="loadFrame" :src="url"></iframe>
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
