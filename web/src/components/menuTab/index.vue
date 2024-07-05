<template>
    <div ref="container" :class="['menu-type-container', `${type}-container`]">
        <i v-if="showOperation" class="el-icon-arrow-left" @click="previous"></i>
        <div :class="[`${type}-content`]">
            <ul>
                <li :key="index"
                    v-for="(item, index) in panels"
                    :class="[
                        type,
                        (item.name === active && 'active'),
                        ((type === 'card' && border) && 'border-li'),
                        (item.disabled && 'disable')
                    ]"
                    @click="toClick(item)">
                    <span v-if="item.tooltips && item.disabled" v-bk-tooltips="item.tooltips">{{ item.label }}</span>
                    <span v-else>{{ item.label }}</span>
                    <template v-if="item.count">
                        <span>{{ item.count }}</span>
                    </template>
                </li>
            </ul>
        </div>
        <i v-if="showOperation" class="el-icon-arrow-right" @click="next"></i>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
