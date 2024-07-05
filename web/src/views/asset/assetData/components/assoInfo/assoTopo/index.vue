<template>
    <div class="asso-topo" v-loading="loading">
        <el-empty
            v-if="isEmpty"
            :image-size="80"
            class="exception-wrap-item exception-part"
            description="暂无数据"
        >
        </el-empty>
        <div v-else class="topo" ref="canvasRef"></div>
        <drawer-component
            :title="`实例详情-${currentModelCfg.inst_name}`"
            :size="800"
            :visible="visible"
            destroy-on-close
            custom-class="common-dialog-wrapper"
            :before-close="beforeCloseDialog">
            <div slot="content" class="content-box common-dialog-wrapper-main">
                <base-info
                    :group-list="groupList"
                    :user-list="userList"
                    :current-model-cfg="currentModelCfg"
                    display-percent="50%"
                >
                </base-info>
            </div>
            <div slot="footer">
                <el-button
                    size="small"
                    @click="beforeCloseDialog">
                    关闭
                </el-button>
            </div>
        </drawer-component>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
