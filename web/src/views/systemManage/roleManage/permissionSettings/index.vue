<template>
    <drawer-component
        :title="`权限管理-${role.name || '--'}`"
        :visible="isShow"
        :size="850"
        custom-class="common-dialog-wrapper"
        @changeVisible="changeVisible">
        <div slot="content" class="common-dialog-wrapper-main">
            <menu-tab :panels="panels" :active-panel="active" @click="toTabMenu" :before-leave="beforeLeave"></menu-tab>
            <div class="main-box" v-loading="loading" v-if="isShow">
                <operation-permission
                    v-if="active === 'operationPermission'"
                    :role="role"
                    ref="menuPermission"
                    @getMenuLoading="getMenuLoading"
                    @getLatestMenu="getLatestMenu"
                    @getPermissions="getPermissions"
                    @getRawIds="getRawIds"
                >
                </operation-permission>
                <instance-permission
                    v-if="active === 'instancePermission'"
                    :role="role"
                    ref="instancePermission">
                </instance-permission>
            </div>
        </div>
        <template slot="footer">
            <el-button
                v-if="active !== 'instancePermission'"
                :disabled="disableBtn || loading"
                type="primary"
                size="small"
                @click="confirm">
                确定
            </el-button>
        </template>
    </drawer-component>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss">
@import "./index.scss"
</style>
