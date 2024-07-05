<template>
    <div class="model-detail">
        <div class="detail-header">
            <div class="header-info">
                <div class="icon">
                    <img :src="require(`@/assets/svg/model/${modelInfo.icn || 'cc-default_默认'}.svg`)" alt="">
                </div>
                <div class="object">
                    <div class="object-name">{{ modelInfo.model_name }}</div>
                    <div class="object-id">{{ modelInfo.model_id }}</div>
                </div>
                <!-- <div class="asset">
                        <span>资产数量：</span>
                        <span class="asset-num">12</span>
                    </div> -->
            </div>
            <div class="header-operate">
                <el-button
                    v-permission="{
                        id: $route.name,
                        type: 'ModelManage_edit'
                    }"
                    type="text"
                    size="mini"
                    icon="el-icon-edit"
                    @click="editModel">
                    编辑
                </el-button>
                <el-button
                    v-permission="{
                        id: $route.name,
                        type: 'ModelManage_delete'
                    }"
                    type="text"
                    size="mini"
                    icon="el-icon-delete"
                    @click="handleDelete">
                    删除
                </el-button>
            </div>
        </div>
        <el-card class="mt10">
            <menu-tab type="line" :panels="panels" :active-panel="active" @click="toTabMenu"></menu-tab>
            <div v-if="active === 'property'">
                <el-button
                    v-permission="{
                        id: $route.name,
                        type: 'ModelManage_create'
                    }"
                    class="mt20 mb15"
                    size="small"
                    type="primary"
                    @click="editAttr()">
                    添加属性
                </el-button>
                <com-table
                    :data="propertyData"
                    :columns="columns"
                    v-loading="loading"
                    :row-key="'attr_id'"
                    :height="tableMaxHeight">
                    <template slot="operation" slot-scope="{ row }">
                        <el-button
                            v-permission="{
                                id: $route.name,
                                type: 'ModelManage_edit'
                            }"
                            type="text"
                            size="mini"
                            @click="editAttr(row)">
                            编辑
                        </el-button>
                        <el-button
                            v-permission="{
                                id: $route.name,
                                type: 'ModelManage_delete'
                            }"
                            type="text"
                            size="mini"
                            @click="deleteAtrr(row)">
                            删除
                        </el-button>
                    </template>
                    <template slot="require" slot-scope="{ row }">
                        <el-tag :type="row.is_required ? 'success' : ''">{{row.is_required ? '是' : '否'}}</el-tag>
                    </template>
                    <template slot="editable" slot-scope="{ row }">
                        <el-tag :type="row.editable ? 'success' : ''">{{row.editable ? '是' : '否'}}</el-tag>
                    </template>
                    <template slot="is_only" slot-scope="{ row }">
                        <el-tag :type="row.is_only ? 'success' : ''">{{row.is_only ? '是' : '否'}}</el-tag>
                    </template>
                    <template slot="attrType" slot-scope="{ row }">
                        <span>{{ showAttrType(row.attr_type) }}</span>
                    </template>
                </com-table>
            </div>
            <template v-else>
                <el-button
                    v-permission="{
                        id: $route.name,
                        type: 'ModelManage_create'
                    }"
                    class="mt20 mb15"
                    size="small"
                    type="primary"
                    @click="relationOperate('add')">
                    添加关联
                </el-button>
                <com-table
                    :data="relationData"
                    :columns="relateColumns"
                    v-loading="relateLoading"
                    :height="tableMaxHeight">
                    <template slot="mapping" slot-scope="{ row }">
                        {{ showMapping(row) }}
                    </template>
                    <template slot="src_model_id" slot-scope="{ row }">
                        {{ showModelName(row.src_model_id) }}
                    </template>
                    <template slot="dst_model_id" slot-scope="{ row }">
                        {{ showModelName(row.dst_model_id) }}
                    </template>
                    <template slot="asst_id" slot-scope="{ row }">
                        {{ showConnectType(row.asst_id,'label') }}
                    </template>
                    <template slot="model_asst_id" slot-scope="{ row }">
                        {{ showConnectName(row) }}
                    </template>
                    <template slot="operation" slot-scope="{ row }">
                        <el-button
                            v-permission="{
                                id: $route.name,
                                type: 'ModelManage_edit'
                            }"
                            type="text"
                            size="mini"
                            @click="relationOperate('edit',row)">
                            编辑
                        </el-button>
                        <el-button
                            v-permission="{
                                id: $route.name,
                                type: 'ModelManage_delete'
                            }"
                            type="text"
                            size="mini"
                            @click="deleteAsso(row)">
                            删除
                        </el-button>
                    </template>
                </com-table>
            </template>
        </el-card>
        <add-model ref="editModel" :group-list="modelGroupList" @refreshModel="refreshModel"></add-model>
        <attributes-operation
            ref="attributesOperation"
            :model-id="modelInfo.model_id"
            @getTableData="handlerChange" />
        <connect-operation
            ref="connectOperation"
            :model-list="modelList"
            :connect-type-list="connectTypeList"
            :model-id="modelInfo.model_id"
            @refreshRel="getModelAssoList">
        </connect-operation>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
