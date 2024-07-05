<template>
    <div class="asset-model page-container" v-loading="loading">
        <el-tabs class="asset-model-tabs" v-model="currentModel" @tab-click="handleTabClick">
            <el-tab-pane
                v-for="(item,index) in modelList"
                :key="index"
                :label="item.model_name"
                :name="item.model_id">
            </el-tab-pane>
        </el-tabs>
        <div class="asset-model-wrapper">
            <div class="group-tree">
                <el-tree
                    v-if="treeList.length"
                    empty-text="暂无数据"
                    ref="groupTree"
                    :data="treeList"
                    default-expand-all
                    :expand-on-click-node="false"
                    highlight-current
                    :props="{ children: 'subGroups', label: 'name' }"
                    node-key="id"
                    @node-click="selectGroup">
                    <span slot-scope="{ data }" class="tree-node">
                        <span class="cw-icon weops-apply tree-icon"></span>
                        <span>{{ data.name }}</span>
                    </span>
                </el-tree>
                <el-empty v-else class="empty" :image-size="50"></el-empty>
            </div>
            <div class="instance-list">
                <div class="operate-box">
                    <div class="operate-box-left">
                        <el-dropdown size="small">
                            <el-button
                                size="small"
                                type="primary">
                                新建
                                <i class="el-icon-arrow-down el-icon--right"></i>
                            </el-button>
                            <el-dropdown-menu slot="dropdown">
                                <el-dropdown-item
                                    v-permission="operatePower"
                                    @click.native="addResource('add')">
                                    手动创建
                                </el-dropdown-item>
                                <el-dropdown-item
                                    v-permission="operatePower"
                                    @click.native="addResource('import')">
                                    批量导入
                                </el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>
                        <el-dropdown class="mr10 ml10" size="small">
                            <el-button size="small">
                                操作
                                <i class="el-icon-arrow-down el-icon--right"></i>
                            </el-button>
                            <el-dropdown-menu slot="dropdown">
                                <el-dropdown-item
                                    v-permission="operatePower"
                                    :disabled="!selectedInstances.length"
                                    @click.native="deleteInstance(selectedInstances)">
                                    批量删除
                                </el-dropdown-item>
                                <el-dropdown-item
                                    v-permission="operatePower"
                                    :disabled="!selectedInstances.length"
                                    @click.native="addResource('batchUpdate')">
                                    批量更新
                                </el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>
                        <el-dropdown size="small">
                            <el-button size="small">
                                导出
                                <i class="el-icon-arrow-down el-icon--right"></i>
                            </el-button>
                            <el-dropdown-menu slot="dropdown">
                                <el-dropdown-item
                                    v-permission="operatePower"
                                    @click.native="exportInst([])">
                                    导出全部
                                </el-dropdown-item>
                                <el-dropdown-item
                                    v-permission="operatePower"
                                    :disabled="!selectedInstances.length"
                                    @click.native="exportInst(selectedInstances)">
                                    导出所选
                                </el-dropdown-item>
                            </el-dropdown-menu>
                        </el-dropdown>
                    </div>
                    <div class="operate-box-right">
                        <selectInput :property-list="atrrList" :user-list="userList" @change="changeFeild" />
                    </div>
                </div>
                <com-table
                    v-show="columns.length"
                    v-loading="tableLoading"
                    ref="comTable"
                    :data="instanceList"
                    :columns="columns"
                    :pagination="pagination"
                    height="calc(100vh - 230px)"
                    :settings-fields="displayFields"
                    @page-change="handlePageChange"
                    @page-limit-change="handleLimitChange"
                    @select="handleSelect"
                    @select-all="handleSelect"
                    @handle-setting-change="handleSettingChange"
                >
                    <template slot="operation" slot-scope="{ row }">
                        <el-button
                            type="text"
                            size="small"
                            @click="checkDetail(row)">
                            详情
                        </el-button>
                        <el-button
                            v-permission="operatePower"
                            type="text"
                            size="small"
                            @click="addResource('edit',row)">
                            编辑
                        </el-button>
                        <el-button
                            type="text"
                            size="small"
                            @click="checkRelate(row)">
                            关联
                        </el-button>
                        <el-button
                            v-permission="operatePower"
                            type="text"
                            size="small"
                            @click="deleteInstance([row])">
                            删除
                        </el-button>
                    </template>
                    <template v-for="field in slotColumns" :slot="field.scopedSlots" slot-scope="{ row }">
                        <div :key="field.key">
                            <el-tag
                                v-if="field.attr_type === 'bool'"
                                :type="row[field.key] ? 'success' : ''">
                                {{getShowValue(field, row)}}
                            </el-tag>
                            <span v-else>{{ getShowValue(field, row) }}</span>
                        </div>
                    </template>
                </com-table>
            </div>
        </div>
        <add-instance
            ref="addInstance"
            :model-id="currentModel"
            :group-list="groupList"
            :user-list="userList"
            :current-node="currentNode"
            :connect-type-list="connectTypeList"
            :model-info-list="modelInfoList"
            @on-success="updateInstanceList" />
        <import-instance
            ref="importInstance"
            :model-id="currentModel"
            :current-node="currentNode"
            @on-success="updateInstanceList" />
        <relation ref="relation"
            :group-list="groupList"
            :connect-type-list="connectTypeList"
            :model-info-list="modelInfoList"
            :user-list="userList"
            :property-list="propertyList"
            :inst-info="instInfo"
        />
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
.asset-model {
    .asset-model-tabs {
        min-height: 54px;
        margin-top: -14px;
    }

    .asset-model-wrapper {
        display: flex;
    }

    .instance-list {
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        overflow: scroll;
        flex-flow: column;
        background: #fff;
    }

    .group-tree {
        width: 250px;
        background: #fafbfd;
        border: 1px solid #edeff3;
        margin-right: 10px;
        padding: 10px;
        overflow: scroll;
        height: calc(100vh - 130px);
    }
    .tree-node {
        display: flex;
        align-items: center;
        font-size: 12px;
        .tree-icon {
            color: #a3c5fd;
            margin-right: 4px;
        }
    }

    /* stylelint-disable selector-class-pattern */
    /deep/ .el-tree-node__content {
        background: #fafbfd;
        &:hover {
            background: #f0f7ff;
        }
    }
    /deep/ .el-tree-node__label {
        font-size: 12px;
    }
    /deep/ .el-tree-node > .el-tree-node__children {
        background-color: #fafbfd;
    }
    /deep/ .is-current > .el-tree-node__content {
        background-color: #e1ecff !important;
        .tree-icon {
            color: #4b8fff !important;
        }
    }
}
</style>
