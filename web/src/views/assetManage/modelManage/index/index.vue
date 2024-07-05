<template>
    <div class="asset-model page-container">
        <page-explanation
            title="模型管理"
            content="模型管理提供了所有资产的模型和模型分组的新建和管理，您可以根据需求创建和管理" />
        <div
            class="asset-model-wrapper"
            v-loading="loading">
            <div class="action-bar">
                <el-button
                    v-permission="{
                        id: $route.name,
                        type: 'ModelManage_create'
                    }"
                    size="small"
                    :type="'primary'"
                    @click="addModel">
                    新建模型
                </el-button>
                <el-button
                    size="small"
                    v-permission="{
                        id: $route.name,
                        type: 'ModelManage_create'
                    }"
                    class="ml20"
                    @click="groupOperation('add')">
                    新建分组
                </el-button>
                <el-input
                    class="ml20"
                    size="small"
                    clearable
                    placeholder="请输入模型名称"
                    style="flex: 1;"
                    suffix-icon="el-icon-search"
                    v-model="searchKey"
                    @change="getAllModelList"
                    @clear="getAllModelList">
                </el-input>
            </div>
            <div class="show-box">
                <div
                    class="model-list"
                    v-for="item in modelList"
                    :key="item.id">
                    <div class="model-header">
                        <div>
                            <span class="name">{{item.classification_name}}</span>
                            <span class="count">{{`(${item.list.length})`}}</span>
                        </div>
                        <div class="model-header-operation show-operation">
                            <el-button
                                v-permission="{
                                    id: $route.name,
                                    type: 'ModelManage_delete'
                                }"
                                :disabled="!!item.list.length"
                                type="text"
                                size="mini"
                                icon="el-icon-delete"
                                @click="handleDelete(item)">
                            </el-button>
                            <el-button
                                v-permission="{
                                    id: $route.name,
                                    type: 'ModelManage_edit'
                                }"
                                type="text"
                                size="mini"
                                icon="el-icon-edit"
                                @click="groupOperation('edit',item)">
                            </el-button>
                        </div>
                    </div>
                    <div class="model-body">
                        <div
                            v-for="tex in item.list"
                            :key="tex.model_id"
                            class="model-info"
                            @click="checkModelDetail(tex)">
                            <div class="left-info">
                                <div class="icon-box">
                                    <div
                                        class="drag-item">
                                        <!-- <i class="cw-icon weops-drag-drop"></i> -->
                                    </div>
                                    <img :src="getIconUrl(tex)" alt="">
                                </div>
                                <div class="info-box">
                                    <div class="hide-text" v-overflow-tooltip>
                                        {{tex.model_name}}
                                    </div>
                                    <div class="model-id hide-text" v-overflow-tooltip>
                                        {{tex.model_id}}
                                    </div>
                                </div>
                            </div>
                            <div :class="['right-info', 'is-show', item.bk_classification_id === 'bk_file' && 'is-disabled']">
                                <i class="el-icon-date" style="font-size: 16px;" />
                                <!-- <span>{{tex.count > 999 ? '999+' : tex.count}}</span> -->
                            </div>
                        </div>
                    </div>
                </div>
                <el-empty
                    v-if="!modelList.length"
                    style="margin-top: 200px;"
                    class="exception-wrap-item exception-part"
                    description="暂无数据"
                >
                </el-empty>
            </div>
            <add-model
                ref="addModel"
                :group-list="modelGroupList"
                @getAllModelList="getAllModelList">
            </add-model>
            <group-operation
                ref="groupOperation"
                @getAllModelList="getAllModelList" />
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
