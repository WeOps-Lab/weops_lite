<template>
    <drawer-component
        :title="`${isAdd ? '新增' : '编辑'}外链`"
        :visible="isShow"
        :size="500"
        custom-class="common-dialog-wrapper"
        @changeVisible="changeVisible">
        <div slot="content" class="common-dialog-wrapper-main">
            <div class="form-box">
                <el-form label-width="90px" :model="formData" :rules="rules" ref="validateForm">
                    <el-form-item label="显示名称" :required="true" prop="name">
                        <el-input v-model="formData.name" size="small"></el-input>
                    </el-form-item>
                    <el-form-item label="链接" :required="true" prop="url">
                        <el-input v-model="formData.url" size="small"></el-input>
                    </el-form-item>
                </el-form>
            </div>
        </div>
        <template slot="footer" class="common-dialog-wrapper-footer">
            <el-button
                type="primary"
                class="mr10"
                size="small"
                @click="confirm">
                确认
            </el-button>
            <el-button @click="cancel" size="small">
                取消
            </el-button>
        </template>
    </drawer-component>
</template>

<script lang="ts" src="./index.ts"></script>
