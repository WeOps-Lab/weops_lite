<template>
    <el-dialog
        width="600px"
        :visible.sync="resetVisible"
        :close-on-click-modal="false"
        title="重置密码"
        @closed="closeResetDialog">
        <div v-loading="resetLoading">
            <el-form label-width="80px" :model="formData" :rules="rules" ref="validatePsdForm">
                <el-form-item label="重置密码" :prop="'password'">
                    <el-input
                        :clearable="true"
                        size="small"
                        v-model="formData.password"
                        show-password
                        placeholder="请输入重置密码"
                    >
                    </el-input>
                </el-form-item>
                <el-form-item label="确认密码" :prop="'confirmPassword'">
                    <el-input
                        :clearable="true"
                        size="small"
                        v-model="formData.confirmPassword"
                        show-password
                        placeholder="请输入重置密码"
                    >
                    </el-input>
                </el-form-item>
            </el-form>
        </div>
        <template slot="footer">
            <el-button
                :disabled="resetLoading"
                :type="'primary'"
                class="mr10"
                size="small"
                @click="confirmReset">
                确认
            </el-button>
            <el-button size="small" @click="close">
                取消
            </el-button>
        </template>
    </el-dialog>
</template>

<script lang="ts" src="./index.ts"></script>
