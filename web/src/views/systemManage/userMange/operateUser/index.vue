<template>
    <el-dialog
        :visible.sync="visible"
        width="600px"
        :close-on-click-modal="false"
        :title="type === 'add' ? '新增用户' : '编辑用户'"
        @closed="closeDialog">
        <div class="content-box" v-loading="loading">
            <el-form label-width="80px" :model="formData" :rules="rules" ref="validateUserForm">
                <el-form-item label="用户名" prop="username">
                    <el-input
                        :disabled="type === 'edit'"
                        v-model="formData.username"
                        size="small"
                        placeholder="请输入用户名">
                    </el-input>
                </el-form-item>
                <el-form-item label="中文名" prop="lastName">
                    <el-input v-model="formData.lastName" size="small" placeholder="请输入中文名"></el-input>
                </el-form-item>
                <el-form-item label="邮箱" :prop="'email'">
                    <el-input v-model="formData.email" size="small" placeholder="请输入邮箱"></el-input>
                </el-form-item>
                <el-form-item v-if="type === 'add'" label="密码" :prop="'password'">
                    <el-input
                        v-model="formData.password"
                        placeholder="请输入密码"
                        show-password
                        size="small"
                        :clearable="true">
                    </el-input>
                </el-form-item>
                <el-form-item v-if="type === 'add'" label="确认密码" :prop="'confirmPassword'">
                    <el-input
                        v-model="formData.confirmPassword"
                        placeholder="请输入密码"
                        show-password
                        size="small"
                        :clearable="true">
                    </el-input>
                </el-form-item>
            </el-form>
        </div>
        <template slot="footer">
            <el-button
                :disabled="loading"
                :type="'primary'"
                class="mr10"
                size="small"
                @click="confirm">
                确认
            </el-button>
            <el-button size="small" @click="close">
                取消
            </el-button>
        </template>
    </el-dialog>
</template>

<script lang="ts" src="./index.ts"></script>
