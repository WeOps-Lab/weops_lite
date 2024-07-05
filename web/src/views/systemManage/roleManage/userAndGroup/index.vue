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
                            :panels="panels"
                            :active-panel="active"
                            type="capsule"
                            @change="changeMenu">
                        </menu-tab>
                        <el-input
                            v-if="active === 'user'"
                            clearable
                            style="width: 300px;"
                            :placeholder="'请输入关键字搜索'"
                            :suffix-icon="'el-icon-search'"
                            size="small"
                            v-model="searchValue"
                            @clear="handleSearch"
                            @change="handleSearch">
                        </el-input>
                    </div>
                    <com-table
                        v-if="active === 'user'"
                        class="mt20 table-container"
                        ref="userTable"
                        :data="dataList"
                        :pagination="pagination"
                        v-loading="loading"
                        :columns="userColumns"
                        @select="handleSelect"
                        @select-all="handleAllSelect"
                        @page-change="handlePageChange"
                        @page-limit-change="handleLimitChange">
                    </com-table>
                    <div v-else class="content-box">
                        <div class="search">
                            <el-input
                                clearable
                                style="width: 300px;"
                                placeholder="请输入搜索关键字"
                                :suffix-icon="'el-icon-search'"
                                size="small"
                                v-model="searchValue"
                                @change="handlerIconClick"
                                @clear="handlerIconClick"
                            >
                            </el-input>
                        </div>
                        <div class="organization-box" v-loading="loading">
                            <el-tree
                                v-if="nodeData.length"
                                ref="tree"
                                :data="nodeData"
                                default-expand-all
                                :props="{ children: 'subGroups' }">
                                <span class="custom-tree-node" slot-scope="{ data }">
                                    <span class="name">{{data.name}}</span>
                                    <el-checkbox
                                        v-model="data.checked"
                                        @change="handleCheck(data)" />
                                </span>
                            </el-tree>
                        </div>
                    </div>
                </div>
                <div class="selection-container">
                    <p>已选择（共<span>{{allSelected.length}}</span>条）<span class="clear" @click="handleClear">清空</span></p>
                    <ul>
                        <li v-for="item in allSelected" :key="item.id + item.type">
                            {{ item.type === 'user' ? `${item.chname || '--'}(${item.bk_username})` : item.name }}
                            <span>{{ item.type === 'user' ? '用户' : '组织' }}</span>
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
