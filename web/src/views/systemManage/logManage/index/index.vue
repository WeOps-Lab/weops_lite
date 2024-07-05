<template>
    <div class="sys-log">
        <page-explanation
            title="操作日志"
            content="展示所有增删改等历史记录，您可以根据操作者/操作类型/时间等条件进行查询" />
        <div class="manage-wrapper">
            <div class="search-box">
                <span>操作者</span>
                <el-input
                    clearable
                    v-model="params.operator"
                    style="width: 150px;"
                    placeholder="请输入操作者"
                    size="small"
                    @change="searchDataByUser">
                </el-input>
                <span>操作类型</span>
                <el-select
                    v-model="params.operate_type"
                    style="width: 150px;
                    background-color: #ffffff;"
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
                    :disabled="isLoading"
                    size="small"
                    type="primary"
                    @click="resetSearch">
                    重置
                </el-button>
            </div>
            <div class="test-dom" v-loading="isLoading">
                <com-table
                    ref="table"
                    :data="logList"
                    :columns="columns"
                    :pagination="pagination"
                    :max-height="tableMaxHeight"
                    @page-change="handlePageChange"
                    @page-limit-change="handleLimitChange"
                >
                    <template slot="operate_type" slot-scope="{ row }">
                        <span>{{ getOperateType(row.operate_type)}}</span>
                    </template>
                </com-table>
            </div>
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss">
@import "./index.scss"
</style>
