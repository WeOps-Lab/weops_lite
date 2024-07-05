<template>
    <div class="drawer-container">
        <el-drawer
            ref="drawer"
            :visible.sync="drawerVisible"
            v-bind="$attrs">
            <div class="title-slot" slot="title">
                <span class="back-icon">
                    <i class="el-icon-arrow-right" @click="handleClose"></i>
                </span>
                <span class="title-text">{{ title }}</span>
            </div>
            <!-- 主体内容 -->
            <slot name="content"></slot>
            <!-- 底部区域 -->
            <div class="footer-slot">
                <slot name="footer"></slot>
            </div>
        </el-drawer>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
