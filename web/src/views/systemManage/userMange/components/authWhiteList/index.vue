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
                        <menu-tab
                            v-if="!onlyChooseUser"
                            :panels="panels"
                            v-model="active"
                            type="capsule"
                            @change="changeMenu">
                        </menu-tab>
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
                        :columns="onlyChooseUser ? userColumns : groupColumns"
                        @select="handleSelect"
                        @select-all="handleAllSelect"
                        @page-change="handlePageChange"
                        @page-limit-change="handleLimitChange">
                    </com-table>
                </div>
                <div class="selection-container">
                    <p>已选择（共<span>{{initChooseAdmin ? allSelected.length + 1 : allSelected.length}}</span>条）<span class="clear" @click="handleClear">清空</span></p>
                    <ul>
                        <li v-if="initChooseAdmin">
                            超管(admin)
                            <span>用户</span>
                        </li>
                        <li v-for="item in allSelected" :key="item.id + item.type">
                            {{ item.type === 'role' ? item.role_name : `${item.chname || '--'}(${item.bk_username})` }}
                            <span>{{ item.type === 'role' ? '角色' : '用户' }}</span>
                            <i class="el-icon-close" style="font-size: 12px;" @click="handleRemove(item)"></i>
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
