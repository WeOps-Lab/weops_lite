<template>
    <drawer-component
        :size="550"
        :title="`${isAdd ? '新建关联' : '编辑关联'}属性`"
        :visible="isShow"
        :quick-close="true"
        destroy-on-close
        custom-class="common-dialog-wrapper"
        :before-close="cancel">
        <div slot="content" class="common-dialog-wrapper-main content-box">
            <el-form
                v-loading="loading"
                label-width="110"
                :model="formData"
                :rules="rules"
                ref="validateForm">
                <el-form-item label="关联名称" :prop="'name'">
                    <el-input
                        class="width100"
                        size="small"
                        disabled
                        placeholder="请输入关联名称"
                        v-model="assoName">
                    </el-input>
                </el-form-item>
                <el-form-item
                    label="源模型"
                    :prop="'src_model_id'">
                    <el-select
                        class="width100"
                        :disabled="!isAdd"
                        size="small"
                        v-model="formData.src_model_id"
                        @change="changeSourceModel">
                        <el-option-group
                            v-for="group in modelList"
                            :label="group.classification_name"
                            :key="group.classification_id">
                            <el-option
                                v-for="option in group.list"
                                :disabled="option.disabled"
                                :key="option.model_id"
                                :value="option.model_id"
                                :label="option.model_name">
                            </el-option>
                        </el-option-group>
                    </el-select>
                </el-form-item>
                <div v-if="isAdd" class="sort">
                    <span class="exchange-icon" @click="exchangeSource">
                        <i class="el-icon-sort"></i>
                    </span>
                </div>
                <el-form-item
                    label="目标模型"
                    :prop="'dst_model_id'">
                    <el-select
                        class="width100"
                        size="small"
                        v-model="formData.dst_model_id"
                        :disabled="!isAdd"
                        @change="changeTargetModel">
                        <el-option-group
                            v-for="group in modelList"
                            :label="group.classification_name"
                            :key="group.classification_id">
                            <el-option
                                v-for="option in group.list"
                                :disabled="option.disabled"
                                :key="option.model_id"
                                :value="option.model_id"
                                :label="option.model_name">
                            </el-option>
                        </el-option-group>
                    </el-select>
                </el-form-item>
                <el-form-item
                    label="关联类型"
                    :prop="'asst_id'">
                    <el-select
                        class="width100"
                        size="small"
                        v-model="formData.asst_id"
                        :disabled="!isAdd"
                        :clearable="false"
                        @change="changeConnectType">
                        <el-option
                            v-for="option in connectTypeList"
                            :key="option.id"
                            :value="option.id"
                            :label="option.name">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item
                    label="约束条件"
                    :prop="'mapping'">
                    <el-select
                        class="width100"
                        size="small"
                        v-model="formData.mapping"
                        :clearable="false"
                        :disabled="!isAdd">
                        <el-option
                            v-for="option in targetBindList"
                            :key="option.id"
                            :value="option.id"
                            :label="option.name">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item v-if="sourceModelDetail && targetModelDetail && connectTypeDetail" label="效果示意">
                    <div class="effect-representation">
                        <div class="model-item">
                            <div class="model-icon">
                                <img :src="getIconUrl(sourceModelDetail)" alt="">
                            </div>
                            <span class="model-name">{{sourceModelDetail.model_name}}</span>
                        </div>
                        <div class="model-edge">
                            <div class="connection">
                                <span v-overflow-tooltip class="name">{{connectTypeDetail.name}}</span>
                            </div>
                        </div>
                        <div class="model-item">
                            <div class="model-icon">
                                <img :src="getIconUrl(targetModelDetail)" alt="">
                            </div>
                            <span class="model-name">{{targetModelDetail.model_name}}</span>
                        </div>
                    </div>
                    <!-- <div class="tip-text">
                        <span>{{assoName}}</span>
                    </div> -->
                    <div class="tip-text">
                        <span>{{connectTypeDetail.name}}</span>:
                        <span class="ml5">{{connectTypeMap[formData.asst_id] || connectTypeMap.default}}</span>
                    </div>
                </el-form-item>
            </el-form>
        </div>
        <div slot="footer">
            <el-button
                :disabled="loading || !isAdd"
                :loading="loading"
                type="primary"
                size="small"
                @click="confirm">
                确认
            </el-button>
            <el-button
                size="small"
                type="default"
                @click="cancel">
                取消
            </el-button>
        </div>
    </drawer-component>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
