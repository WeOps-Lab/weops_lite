<template>
    <drawer-component
        title="个人信息"
        :visible="isShow"
        :size="600"
        :before-close="beforeClose"
        custom-class="common-dialog-wrapper">
        <div slot="content" class="common-dialog-wrapper-main content-box" v-loading="pageLoading">
            <el-form label-width="80px" :model="formData" ref="validateForm"
                v-loading="isInfoLoading" :rules="formRules">
                <el-form-item label="用户名" :required="true" prop="username">
                    <el-input
                        :disabled="true"
                        size="small"
                        v-model="formData.username"
                        placeholder="请输入用户名">
                    </el-input>
                </el-form-item>
                <el-form-item label="中文名" prop="display_name">
                    <el-input
                        :disabled="!isEdit"
                        size="small"
                        v-model="formData.display_name"
                        placeholder="请输入中文名">
                    </el-input>
                </el-form-item>
                <el-form-item label="邮箱" prop="email">
                    <el-input
                        :disabled="!isEdit"
                        size="small"
                        v-model="formData.email"
                        placeholder="请输入邮箱">
                    </el-input>
                </el-form-item>
            </el-form>
            <div class="btn-box" v-if="!isEdit">
                <el-button
                    type="text"
                    style="margin-right: 20px;"
                    @click="updateFormData">
                    修改信息
                </el-button>
                <el-button type="text" @click="showPasswordForm">
                    重置密码
                </el-button>
            </div>
            <reset-password ref="resetPassword" />
        </div>
        <template slot="footer">
            <div v-if="isEdit">
                <el-button type="primary" size="small" @click="onFormSubmit">提交</el-button>
                <el-button type="default" size="small" @click="onFormCancel">取消</el-button>
            </div>
            <el-button v-else type="default" size="small" @click="isShow = false">关闭</el-button>
        </template>
    </drawer-component>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
