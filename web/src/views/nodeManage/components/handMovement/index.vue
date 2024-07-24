<template>
    <drawer-component
        :title="`手动${detail.inner_ip}`"
        :size="650"
        :visible="isShow"
        destroy-on-close
        :before-close="beforeCloseDialog">
        <div
            class="common-dialog-wrapper-main"
            slot="content"
            v-loading="loading">
            <div class="mb10" style="font-size: 14px;color: #63656e;font-weight: 700;">
                安装方式:
            </div>
            <el-radio-group
                v-model="system"
                size="small"
                class="mb10"
                @input="handlerChange">
                <el-radio-button
                    v-for="(item, index) in systemList"
                    :key="index"
                    :label="item">
                    {{ item }}
                </el-radio-button>
            </el-radio-group>
            <el-radio-group
                v-model="installWay"
                size="small"
                class="mb10"
                @input="handlerChange">
                <el-radio-button
                    v-for="(item, index) in commandList"
                    :key="index"
                    :label="item.type">
                    {{ item.type_name }}
                </el-radio-button>
            </el-radio-group>
            <el-alert
                class="mb10"
                type="info"
                :title="installDescription">
            </el-alert>
            <div class="show-result">
                <div v-if="commands.length" class="text-box">
                    <div
                        v-for="(item, index) in commands"
                        :class="['custom-step', index !== commands.length - 1 && 'custom-step-space']"
                        :key="index">
                        <div class="step-number">{{index + 1}}</div>
                        <div class="step-content">
                            <div class="step-content-title">{{item.description}}</div>
                            <div v-if="item.type === 'commands'" class="step-result">
                                <div
                                    v-for="(tex, i) in item.contents"
                                    style="position: relative;"
                                    :key="i">
                                    <i
                                        v-copy="tex.text"
                                        class="operate-icon-copy el-icon-document-copy">
                                    </i>
                                    <span>{{tex.text}}</span>
                                </div>
                            </div>
                            <div v-else>
                                <div class="mt10">
                                    <span style="font-size: 12px;color: #63656e;">
                                        文件列表：
                                    </span>
                                    <span class="download-text" @click="downloadAllFile(item.contents)">
                                        下载全部
                                        <i class="el-icon-download"></i>
                                    </span>
                                </div>
                                <com-table
                                    ref="ComTable"
                                    class="mt5"
                                    :data="item.contents"
                                    :columns="columns"
                                    :max-height="400">
                                    <template slot="downLoad" slot-scope="{ row }">
                                        <span style="color: var(--primary-6);cursor: pointer;" @click="downloadFile(row.text)">{{row.name}}</span>
                                    </template>
                                </com-table>
                            </div>
                        </div>
                    </div>
                </div>
                <el-empty v-else description="暂无数据" :image-size="80"></el-empty>
            </div>
        </div>
        <template slot="footer">
            <el-button
                type="default"
                size="small"
                @click="beforeCloseDialog">
                关闭
            </el-button>
        </template>
    </drawer-component>
</template>

<script lang="ts">
    import { Vue, Component, Prop } from 'vue-property-decorator'
    import ComTable from '@/components/comTable/index.vue'
    import DrawerComponent from '@/components/comDrawer/index.vue'
    @Component({
        name: 'hand-movement',
        components: {
            ComTable,
            DrawerComponent
        }
    })
    export default class handMovement extends Vue {
        @Prop({
            type: [Number, String],
            default: () => ''
        })
        jobId: number | string
        isShow: boolean = false
        detail: any = {}
        commands: string = ''
        loading: boolean = false
        installWay: string = ''
        installDescription: string = ''
        commandList: any[] = []
        systemList: any[] = ['Linux', 'Windows']
        system: string = 'Linux'
        columns = [
            {
                label: '文件名称',
                key: 'description',
                align: 'left',
                minWidth: '100'
            },
            {
                label: '文件下载',
                key: 'downLoad',
                align: 'left',
                minWidth: '100',
                scopedSlots: 'downLoad'
            }
        ]
        beforeCloseDialog() {
            this.isShow = false
        }
        show(row) {
            this.isShow = true
            this.detail = row
            this.getManagementCommands()
        }
        async downloadAllFile(fileList) {
            for (const item of fileList) {
                await new Promise(resolve => {
                    const element = document.createElement('a')
                    element.setAttribute('href', item.text)
                    element.setAttribute('download', item.name)
                    element.style.display = 'none'
                    document.body.appendChild(element)
                    element.click()
                    document.body.removeChild(element)
                    setTimeout(resolve, 100) // 延迟100毫秒
                })
            }
        }
        downloadFile(url) {
            window.open(url)
        }
        handlerChange() {
            const target = this.commandList.find(item => item.type === this.installWay)
            this.commands = target.steps
            this.installDescription = target.description
        }
        getManagementCommands() {
            // this.loading = true
            this.$api.agentManage.getManagementCommands({
                job_id: this.jobId,
                bk_host_id: this.detail.bk_host_id
            }).then(res => {
                const { result, data } = res
                if (!result) {
                    return false
                }
                this.commandList = data.solutions
                if (this.commandList[0]) {
                    this.installWay = this.commandList[0].type
                    this.installDescription = this.commandList[0].description
                    this.commands = this.commandList[0].steps
                }
            }).finally(() => {
                this.loading = false
            })
        }
    }
</script>

<style lang="scss" scoped>
    .custom-step {
        display: flex;
        position: relative;
        .step-number {
            width: 24px;
            height: 24px;
            text-align: center;
            line-height: 24px;
            border-radius: 50%;
            color: #fff;
            z-index: 1;
            vertical-align: top;
            background-color: #1272ff;
            border-color: #1272ff;
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
                position: relative;
                padding: 12px 12px 12px 40px;
                border-radius: 2px;
                background: #F4F5F8;
                .bk-icon {
                    position: absolute;
                    top: 4px;
                    left: -24px;
                    font-size: 13px !important;
                    cursor: pointer;
                }
            }
            .download-text {
                font-size: 14px;
                cursor: pointer;
                color: #1272ff;
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
