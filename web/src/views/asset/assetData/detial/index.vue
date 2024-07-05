<template>
    <div class="asset-detial page-container" v-loading="loading">
        <el-tabs v-model="active" @tab-click="handleTabClick">
            <el-tab-pane
                v-for="(item,index) in panels"
                :key="index"
                :label="item.label"
                :name="item.name">
            </el-tab-pane>
            <asso-info
                v-if="['assoInfo','assetCredential'].includes(active) && !loading"
                :key="active"
                :inst-info="{
                    model_type: active === 'assoInfo' ? 'base' : 'credential'
                }"
                :group-list="groupList"
                :connect-type-list="connectTypeList"
                :model-info-list="modelInfoList"
                :user-list="userList"
                :property-list="propertyList" />
            <base-info
                v-if="active === 'baseInfo' && !loading"
                :user-list="userList"
                :group-list="groupList"
                :property-list="propertyList"
            />
            <asset-record
                v-if="active === 'assetRecord' && !loading"
                :user-list="userList"
                :group-list="groupList"
                :property-list="propertyList"
                :model-info-list="modelInfoList"
                :connect-type-list="connectTypeList"
            />
        </el-tabs>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
