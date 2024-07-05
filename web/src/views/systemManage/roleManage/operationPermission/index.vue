<template>
    <div class="operation-permission" v-loading="menuLoading">
        <div class="table-header">
            <div class="menu-box">菜单</div>
            <div class="operate-auth">操作权限</div>
        </div>
        <div class="table-body">
            <div class="menu-list" v-for="item in menuList" :key="item.id">
                <div class="first-level-box" @click="setExpandStatus(item)">
                    <div class="menu-name">
                        <i
                            v-if="item.children"
                            class="expand-icon"
                            :class="item.isExpand ? 'el-icon-caret-bottom' : 'el-icon-caret-right'">
                        </i>
                        <el-checkbox
                            :class="['check-box', !item.children && 'check-box-left']"
                            :indeterminate="item.isIndeterminate"
                            v-model="item.isChecked"
                            @click.stop.native="() => {}"
                            @change="handleMenuChecked(item)"
                        >
                        </el-checkbox>
                        <span>{{item.name}}</span>
                    </div>
                    <div v-if="item.auth" class="menu-operate">
                        <div v-for="(authItem, authIndex) in item.auth" :key="authIndex">
                            <el-checkbox
                                class="check-box"
                                v-model="authItem.value"
                                :indeterminate="authItem.isIndeterminate"
                                @click.stop.native="() => {}"
                                @change="handleOperateChecked(item, authItem.type)"
                            >
                            </el-checkbox>
                            <span v-overflow-tooltip>{{authItem.label}} </span>
                        </div>
                    </div>
                </div>
                <div v-if="item.isExpand">
                    <div v-for="tex in item.children" :key="tex.id">
                        <div class="second-level-box" @click="setExpandStatus(tex)">
                            <div class="menu-name" style="padding-left: 40px;">
                                <!--                        down-shape-->
                                <i v-if="tex.children" class="expand-icon" :class="tex.isExpand ? 'el-icon-caret-bottom' : 'el-icon-caret-right'" />
                                <el-checkbox
                                    :class="['check-box', !tex.children && 'check-box-left']"
                                    :indeterminate="tex.isIndeterminate"
                                    v-model="tex.isChecked"
                                    @change="handleMenuChecked(tex)"
                                    @click.stop.native="() => {}"
                                >
                                </el-checkbox>
                                <span>{{tex.name}}</span>
                            </div>
                            <div v-if="tex.auth" class="menu-operate">
                                <div v-for="(authTex, authTexIndex) in tex.auth" :key="authTexIndex">
                                    <el-checkbox
                                        class="check-box"
                                        :indeterminate="authTex.isIndeterminate"
                                        v-model="authTex.value"
                                        @click.stop.native="() => {}"
                                        @change="handleOperateChecked(tex, authTex.type)"
                                    >
                                    </el-checkbox>
                                    <span v-overflow-tooltip>{{authTex.label}}</span>
                                </div>
                            </div>
                        </div>
                        <div v-if="tex.isExpand">
                            <div class="third-level-box" v-for="nev in tex.children" :key="nev.id">
                                <div class="menu-name" style="padding-left: 90px;">
                                    <el-checkbox
                                        :class="['check-box']"
                                        :indeterminate="nev.isIndeterminate"
                                        v-model="nev.isChecked"
                                        @change="handleMenuChecked(nev)"
                                    >
                                    </el-checkbox>
                                    <span>{{nev.name}}</span>
                                </div>
                                <div v-if="nev.auth" class="menu-operate">
                                    <template v-for="(authNev, authNevIndex) in nev.auth">
                                        <div :key="authNevIndex">
                                            <el-checkbox
                                                class="check-box"
                                                v-model="authNev.value"
                                                @change="handleOperateChecked(nev, authNev.type)"
                                            >
                                            </el-checkbox>
                                            <span v-overflow-tooltip>{{authNev.label}}</span>
                                        </div>
                                    </template>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss">
@import "./index.scss"
</style>
