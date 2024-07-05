<template>
    <div>
        <drawer-component
            :title="`${isAdd ? '新建' : '编辑'}模型`"
            :size="500"
            :visible="isShow"
            destroy-on-close
            custom-class="common-dialog-wrapper"
            :before-close="cancel">
            <div slot="content" class="common-dialog-wrapper-main">
                <div class="icon-box">
                    <div class="icon" @click="selectIcon">
                        <img :src="require(`@/assets/svg/model/${iconUrl}.svg`)" alt="">
                    </div>
                    <div style="text-align: center;margin-top: 8px;">选择图标</div>
                </div>
                <el-form
                    label-width="110"
                    :model="formData"
                    :rules="rules"
                    ref="validateForm"
                >
                    <el-form-item
                        label="所属分组"
                        prop="group">
                        <el-select v-model="formData.group" size="small" style="width: 100%;" :disabled="!isAdd">
                            <el-option v-for="option in groupList"
                                :key="option.classification_id"
                                :label="option.classification_name"
                                :value="option.classification_id">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item
                        label="模型类型"
                        prop="model_type">
                        <el-select v-model="formData.model_type" size="small" style="width: 100%;" :disabled="!isAdd">
                            <el-option v-for="option in typeList"
                                :key="option.id"
                                :label="option.name"
                                :value="option.id">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item
                        label="唯一标识"
                        desc="可使用英文、数字、下划线，需以字母开头"
                        :desc-type="'icon'"
                        :prop="isAdd ? 'onlyMark' : ''">
                        <el-input size="small" v-model="formData.onlyMark" :disabled="!isAdd" placeholder="请输入唯一标识"></el-input>
                    </el-form-item>
                    <el-form-item
                        label="名称"
                        prop="name"
                        desc="请填写模型名"
                        :desc-type="'icon'">
                        <el-input size="small" v-model="formData.name" placeholder="请输入名称"></el-input>
                    </el-form-item>
                </el-form>
            </div>
            <template slot="footer">
                <el-button size="small" :loading="loading" :disabled="loading" :type="'primary'" @click="confirm">
                    确认
                </el-button>
                <el-button :type="'default'" size="small" @click="cancel">
                    取消
                </el-button>
            </template>
        </drawer-component>
        <select-icon
            ref="selectIcon"
            @setIcon="setIcon"
        >
        </select-icon>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
