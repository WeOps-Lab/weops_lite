<template>
    <div>
        <drawer-component
            :title="`${isAdd ? '新建' : '编辑'}资产`"
            :size="640"
            :visible="visible"
            destroy-on-close
            custom-class="common-dialog-wrapper"
            :before-close="beforeCloseDialog">
            <div slot="content" class="content-box common-dialog-wrapper-main">
                <el-form
                    label-width="280"
                    ref="addResourceForm"
                    :rules="rules"
                    :model="formData">
                    <collapse :collapse-list="resourcList">
                        <template slot="content" slot-scope="{ collRow }">
                            <div class="show-info">
                                <el-form-item
                                    v-for="tex in collRow.list"
                                    :key="tex['attr_id']"
                                    :label="tex['attr_name']"
                                    :prop="tex['attr_id']">
                                    <div :class="['el-form-item__label','custom-label',tex.is_required && 'required']">
                                        <el-checkbox
                                            v-if="isBatchUpdate"
                                            :disabled="!tex.editable"
                                            v-model="tex.checked">
                                            {{ tex['attr_name'] }}
                                        </el-checkbox>
                                        <span v-else>{{ tex['attr_name'] }}</span>
                                    </div>
                                    <el-date-picker
                                        v-if="['date', 'time'].includes(tex['attr_type'])"
                                        :disabled="!canEdit(tex)"
                                        class="form-item"
                                        size="small"
                                        v-model="formData[tex.attr_id]"
                                        :placeholder="'选择日期时间'"
                                        :value-format="tex['attr_type'] === 'time' ? 'yyyy-MM-dd HH:mm:ss' : ''"
                                        :type="tex['attr_type'] === 'date' ? 'date' : 'datetime'">
                                    </el-date-picker>
                                    <el-select
                                        v-else-if="['enum', 'list', 'user'].includes(tex['attr_type'])"
                                        class="form-item"
                                        :disabled="!canEdit(tex)"
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
                                        v-else-if="tex['attr_type'] === 'bool'"
                                        class="form-item"
                                        :disabled="!canEdit(tex)"
                                        size="small"
                                        v-model="formData[tex.attr_id]">
                                    </el-switch>
                                    <el-cascader
                                        v-else-if="tex['attr_type'] === 'organization'"
                                        :disabled="!canEdit(tex)"
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
                                        :disabled="!canEdit(tex)"
                                        v-model="formData[tex.attr_id]"
                                        size="small"
                                        clearable
                                        :type="tex['attr_type'] === 'pwd' ? 'password' : 'text'">
                                        <i
                                            v-if="tex['attr_type'] === 'pwd'"
                                            class="el-icon-document-copy el-input__icon"
                                            slot="suffix"
                                            v-copy="formData[tex.attr_id]">
                                        </i>
                                    </el-input>
                                </el-form-item>
                            </div>
                        </template>
                    </collapse>
                </el-form>
            </div>
            <div slot="footer">
                <el-button
                    v-if="isAdd"
                    :loading="loading"
                    :type="'primary'"
                    :disabled="saveDisabled"
                    size="small"
                    @click="handleSubmit('saveAndRelate')">
                    保存并创建关联
                </el-button>
                <el-button
                    :loading="loading"
                    :type="'primary'"
                    :disabled="saveDisabled"
                    size="small"
                    @click="handleSubmit('save')">
                    保存
                </el-button>
                <el-button
                    size="small"
                    @click="beforeCloseDialog">
                    关闭
                </el-button>
            </div>
        </drawer-component>
        <add-relation
            ref="addRelation"
            :connect-type-list="connectTypeList"
            :model-info-list="modelInfoList"
            :group-list="groupList"
            :user-list="userList"
            :inst-info="instInfo"
            @refreshList="closeRelate"
        />
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
