<template>
    <div class="select-input">
        <div class="select-input-main" :style="{ width: `${width}px` }">
            <el-select
                :class="['field',showCondition && 'radius']"
                size="small"
                filterable
                v-model="config.field"
                placeholder="选择资产"
                @change="changeFieldKey">
                <el-option
                    v-for="(item,index) in propertyList"
                    :key="index"
                    :label="item.attr_name"
                    :value="item.attr_id">
                </el-option>
            </el-select>
            <div v-if="showCondition">
                <el-select
                    class="condition"
                    size="small"
                    filterable
                    v-model="config.type"
                    placeholder="选择条件">
                    <el-option
                        v-for="(item,index) in conditionList[currentFeildInfo['attr_type']]"
                        :key="index"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                </el-select>
            </div>
            <el-date-picker
                v-if="['date', 'time'].includes(currentFeildInfo['attr_type'])"
                class="value"
                size="small"
                v-model="config.value"
                :placeholder="'选择日期时间'"
                value-format="yyyy-MM-dd HH:mm:ss"
                type="datetimerange"
                @change="changeFieldvaule">
            </el-date-picker>
            <el-select
                v-else-if="['enum', 'bool','user'].includes(currentFeildInfo['attr_type'])"
                :class="['value',showCondition && 'radius']"
                :multiple="currentFeildInfo['attr_type'] !== 'bool'"
                placeholder="请选择值"
                :collapse-tags="true"
                clearable
                size="small"
                v-model="config.value"
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
                :class="['value',showCondition && 'radius']"
                placeholder="请选择值"
                :props="{
                    emitPath: false,
                    multiple: true,
                    checkStrictly: true
                }"
                size="small"
                v-model="config.value"
                clearable
                :options="groupList"
                @change="changeFieldvaule">
            </el-cascader>
            <el-input
                v-else
                :class="['value',showCondition && 'radius']"
                placeholder="请输入值"
                v-model="config.value"
                size="small"
                clearable
                type="text"
                @change="changeFieldvaule">
            </el-input>
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
