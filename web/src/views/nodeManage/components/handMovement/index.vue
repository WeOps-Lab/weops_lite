<template>
    <drawer-component
        :title="title"
        :size="650"
        :visible="isShow"
        destroy-on-close
        :before-close="beforeCloseDialog">
        <div
            class="common-dialog-wrapper-main hand-movement-content"
            slot="content"
            v-loading="loading">
            <template v-if="detail.operationType !== 'controller'">
                <div class="mb10" style="font-size: 14px;color: #63656e;font-weight: 700;">安装方式:</div>
                <el-radio-group class="mb10" v-model="installWay" size="small" fill="#ffffff" text-color="#63656e">
                    <el-radio-button :label="detail.os_type === 'linux' ? 'Linux' : 'Windows'">
                        {{ detail.os_type === 'linux' ? 'Linux' : 'Windows' }}
                    </el-radio-button>
                </el-radio-group>
            </template>
            <div class="show-result">
                <el-alert
                    v-if="controllerType === 'unload'"
                    class="mb25"
                    type="warning"
                    title="请确定已经手动卸载控制器，系统将自动获取控制器卸载情况，已卸载的主机将从列表中移除，未卸载的主机仍展示在列表中，并可以进行正常操作">
                </el-alert>
                <div class="text-box" v-if="commandList.length">
                    <div :class="['custom-step', index !== commandList.length - 1 && 'custom-step-space']"
                        v-for="(item, index) in commandList"
                        :key="index">
                        <div class="step-number">{{index + 1}}</div>
                        <div class="step-content">
                            <div class="step-content-title">{{item.title}}</div>
                            <div class="step-result" v-if="!item.download_url">
                                <i
                                    v-copy="item.content"
                                    class="operate-icon-copy el-icon-document-copy">
                                </i>
                                <span>{{item.content}}</span>
                            </div>
                            <div
                                v-else
                                class="download-text"
                                @click="downloadFile(item.download_url)">
                                <i class="el-icon-download"></i>
                                {{item.content}}
                            </div>
                        </div>
                    </div>
                </div>
                <el-empty v-else description="暂无数据" :image-size="80"></el-empty>
            </div>
        </div>
        <div slot="footer">
            <el-button
                type="default"
                size="small"
                @click="beforeCloseDialog">
                关闭
            </el-button>
            <el-button
                v-if="controllerType === 'unload'"
                style="margin-left: 15px;"
                type="default"
                size="small"
                @click="handleUnloadController">
                已完成
            </el-button>
        </div>
    </drawer-component>
</template>

<script lang="ts">
    import { Vue, Component } from 'vue-property-decorator'
    import DrawerComponent from '@/components/comDrawer/index.vue'
    @Component({
        name: 'hand-movement',
        components: {
            DrawerComponent
        }
    })
    export default class handMovement extends Vue {
        isShow: boolean = false
        detail: any = {}
        loading: boolean = false
        installWay: string = 'linux'
        commandList: any[] = []
        title: string = '手动安装'
        controllerType: string = ''
        show(row?) {
            this.isShow = true
            this.detail = row
            // if (row.operationType === 'controller') {
            //     const { title, commandList, controllerType } = row
            //     this.title = title
            //     this.commandList = commandList.map(r => ({
            //         ...r,
            //         content: r.content.replace(/\${host}/g, window.HOST + window.APP_CODE)
            //     }))
            //     this.controllerType = controllerType
            //     return false
            // }
            this.installWay = this.detail.os_type === 'linux' ? 'Linux' : 'Windows'
            this.getManagementCommands(row)
        }
        beforeCloseDialog() {
            this.isShow = false
        }
        downloadFile(url) {
            window.open(url)
        }
        getManagementCommands(row) {
            this.loading = true
            const params = {
                id: this.detail.id
            }
            this.$api.NodeManage.getInstallSteps(params).then(res => {
                const { result, data } = res
                if (!result) {
                    return false
                }
                this.commandList = data
            }).finally(() => {
                this.loading = false
            })
        }
        handleUnloadController() {
            this.isShow = false
            this.$emit('unloadController', { type: 'unload', name: '卸载', is_manual: true })
        }
    }
</script>

<style lang="scss" scoped>
    .hand-movement-content {
        /* stylelint-disable selector-class-pattern */
        display: flex;
        flex-direction: column;
        /deep/ .el-radio-button {
            border: 4px solid #f4f5f8;
        }
        /deep/ .el-radio-button__inner {
            height: 30px;
        }
    }
    .custom-step {
        display: flex;
        position: relative;
        .step-number {
            width: 24px;
            height: 24px;
            text-align: center;
            line-height: 24px;
            border-radius: 50%;
            color: #ffffff;
            z-index: 1;
            vertical-align: top;
            background-color: #ffffff;
            border-color: #ffffff;
            margin-right: 8px;
        }
        .step-content {
            flex: 1;
            width: 0;
            padding-bottom: 24px;
            .step-content-title {
                color: #475468;
                font-size: 14px;
                height: 22px;
                line-height: 22px;
            }
            .step-result {
                margin-top: 12px;
                padding: 12px;
                border-radius: 2px;
                background: #F4F5F8;
                display: flex;
                .operate-icon-copy {
                    margin-right: 8px;
                    cursor: pointer;
                    display: inline-block;
                }
            }
            .download-text {
                font-size: 14px;
                cursor: pointer;
                color: #1272ff;
                margin: 15px 0 10px 0;
            }
        }
    }
    .custom-step-space {
        &::after {
            content: "";
            position: absolute;
            left: 12px;
            top: 32px;
            height: calc(100% - 40px);
            width: 1px;
            background-color: #F4F5F8;
        }
    }
    .show-result {
        flex: 1;
        height: 0;
        overflow: auto;
        position: relative;
        .text-box {
            width: 100%;
            max-height: none;
            min-height: 22px;
            line-height: 18px;
            font-size: 12px;
            color: #B2BDCC;
            overflow-x: hidden;
            overflow-y: auto;
            word-break: break-all;
            padding-right: 10px;
        }
    }
</style>
