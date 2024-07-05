<template>
    <el-dialog
        width="600px"
        :visible.sync="visible"
        theme="primary"
        :close-on-click-modal="false"
        title="选择图标"
    >
        <div class="icon-show-list">
            <el-tooltip v-for="(item, index) in iconList" :key="index" :content="item.describe" placement="bottom">
                <div
                    class="top-middle"
                    :class="['icon-item', activeIndex === index && 'active-icon']"
                    @click="selectIcon(item, index)"
                >
                    <img :src="require(`@/assets/svg/model/${item.url}.svg`)" />
                </div>
            </el-tooltip>
        </div>
        <template slot="footer">
            <el-button
                :type="'primary'"
                size="small"
                @click="cancel"
            >
                确认
            </el-button>
            <el-button
                :type="'default'"
                size="small"
                @click="cancel"
            >
                取消
            </el-button>
        </template>
    </el-dialog>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
