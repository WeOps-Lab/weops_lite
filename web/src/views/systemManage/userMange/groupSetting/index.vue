<template>
    <drawer-component
        title="设置所在组织"
        :visible="visible"
        :size="800"
        custom-class="common-dialog-wrapper"
        :before-close="handleClose">
        <div slot="content" class="transfer-box common-dialog-wrapper-main">
            <div class="source-list">
                <div class="header">待选择列表</div>
                <div class="content-box">
                    <div class="search">
                        <el-input
                            clearable
                            style="width: 300px;"
                            placeholder="请输入搜索关键字"
                            :suffix-icon="'el-icon-search'"
                            size="small"
                            v-model="search"
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
                                    v-model="data.checked" />
                            </span>
                        </el-tree>
                    </div>
                </div>
            </div>
            <div class="selection-container">
                <p>已选择（共<span>{{ selectedNode.length }}</span>条）<span class="clear" @click="handleClear">清空</span></p>
                <ul>
                    <li v-for="item in selectedNode" :key="item.id">
                        {{ item.name }}
                        <span>组织</span>
                        <i class="el-icon-close" style="font-size: 12px;" @click="handleDelete(item.id)"></i>
                    </li>
                </ul>
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

<style lang="scss" scoped>
@import "index.scss"
</style>
