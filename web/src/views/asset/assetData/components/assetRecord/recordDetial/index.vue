<template>
    <drawer-component
        title="操作详情"
        :size="640"
        :visible="visible"
        destroy-on-close
        custom-class="common-dialog-wrapper"
        :before-close="beforeCloseDialog">
        <div slot="content" class="content-box common-dialog-wrapper-main" v-loading="loading">
            <div class="record-form">
                <ul class="description">
                    <li class="description-item" v-for="item in formData.list" :key="item.id">
                        <span class="label">
                            {{ item.label }}：
                        </span>
                        <span class="name">
                            {{ getDisplayName(item.id) }}
                        </span>
                    </li>
                </ul>
            </div>
            <com-table
                ref="table"
                :data="formData.attrList"
                :columns="formData.attrColumns"
                height="calc(100vh - 300px)"
            >
            </com-table>
        </div>
        <div slot="footer">
            <el-button
                size="small"
                @click="beforeCloseDialog">
                关闭
            </el-button>
        </div>
    </drawer-component>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
