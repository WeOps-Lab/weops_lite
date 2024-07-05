<template>
    <drawer-component
        title="重置密码"
        :visible="isShow"
        :size="500"
        custom-class="common-dialog-wrapper"
        :append-to-body="true"
        @changeVisible="changeVisible">
        <div slot="content" class="common-dialog-wrapper-main content-box">
            <el-form
                :model="passwordFormData"
                ref="validatePsdForm"
                :rules="passwordRules"
                label-width="80px">
                <el-form-item label="密码" :required="true" prop="password">
                    <el-input
                        show-password
                        size="small"
                        v-model="passwordFormData.password"
                        placeholder="请输入密码">
                    </el-input>
                </el-form-item>
                <el-form-item label="确认密码" :required="true" prop="confirmPassword" error-display-type="normal">
                    <el-input
                        show-password
                        size="small"
                        v-model="passwordFormData.confirmPassword"
                        placeholder="请输入密码">
                    </el-input>
                </el-form-item>
            </el-form>
        </div>
        <template slot="footer">
            <el-button type="primary" size="small" @click="onPasswordSubmit" :loading="isPsdLoading">提交</el-button>
            <el-button type="default" size="small" class="ml20" @click="onPasswordCancel">取消</el-button>
        </template>
    </drawer-component>
</template>

<script lang="ts" src="./resetPassword.ts"></script>
