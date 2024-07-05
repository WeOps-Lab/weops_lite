<template>
    <div>
        <drawer-component
            :size="538"
            :title="`${currentType}属性`"
            :visible="isShow"
            :quick-close="true"
            destroy-on-close
            custom-class="common-dialog-wrapper"
            :before-close="cancel">
            <div slot="content">
                <div class="common-dialog-wrapper-main" v-loading="loading">
                    <div class="form-box">
                        <el-form
                            label-width="94"
                            :model="formData"
                            :rules="rules"
                            ref="validateForm">
                            <el-form-item
                                label="属性ID"
                                desc="请填写英文开头，下划线、数字、英文的组合"
                                :desc-type="'icon'"
                                :prop="isAdd ? 'propertyID' : ''">
                                <el-input
                                    v-model="formData.propertyID"
                                    size="small"
                                    :disabled="!isAdd"
                                    placeholder="请输入属性ID">
                                </el-input>
                            </el-form-item>
                            <el-form-item
                                label="属性名"
                                prop="name">
                                <el-input v-model="formData.name" size="small" placeholder="请输入属性名"></el-input>
                            </el-form-item>
                            <el-form-item
                                label="值类型"
                                prop="valueType">
                                <el-select
                                    style="width: 100%;"
                                    placeholder="请选择值类型"
                                    v-model="formData.valueType"
                                    searchable
                                    size="small"
                                    :clearable="false"
                                    :disabled="!isAdd"
                                    @change="changeValueType">
                                    <el-option
                                        v-for="option in valueTypeList"
                                        :key="option.id"
                                        :label="option.name"
                                        :value="option.id">
                                    </el-option>
                                </el-select>
                            </el-form-item>
                            <div class="field-setting" v-if="formData.valueType === 'enum'">
                                <!-- 暂且隐藏 -->
                                <!-- <div class="field-setting-item">
                                    <div class="label">字段设置</div>
                                    <bk-checkbox
                                        v-model="formData.fieldEdit.isEdit"
                                        :true-value="true"
                                        :false-value="false">
                                        可编辑
                                    </bk-checkbox>
                                </div>
                                <div v-if="['bool'].includes(formData.valueType)" class="field-setting-item">
                                    <div class="label">默认值</div>
                                    <bk-switcher v-model="formData.fieldEdit.defaultValue" theme="primary"></bk-switcher>
                                </div>
                                <div v-if="['singlechar', 'longchar'].includes(formData.valueType)" class="field-setting-item">
                                    <div class="label">正则校验</div>
                                    <bk-input
                                        v-model="formData.fieldEdit.regularCheck"
                                        placeholder="请输入"
                                        :type="'textarea'"
                                        :rows="3">
                                    </bk-input>
                                </div>
                                <div v-if="['int', 'float'].includes(formData.valueType)" class="field-setting-item">
                                    <div class="label line-height-32">最小值</div>
                                    <bk-input
                                        v-model="formData.fieldEdit.minValue"
                                        type="number"
                                        placeholder="请输入最小数值"
                                        @change="verificationNumber('min')">
                                    </bk-input>
                                </div>
                                <div v-if="['int', 'float'].includes(formData.valueType)" class="field-setting-item">
                                    <div class="label line-height-32">最大值</div>
                                    <bk-input
                                        v-model="formData.fieldEdit.maxValue"
                                        type="number"
                                        placeholder="请输入最大数值"
                                        @change="verificationNumber('max')">
                                    </bk-input>
                                </div> -->
                                <div v-if="['list', 'enum'].includes(formData.valueType)" class="field-setting-item">
                                    <div class="label">{{formData.valueType === 'list' ? '列表' : '枚举'}}值</div>
                                    <div class="list-type" style="flex: 1;">
                                        <div class="already-add-list">
                                            <transition-group class="container" name="sort">
                                                <div
                                                    v-for="(item, index) in alreadyAddList"
                                                    :key="item.id"
                                                    :class="[
                                                        'already-add-list-item',
                                                        index !== 0 && 'item-top',
                                                        item.id === dragEndId && dragStartId !== dragEndId && (dragStartIndex > dragEndIndex ? 'already-add-active-top' : 'already-add-active-bottom')
                                                    ]">
                                                    <div
                                                        class="drag-box"
                                                        draggable="true"
                                                        @dragstart="dragstart(item, index)"
                                                        @dragenter="dragenter(item, index)"
                                                        @dragend="getDragend()"
                                                        @dragover="dragover($event)">
                                                        <div style="margin-right: 5px;">
                                                            <i class="cw-icon weops-drag-drop"></i>
                                                        </div>
                                                        <div class="input-box">
                                                            <el-input
                                                                v-if="formData.valueType === 'enum'"
                                                                size="small"
                                                                v-model="item.valueId"
                                                                style="width: 110px;margin-right: 10px;"
                                                                placeholder="请输入ID"
                                                                @change="changeValueId(item, index)">
                                                            </el-input>
                                                            <span class="error-input-msg">{{item.valueIdErrorMsg}}</span>
                                                        </div>
                                                        <div class="input-box" style="flex: 1;">
                                                            <el-input
                                                                v-model="item.name"
                                                                size="small"
                                                                style="width: 100%;"
                                                                placeholder="请输入值"
                                                                @change="changeName(item, index)">
                                                            </el-input>
                                                            <span class="error-input-msg">{{item.nameErrorMsg}}</span>
                                                        </div>
                                                        <div class="icon-box" :style="{ flexDirection: alreadyAddList.length > 1 ? 'row' : 'row-reverse' }">
                                                            <i class="cw-icon weops-add" @click="addListTypeData"></i>
                                                            <i
                                                                v-if="alreadyAddList.length > 1"
                                                                class="cw-icon weops-delete"
                                                                @click="deleteListTypeData(index)">
                                                            </i>
                                                        </div>
                                                    </div>
                                                </div>
                                            </transition-group>
                                        </div>
                                    </div>
                                </div>
                                <div
                                    v-if="['enum'].includes(formData.valueType)"
                                    class="field-setting-item default-value-setting"
                                    style="display: flex;">
                                    <div class="label line-height-32">默认值设置</div>
                                    <el-select
                                        v-model="formData.fieldEdit.enumDefaultValue"
                                        size="small"
                                        placeholder="请选择默认值"
                                        :clearable="false"
                                        searchable
                                        style="flex: 1;">
                                        <el-option
                                            v-for="option in enumDefaultList"
                                            :key="option.id"
                                            :value="option.id"
                                            :label="option.name">
                                        </el-option>
                                    </el-select>
                                </div>
                            </div>
                            <!-- <bk-form-item
                                label="所属分组"
                                :required="true"
                                :property="'group'"
                                :error-display-type="'normal'">
                                <bk-select
                                    v-model="formData.group"
                                    placeholder="请选择所属分组"
                                    searchable
                                    :disabled="!isAdd"
                                    :clearable="false">
                                    <bk-option
                                        v-for="option in groupList"
                                        :key="option.id"
                                        :id="option.id"
                                        :name="option.name">
                                    </bk-option>
                                </bk-select>
                            </bk-form-item>
                            <bk-form-item
                                v-if="!['date', 'time', 'bool'].includes(formData.valueType)"
                                label="是否唯一"
                                :required="true"
                                :property="'is_only'"
                                ext-cls="whether-class"
                                :error-display-type="'normal'">
                                <bk-radio-group v-model="formData.is_only">
                                    <bk-radio :value="true" style="margin-right: 27px;">是</bk-radio>
                                    <bk-radio :value="false">否</bk-radio>
                                </bk-radio-group>
                            </bk-form-item> -->
                            <el-form-item
                                label="是否必填"
                                prop="is_required"
                                ext-cls="whether-class"
                                :error-display-type="'normal'">
                                <el-radio-group v-model="formData.is_required" style="width: 100%;">
                                    <el-radio :label="true" class="mr20">是</el-radio>
                                    <el-radio :label="false">否</el-radio>
                                </el-radio-group>
                            </el-form-item>
                            <el-form-item
                                label="可编辑"
                                prop="editable"
                                ext-cls="whether-class"
                                :error-display-type="'normal'">
                                <el-radio-group v-model="formData.editable" style="width: 100%;">
                                    <el-radio :label="true" class="mr20">是</el-radio>
                                    <el-radio :label="false">否</el-radio>
                                </el-radio-group>
                            </el-form-item>
                            <el-form-item
                                label="是否唯一"
                                prop="is_only"
                                ext-cls="whether-class"
                                :error-display-type="'normal'">
                                <el-radio-group v-model="formData.is_only" style="width: 100%;">
                                    <el-radio :label="true" class="mr20">是</el-radio>
                                    <el-radio :label="false">否</el-radio>
                                </el-radio-group>
                            </el-form-item>
                            <!-- <bk-form-item
                                v-if="formData.valueType === 'int'"
                                label="单位">
                                <bk-cascade
                                    clearable
                                    :list="unitOptions"
                                    :options="{
                                        childrenKey: 'formats'
                                    }"
                                    placeholder="请选择数据单位"
                                    v-model="formData.unitGroup"
                                    style="width: 100%;"
                                    @change="changeUnit">
                                </bk-cascade>
                            </bk-form-item> -->
                        </el-form>
                    </div>
                </div>
            </div>
            <div slot="footer">
                <el-button
                    :disabled="loading"
                    type="primary"
                    size="small"
                    @click="validate">
                    提交
                </el-button>
                <el-button
                    :disabled="loading"
                    size="small"
                    type="default"
                    @click="cancel">
                    取消
                </el-button>
            </div>
        </drawer-component>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
