<template>
    <div class="base-info" v-loading="loading">
        <el-form
            label-width="200"
            ref="addResourceForm"
            :rules="rules"
            :model="formData">
            <collapse :collapse-list="resourcList">
                <template slot="content" slot-scope="{ collRow }">
                    <div class="show-info">
                        <el-form-item
                            v-for="tex in collRow.list"
                            :style="{ width: displayPercent }"
                            class="custom-form-item"
                            :key="tex['attr_id']"
                            :label="tex['attr_name']"
                            :prop="tex['attr_id']">
                            <span :class="['custom-label',tex.is_required && 'label-required']">
                                <span v-overflow-tooltip class="attr-name">{{ tex['attr_name'] }}</span>
                                <span>:</span>
                            </span>
                            <template v-if="tex.isEdit">
                                <el-date-picker
                                    v-if="['date', 'time'].includes(tex['attr_type'])"
                                    class="form-item"
                                    size="small"
                                    v-model="formData[tex.attr_id]"
                                    :placeholder="'选择日期时间'"
                                    :value-format="tex['attr_type'] === 'time' ? 'yyyy-MM-dd HH:mm:ss' : ''"
                                    :type="tex['attr_type'] === 'date' ? 'date' : 'datetime'">
                                </el-date-picker>
                                <el-select
                                    class="form-item"
                                    v-else-if="['enum', 'list', 'user'].includes(tex['attr_type'])"
                                    size="small"
                                    v-model="formData[tex.attr_id]"
                                    filterable>
                                    <el-option
                                        v-for="option in tex['attr_type'] === 'user' ? userList : tex.option"
                                        :key="option.id"
                                        :value="option.id"
                                        :label="option.name">
                                    </el-option>
                                </el-select>
                                <el-switch
                                    class="form-item"
                                    v-else-if="tex['attr_type'] === 'bool'"
                                    size="small"
                                    v-model="formData[tex.attr_id]">
                                </el-switch>
                                <el-cascader
                                    v-else-if="tex['attr_type'] === 'organization'"
                                    :props="{
                                        emitPath: false,
                                        checkStrictly: true
                                    }"
                                    class="form-item"
                                    size="small"
                                    v-model="formData[tex.attr_id]"
                                    :options="groupList">
                                </el-cascader>
                                <el-input
                                    v-else
                                    v-model="formData[tex.attr_id]"
                                    size="small"
                                    clearable
                                    :show-password="tex['attr_type'] === 'pwd'"
                                    :type="tex['attr_type'] === 'pwd' ? 'password' : 'text'">
                                </el-input>
                            </template>
                            <template v-else>
                                <div class="operate-content">
                                    <span v-overflow-tooltip class="content">{{ getShowValue(tex) }}</span>
                                    <span class="operate-edit">
                                        <span v-if="!tex.isEdit" class="edit-icon">
                                            <span
                                                v-if="tex.editable && allowEdit"
                                                v-permission="operatePower"
                                                class="cw-icon weops-edit operate-icon-edit"
                                                @click="editInfo(tex)"></span>
                                            <span class="cw-icon weops-copy operate-icon-copy" v-copy="getShowValue(tex)"></span>
                                        </span>
                                    </span>
                                </div>
                            </template>
                            <span class="operate-confirm">
                                <span v-if="tex.isEdit" class="confirm-cancel">
                                    <span
                                        v-permission="operatePower"
                                        class="cw-icon weops-complete operate-icon-left"
                                        @click="confirmEdit(tex)">
                                    </span>
                                    <span class="cw-icon weops-close operate-icon-right" @click="cancelEdit(tex)"></span>
                                </span>
                            </span>
                        </el-form-item>
                    </div>
                </template>
            </collapse>
        </el-form>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
