<template>
    <div class="sys-organization">
        <page-explanation
            title="组织管理"
            content="您可以创建组织，用于管理一组用户，或者进行角色授权，您可以创建、修改和删除组织，并管理其下级单位。" />
        <div class="organization-manage manage-wrapper">
            <div class="operate-box">
                <!-- <div >
                    <el-button
                        class="mr10"
                        type="primary"
                        v-permission="{
                            id: $route.name,
                            type: 'SysGroup_create'
                        }"
                        size="small"
                        @click="operateGroup('add')">
                        新增组织
                    </el-button>
                </div> -->
                <el-input
                    clearable
                    style="width: 300px;"
                    placeholder="请输入搜索关键字"
                    suffix-icon="el-icon-search"
                    size="small"
                    v-model="search"
                    @change="handlerIconClick"
                    @clear="handlerIconClick"
                >
                </el-input>
            </div>
            <div class="tree-box" v-loading="loading">
                <div class="tree-box-header">
                    <span>组织名称</span>
                    <span>操作</span>
                </div>
                <el-tree
                    class="tree-box-body"
                    ref="tree"
                    :data="nodeData"
                    default-expand-all
                    :props="{ children: 'subGroups' }"
                    @check-change="handleCheck">
                    <span class="custom-tree-node" slot-scope="{ node,data }">
                        <span>{{ data.name }}</span>
                        <span class="operate-node">
                            <el-button
                                type="text"
                                v-permission="{
                                    id: $route.name,
                                    type: 'SysGroup_create'
                                }"
                                size="small"
                                @click.stop="operateGroup('addSub', node)">
                                添加子组
                            </el-button>
                            <el-button
                                type="text"
                                v-permission="{
                                    id: $route.name,
                                    type: 'SysGroup_user'
                                }"
                                size="small"
                                @click.stop="personnelManage(node)">
                                人员管理
                            </el-button>
                            <el-button
                                type="text"
                                v-permission="{
                                    id: $route.name,
                                    type: 'SysGroup_role'
                                }"
                                size="small"
                                @click.stop="roleManage(node)">
                                角色管理
                            </el-button>
                            <el-button
                                type="text"
                                v-permission="{
                                    id: $route.name,
                                    type: 'SysGroup_edit'
                                }"
                                size="small"
                                @click.stop="operateGroup('edit', node)">
                                编辑
                            </el-button>
                            <el-button
                                class="mr20"
                                type="text"
                                v-permission="{
                                    id: $route.name,
                                    type: 'SysGroup_delete'
                                }"
                                :disabled="!!data.subGroupCount"
                                size="small"
                                @click.stop="deleteNode(node)">
                                删除
                            </el-button>
                        </span>
                    </span>
                </el-tree>
            </div>
        </div>
        <operate-group ref="operateGroup" @refreshList="refreshList" />
        <auth-white-list
            ref="authWhiteList"
            :only-choose-user="true"
            title="人员管理"
            caller="groupManage"
            @confirm="getGroups" />
        <role-manage
            ref="roleManage"
            title="角色管理" />
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
