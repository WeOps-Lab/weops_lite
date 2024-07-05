<template>
    <drawer-component
        :title="title"
        :visible="visible"
        :size="850"
        custom-class="common-dialog-wrapper"
        :before-close="handleClose">
        <div slot="content"
            class="common-dialog-wrapper-main">
            <div class="auth-white-list">
                <div class="list-container">
                    <div class="header">
                        <el-input
                            clearable
                            style="width: 300px;"
                            :placeholder="'请输入关键字搜索'"
                            :suffix-icon="'el-icon-search'"
                            v-model="searchValue"
                            size="small"
                            @clear="handleSearch"
                            @change="handleSearch">
                        </el-input>
                    </div>
                    <com-table
                        class="mt20 table-container"
                        ref="userTable"
                        :data="dataList"
                        :pagination="pagination"
                        v-loading="loading"
                        :columns="roleColumns"
                        @select="handleSelect"
                        @select-all="handleAllSelect"
                        @page-change="handlePageChange"
                        @page-limit-change="handleLimitChange">
                    </com-table>
                </div>
                <div class="selection-container">
                    <p>已选择（共<span>{{allSelected.length}}</span>条）<span class="clear" @click="handleClear">清空</span></p>
                    <ul>
                        <li v-for="item in allSelected" :key="item.id + item.type">
                            <span :class="['cw-icon',item.role_type === 'group' ? 'weops-zu-zhi-jue-se' : 'weops-ge-ren-jue-se']"></span>
                            {{ item.name }}
                            <span>{{ item.role_type === 'group' ? '组织角色' : '个人角色' }}</span>
                            <i class="el-icon-close" style="font-size: 12px;" v-if="item.role_type !== 'group'" @click="handleRemove(item)"></i>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <template slot="footer">
            <el-button
                class="mr10"
                :type="'primary'"
                :loading="isConfirm"
                size="small"
                @click="handleConfirm()">
                确认
            </el-button>
            <el-button
                :disabled="isConfirm"
                size="small"
                @click="handleClose()">
                取消
            </el-button>
        </template>
    </drawer-component>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss">
@import "./index.scss"
</style>
