<template>
    <div>
        <drawer-component
            :title="`${isAdd ? '新建' : '编辑'}分组`"
            :size="500"
            :visible="visible"
            custom-class="common-dialog-wrapper"
            destroy-on-close
            :before-close="cancel">
            <div slot="content" class="common-dialog-wrapper-main">
                <el-form
                    label-width="110"
                    :model="formData"
                    :rules="rules"
                    ref="validateForm">
                    <el-form-item
                        label="唯一标识"
                        desc="可使用小写字母、数字、下划线，需以字母开头"
                        :desc-type="'icon'"
                        prop="onlyMark">
                        <el-input
                            v-model="formData.onlyMark"
                            :disabled="!isAdd"
                            size="small"
                            placeholder="请输入唯一标识，可使用小写字母、数字、下划线，需以字母开头"
                            ref="onlyMark">
                        </el-input>
                    </el-form-item>
                    <el-form-item
                        label="名称"
                        prop="name">
                        <el-input size="small" v-model="formData.name" placeholder="请输入名称"></el-input>
                    </el-form-item>
                </el-form>
            </div>
            <div slot="footer">
                <el-button
                    :loading="loading"
                    :disabled="loading"
                    :type="'primary'"
                    size="small"
                    @click="confirm">
                    确认
                </el-button>
                <el-button size="small" @click="cancel">
                    取消
                </el-button>
            </div>
        </drawer-component>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>
