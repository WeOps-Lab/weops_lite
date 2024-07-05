<template>
    <drawer-component
        title="导入资产"
        :size="640"
        :visible="visible"
        destroy-on-close
        custom-class="common-dialog-wrapper"
        :before-close="beforeCloseDialog">
        <div slot="content" class="content-box common-dialog-wrapper-main">
            <div class="upload-area">
                <el-upload
                    class="upload-com"
                    :accept="'.xls,.xlsx'"
                    :file-list="formData.fileList"
                    :http-request="handleUpload"
                    :show-file-list="false"
                    drag
                    action="https://jsonplaceholder.typicode.com/posts/">
                    <i class="el-icon-upload"></i>
                    <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                    <div class="el-upload__tip" slot="tip">只能上传xlsx文件，且不超过20MB</div>
                </el-upload>
                <span class="template-file" @click="handleDownload"><span class="cw-icon file-download weops-download"></span>下载模板</span>
                <ul v-if="formData.fileList.length" class="file-list">
                    <li v-for="(item, index) in formData.fileList" :key="index">
                        <div class="file-list-name">
                            <span class="file-success cw-icon weops-complete-fill"></span>
                            <span class="name hide-text">{{item.name}}</span>
                        </div>
                        <span class="file-delete show-delete" @click="deleteFile(index)">×</span>
                    </li>
                </ul>
            </div>
        </div>
        <div slot="footer">
            <el-button
                :disabled="!formData.fileList.length"
                :loading="loading"
                :type="'primary'"
                size="small"
                @click="handleSubmit">
                保存
            </el-button>
            <el-button
                size="small"
                @click="beforeCloseDialog">
                关闭
            </el-button>
        </div>
    </drawer-component>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
