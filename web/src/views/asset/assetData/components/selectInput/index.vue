<template>
    <div class="select-input">
        <div class="select-input-main" :style="{ width: `${width}px` }">
            <el-select
                class="field"
                size="small"
                filterable
                v-model="fieldKey"
                placeholder="请选择"
                @change="changeFieldKey">
                <el-option
                    v-for="(item,index) in propertyList"
                    :key="index"
                    :label="item.attr_name"
                    :value="item.attr_id">
                </el-option>
            </el-select>
            <el-date-picker
                v-if="['date', 'time'].includes(currentFeildInfo['attr_type'])"
                class="value"
                size="small"
                v-model="fieldValue"
                :placeholder="'选择日期时间'"
                value-format="yyyy-MM-dd HH:mm:ss"
                type="datetimerange"
                @change="changeFieldvaule">
            </el-date-picker>
            <el-select
                v-else-if="['enum', 'bool','user'].includes(currentFeildInfo['attr_type'])"
                class="value"
                clearable=""
                size="small"
                v-model="fieldValue"
                filterable
                @change="changeFieldvaule">
                <el-option
                    v-for="option in currentFeildInfo['attr_type'] === 'user' ? userList : currentFeildInfo.option"
                    :key="option.id"
                    :value="option.id"
                    :label="option.name">
                </el-option>
            </el-select>
            <el-cascader
                v-else-if="currentFeildInfo['attr_type'] === 'organization'"
                class="value"
                :props="{
                    emitPath: false,
                    checkStrictly: true
                }"
                size="small"
                v-model="fieldValue"
                clearable
                :options="groupList"
                @change="changeFieldvaule">
            </el-cascader>
            <el-input
                v-else
                class="value"
                v-model="fieldValue"
                size="small"
                clearable
                type="text"
                @change="changeFieldvaule">
            </el-input>
            <div v-if="exactSearch"
                class="exact-search-box">
                <el-checkbox
                    :true-label="1"
                    :false-label="0"
                    v-model="isExactSearch"
                    @change="changeFieldvaule(fieldValue)">
                    精确搜索
                </el-checkbox>
            </div>
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
