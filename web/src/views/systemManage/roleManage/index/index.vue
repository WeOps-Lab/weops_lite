<template>
    <div class="role-manage">
        <page-explanation
            title="角色管理"
            content="您可以进行角色的新建和授权，权限的授权分为操作权限和实例权限，可从菜单操作和实例管理两个方面进行限制" />
        <div class="role-manage-wrapper manage-wrapper">
            <div class="operate-box">
                <el-button
                    v-permission="{
                        id: $route.name,
                        type: 'SysRole_create'
                    }"
                    class="mr10"
                    type="primary"
                    icon="el-icon-plus"
                    size="small"
                    @click="operateRole('add')">
                    新增角色
                </el-button>
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
            <div class="table-box">
                <com-table
                    v-loading="tableLoading"
                    ref="comTable"
                    :data="dataList"
                    :columns="columns"
                    :pagination="pagination"
                    :max-height="tableMaxHeight"
                    @page-change="handlePageChange"
                    @page-limit-change="limitChange"
                >
                    <template slot="built_in" slot-scope="{ row }">
                        <el-tag type="success" v-if="['admin', 'normal', 'grade_admin'].includes(row.name)">是</el-tag>
                        <el-tag v-else>否</el-tag>
                    </template>
                    <template slot="operation" slot-scope="{ row }">
                        <el-button
                            v-permission="{
                                id: $route.name,
                                type: 'SysRole_users_manage'
                            }"
                            class="mr10"
                            type="text"
                            size="small"
                            @click="personnelManage(row)">
                            人员和组织
                        </el-button>
                        <el-button
                            v-permission="{
                                id: $route.name,
                                type: 'SysRole_permissions'
                            }"
                            class="mr10"
                            type="text"
                            size="small"
                            :disabled=" ['admin', 'grade_admin'].includes(row.name)"
                            @click="setPermission(row)">
                            设置权限
                        </el-button>
                        <el-button
                            v-permission="{
                                id: $route.name,
                                type: 'SysRole_edit'
                            }"
                            class="mr10"
                            type="text"
                            size="small"
                            :disabled="['admin', 'normal', 'grade_admin'].includes(row.name)"
                            @click="operateRole('edit', row)">
                            编辑
                        </el-button>
                        <el-button
                            v-permission="{
                                id: $route.name,
                                type: 'SysRole_delete'
                            }"
                            class="mr10"
                            type="text"
                            size="small"
                            :disabled="['admin', 'normal', 'grade_admin'].includes(row.name)"
                            @click="deleteRole(row)">
                            删除
                        </el-button>
                    </template>
                </com-table>
            </div>
            <operate-role ref="operateRole" @refreshList="refreshList" :role-list="dataList" />
            <permission-settings ref="permissionSettings" />
            <user-and-group
                ref="userAndGroup"
                title="人员和组织"
                @confirm="getRoleList()" />
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>
