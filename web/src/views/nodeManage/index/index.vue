<template>
    <div class="node-manage">
        <page-explanation
            title="节点管理"
            content="您可以将资产选择成为节点，以便进行自动化操作或者日志探针的安装。" />
        <div class="node-manage-wrapper manage-wrapper">
            <div class="operate-box">
                <el-button
                    v-permission="{
                        id: $route.name,
                        type: 'NodeManage_manage'
                    }"
                    class="mr10"
                    type="primary"
                    icon="el-icon-plus"
                    size="small"
                    @click="addNode">
                    新增节点
                </el-button>
                <div class="select-input-main" style="width: 350px;">
                    <el-select
                        class="field"
                        size="small"
                        filterable
                        v-model="fieldKey"
                        placeholder="请选择"
                        @change="changeFieldKey">
                        <el-option
                            v-for="(item,index) in attrList"
                            :key="index"
                            :label="item.name"
                            :value="item.id">
                        </el-option>
                    </el-select>
                    <el-select
                        v-if="fieldKey === 'model_id'"
                        class="value"
                        clearable
                        size="small"
                        v-model="fieldValue"
                        filterable
                        @change="changeFieldvaule">
                        <el-option
                            v-for="option in modelList"
                            :key="option.model_id"
                            :value="option.model_id"
                            :label="option.model_name">
                        </el-option>
                    </el-select>
                    <el-input
                        v-else
                        class="value"
                        v-model="fieldValue"
                        size="small"
                        clearable
                        type="text"
                        @change="changeFieldvaule">
                    </el-input>
                </div>
            </div>
            <div class="table-box">
                <com-table
                    v-loading="tableLoading"
                    ref="comTable"
                    :data="dataList"
                    :columns="columns"
                    :pagination="pagination"
                    height="calc(100vh - 300px)"
                    @page-change="handlePageChange"
                    @page-limit-change="limitChange"
                    @filter-change="filterChange"
                >
                    <template slot="model_id" slot-scope="{ row }">
                        {{ showModelName(row.model_id) }}
                    </template>
                    <template slot="os_type" slot-scope="{ row }">
                        {{ showType(row.os_type) }}
                    </template>
                    <template slot="sidecar_status" slot-scope="{ row }">
                        <el-tag
                            :type="getStatusStyle(row.sidecar_status)">
                            {{showStatus(row.sidecar_status)}}
                        </el-tag>
                    </template>
                    <template slot="operation" slot-scope="{ row }">
                        <el-button
                            class="mr10"
                            type="text"
                            size="small"
                            @click="handleInstall(row)">
                            安装控制器
                        </el-button>
                        <el-button
                            v-permission="{
                                id: $route.name,
                                type: 'NodeManage_manage'
                            }"
                            class="mr10"
                            type="text"
                            size="small"
                            @click="deleteNode(row)">
                            删除
                        </el-button>
                    </template>
                </com-table>
            </div>
        </div>
        <add-instance ref="addInstance" @createNode="createNode" />
        <handMovement ref="handMovement" />
    </div>
</template>

<script lang="ts" src="./index.ts"></script>
<style lang="scss" scoped>
@import "./index.scss"
</style>
