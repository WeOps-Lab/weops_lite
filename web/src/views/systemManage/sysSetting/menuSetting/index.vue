<template>
    <div class="menu-setting-wrapper">
        <div class="custom-menu-wrapper">
            <span>菜单名称：</span>
            <el-input
                style="width: 250px;"
                :clearable="true"
                v-model="menuTitle"
                size="small"
                placeholder="请输入菜单名称" />
        </div>
        <div class="custom-menu-content mt15">
            <div class="built-in-menu container-col">
                <div class="title">菜单项</div>
                <div class="bt-menu-content col-content">
                    <el-tree
                        default-expand-all
                        :data="activationMenu">
                        <div :class="{
                                 'tree-row': true,
                                 'disabled': data.id === 'SysSetting'
                             }"
                            slot-scope="{ data }"
                            @click="handleRow(data, $event)">
                            <!-- 层级：{{ node.level + 1 }}，名称：  -->
                            <!-- 只有最后一层级路由即页面可勾选（children不存在）或者动态的页面组，如基础监控和资产记录(存在children，但是为空) -->
                            <el-checkbox
                                v-if="!data.children || (data.children && data.children.length === 0)"
                                :value="data.checked" />
                            {{ data.name }}
                            <span
                                v-if="menuGroup.includes(data.id)"
                                class="tip-section">
                                ({{ tipMap[data.id] }})
                            </span>
                        </div>
                    </el-tree>
                </div>
            </div>
            <div class="configuration-menu container-col">
                <div class="title">
                    <p>
                        菜单结构
                        <el-tooltip content="最多支持三层菜单结构，直接拖动可进行排序和层级调整，其中目录下必须包含页面,‘基础监控’和‘资产记录’仅支持在第1/2层级" placement="right">
                            <i class="el-icon-question"></i>
                        </el-tooltip>
                    </p>
                    <el-button
                        size="small"
                        type="primary"
                        plain
                        @click="createExternalChain('add')">
                        创建外链
                    </el-button>
                    <el-button
                        class="mr20"
                        size="small"
                        type="primary"
                        plain
                        @click="handleAddDirectory">
                        创建目录
                    </el-button>
                </div>
                <div class="col-content" v-loading="initLoading">
                    <menu-item
                        v-if="configMenuList && configMenuList.length"
                        :all-menu="configMenuList"
                        :menu="configMenuList"
                        :key="refreshKey"
                        @edit-external-chain="editExternalChain"
                        @delete="deleteMenuItem"
                        @change="changeMenuItem" />
                </div>
                <div class="col-button-wrapper">
                    <el-button
                        type="primary"
                        size="small"
                        class="mr10"
                        :disabled="loading"
                        :loading="loading"
                        @click="handleSave">
                        保存
                    </el-button>
                    <el-button
                        size="small"
                        class="mr10"
                        @click="handleCancel">
                        取消
                    </el-button>
                </div>
            </div>
        </div>
        <external-chain
            ref="externalChain"
            @handle-external-chain="handleExternalChain">
        </external-chain>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss">
@import "./index.scss"
</style>
