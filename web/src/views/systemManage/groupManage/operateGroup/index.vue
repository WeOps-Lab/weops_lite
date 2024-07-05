<template>
    <el-dialog
        :visible.sync="visible"
        width="600px"
        :close-on-click-modal="false"
        :title="title"
        @closed="closeDialog"
    >
        <div class="content-box" v-loading="loading">
            <el-form label-width="60px" :model="formData" :rules="rules" ref="organizationValidateForm">
                <el-form-item label="名称" prop="group_name">
                    <el-input size="small" v-model="formData.group_name" placeholder="请输入组织名称"></el-input>
                </el-form-item>
            </el-form>
        </div>
        <template slot="footer">
            <el-button
                class="mr10"
                :disabled="loading"
                type="primary"
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
