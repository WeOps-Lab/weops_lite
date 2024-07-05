<template>
    <div id="logoSetting" v-loading="basicLoading">
        <div class="table">
            <el-upload
                v-loading="!reShow"
                class="avatar-uploader"
                list-type="picture-card"
                :action="'0'"
                :http-request="handleUpload"
                :with-credentials="true"
                :multiple="false"
                :show-file-list="false">
                <img v-if="file[0].url" :src="file[0].url" class="avatar">
                <div v-else class="avatar-uploader-icon">
                    <i class="el-icon-plus"></i>
                    <div>点击上传</div>
                </div>
            </el-upload>
            <el-button
                v-permission="powerParams"
                class="restyle-btn"
                :disabled="!$BtnPermission({
                    id: $route.name,
                    type: 'operateAuth'
                }) && !fileData"
                size="small"
                type="primary"
                @click="uploadLogo()">
                确认上传
            </el-button>
            <el-button
                v-permission="powerParams"
                class="restyle-btn"
                size="small"
                @click="initLogo()">
                恢复默认
            </el-button>
            <i class="el-icon-info" style="color: #3A84FF;"></i>
            <span style="margin-left: 15px;color: #979BA5;">
                仅支持上传 png、jpg、jpeg 或 svg 格式的图片，建议上传图片宽高比1:1。
            </span>
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss">
@import "./index.scss"
</style>
