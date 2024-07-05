<template>
    <div class="sys-log">
        <div class="manage-wrapper">
            <div class="search-box">
                <span>操作者</span>
                <el-select
                    v-model="params.operator"
                    style="width: 150px;"
                    clearable
                    placeholder="请选择操作者"
                    size="small"
                    @change="searchDataByUser">
                    <el-option
                        v-for="item in userList"
                        :key="item.id"
                        :label="item.name"
                        :value="item.id">
                    </el-option>
                </el-select>
                <span>操作类型</span>
                <el-select
                    v-model="params.type"
                    style="width: 150px;"
                    clearable
                    placeholder="请选择操作类型"
                    size="small"
                    @change="searchDataByType">
                    <el-option
                        v-for="item in typeList"
                        :key="item.id"
                        :label="item.name"
                        :value="item.id">
                    </el-option>
                </el-select>
                <span>时间范围</span>
                <el-date-picker
                    class="mr16"
                    v-model="params.dateTime"
                    type="datetimerange"
                    range-separator="-"
                    start-placeholder="开始日期"
                    end-placeholder="结束日期"
                    size="small"
                    @change="getDate">
                </el-date-picker>
                <el-button
                    class="mr8"
                    :disabled="isLoading"
                    size="small"
                    type="primary"
                    @click="getLogs">
                    搜索
                </el-button>
                <el-button
                    :disabled="isLoading"
                    size="small"
                    @click="resetSearch">
                    重置
                </el-button>
            </div>
            <div class="test-dom" v-loading="isLoading">
                <com-table
                    ref="table"
                    :data="recordList"
                    :columns="columns"
                    :pagination="pagination"
                    height="calc(100vh - 320px)"
                    @page-change="handlePageChange"
                    @page-limit-change="handleLimitChange"
                >
                    <template slot="type" slot-scope="{ row }">
                        <span>{{ getOperateType(row.type)}}</span>
                    </template>
                    <template slot="operator" slot-scope="{ row }">
                        <span>{{ getOperator(row.operator)}}</span>
                    </template>
                    <template slot="operation" slot-scope="{ row }">
                        <el-button
                            size="small"
                            type="text"
                            @click="checkDetail(row)"
                        >
                            详情
                        </el-button>
                    </template>
                </com-table>
            </div>
        </div>
        <record-detial
            ref="recordDetial"
            :model-info-list="modelInfoList"
            :property-list="propertyList"
            :group-list="groupList"
            :user-list="userList"
            :connect-type-list="connectTypeList"
        />
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss">
@import "./index.scss"
</style>
