<template>
    <div class="user-manage">
        <page-explanation
            title="用户列表"
            content="展示所有自动/手动同步的用户信息，您可以进行用户信息的维护和角色的授予" />
        <div class="manage-wrapper">
            <div class="operate-box">
                <div>
                    <el-button
                        :disabled="tableLoading"
                        type="primary"
                        icon="el-icon-plus"
                        class="mr10"
                        v-permission="{
                            id: $route.name,
                            type: 'SysUser_create'
                        }"
                        size="small"
                        @click="operateUser('add')">
                        新增用户
                    </el-button>
                </div>
                <el-input
                    :disabled="tableLoading"
                    clearable
                    style="width: 300px;"
                    placeholder="请输入搜索关键字"
                    :suffix-icon="'el-icon-search'"
                    v-model="search"
                    size="small"
                    @change="handlerIconClick"
                    @clear="handlerIconClick"
                >
                </el-input>
            </div>
            <div class="table-box">
                <com-table
                    v-loading="tableLoading"
                    ref="comTable"
                    :data="dataList"
                    :columns="columns"
                    :max-height="tableMaxHeight"
                    :pagination="pagination"
                    @page-change="handlePageChange"
                    @page-limit-change="limitChange"
                    @filter-change="sourceFilterMethod"
                >
                    <template slot="roles" slot-scope="{ row }">
                        <span>{{getRoles(row)}}</span>
                    </template>
                    <template slot="groups" slot-scope="{ row }">
                        <span>{{getOrganizationOrSuperior(row, { listKey: 'groups', fieldKey: 'path' })}}</span>
                    </template>
                    <template slot="operation" slot-scope="{ row }">
                        <el-button
                            class="mr10"
                            type="text"
                            v-permission="{
                                id: $route.name,
                                type: 'SysUser_edit'
                            }"
                            size="small"
                            @click="operateRole(row)">
                            设置角色
                        </el-button>
                        <el-button
                            class="mr10"
                            type="text"
                            v-permission="{
                                id: $route.name,
                                type: 'SysUser_edit'
                            }"
                            size="small"
                            @click="operateGroup(row)">
                            设置组织
                        </el-button>
                        <el-button
                            class="mr10"
                            type="text"
                            v-permission="{
                                id: $route.name,
                                type: 'SysUser_edit'
                            }"
                            size="small"
                            @click="operateUser('edit', row)">
                            编辑
                        </el-button>
                        <el-button
                            class="mr10"
                            type="text"
                            v-permission="{
                                id: $route.name,
                                type: 'SysUser_delete'
                            }"
                            size="small"
                            @click="deleteUser(row)">
                            删除
                        </el-button>
                        <el-button
                            class="mr10"
                            type="text"
                            v-permission="{
                                id: $route.name,
                                type: 'SysUser_edit'
                            }"
                            size="small"
                            @click="resetPassword(row)">
                            重置密码
                        </el-button>
                    </template>
                </com-table>
            </div>
            <reset-password ref="resetPassword"></reset-password>
            <operate-user ref="operateUser" @refreshList="refreshList"></operate-user>
            <group-setting ref="operateGroup" @confirm="confirm"></group-setting>
            <role-manage
                ref="roleManage"
                title="设置角色"
                @confirm="confirm" />
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>
