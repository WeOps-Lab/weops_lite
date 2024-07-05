<template>
    <div class="collapse">
        <div class="collapse" v-for="item in collapseList" :key="item.id">
            <div :class="['header',!item.isExpand && 'mb20']">
                <span
                    :class="['cw-icon' ,'title-icon',item.isExpand ? 'weops-triangle-down' : 'weops-triangle-right']"
                    @click="item.isExpand = !item.isExpand">
                </span>
                <span class="title">{{ item.label }}</span>
            </div>
            <div v-show="item.isExpand" class="show-info mb20">
                <slot name="content" :collRow="item"></slot>
            </div>
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss">
@import "./index.scss"
</style>
