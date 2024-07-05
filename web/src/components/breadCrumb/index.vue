<template>
    <div
        class="breadcrumb-container"
        v-if="menuList.length > 1">
        <i class="el-icon-back icon-arrows-left" @click="toPrev"></i>
        <ul>
            <li
                v-for="item in parentMenus"
                :key="item.id"
                v-if="parentMenus.length && menuList.length">
                {{ item.name }}
                <i class="el-icon-arrow-right" style="font-size: 12px;"></i>
            </li>
            <li
                :key="index"
                v-for="(item,index) in menuList">
                <span
                    :class="[menuList.length - 1 > index && 'breadcrumb-active']"
                    @click="toLink(item)">
                    {{ getTitle(item) }}
                </span>
                <i class="el-icon-arrow-right"
                    v-if="menuList.length - 1 > index"></i>
            </li>
        </ul>
        <span
            class="sub-title"
            v-if="subTitle">
            -- {{ subTitle }}
        </span>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss">
@import "./index.scss"
</style>
