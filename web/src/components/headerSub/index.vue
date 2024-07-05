<template>
    <div :class="['header-sub-container', isFixed && 'sub-fixed']" :style="{ ...extStyle, top: `${topValue}px` }">
        <div :class="['header-sub-title', isBack && 'pl-35']">
            <span class="header-title-icon" v-if="isBack" @click="toPrev">
                <svg class="icon" style="width: 1em; height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4756"><path d="M416 480h320v64H416l96 96-48 48-176-176 176-176 48 48-96 96z" p-id="4757"></path></svg>
            </span>
            <template v-if="title">
                {{ title }}
            </template>
            <template v-else>
                <slot name="title"></slot>
            </template>
            <span class="fr collapse" v-if="operationShow" @click="isExpand = !isExpand">
                <i :class="[isExpand ? 'weops-circle-up' : 'weops-circle-down','cw-icon']"></i>
                {{ isExpand ? '收起' : '展开' }}
            </span>
        </div>
        <template v-if="isExpand">
            <div>
                <slot name="content"></slot>
            </div>
        </template>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss">
@import "./index.scss"
</style>
