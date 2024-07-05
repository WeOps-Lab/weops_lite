<template>
    <div>
        <el-container>
            <!-- 头部 -->
            <el-header>
                <div class="navigation-header">
                    <div class="navigation-title">
                        <div class="monitor-logo" @click="goHome">
                            <img :src="'data:image/png;base64,' + nav.logo" height="40" width="40" :alt="'logo图片'">
                        </div>
                        <span class="title-desc">WeOps</span>
                    </div>
                    <div class="header-right">
                        <div class="monitor-navigation-header">
                            <ul class="top-nav">
                                <li
                                    v-for="item in menuList"
                                    :key="item.id"
                                    :class="['top-nav-item', activeTopNav === item.id && 'active-top-nav']"
                                    @click="changeTopNav(item)">
                                    {{item.name}}
                                </li>
                            </ul>
                            <div class="other-info">
                                <el-popover
                                    placement="top-start"
                                    trigger="hover"
                                    popper-class="header-popper">
                                    <div class="header-user is-left" slot="reference">
                                        <el-tooltip :content="user.chname" :disabled="isShowTooltip" placement="bottom" effect="dark">
                                            <div
                                                @mouseover="onMouseOver"
                                                style="max-width: 100px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;"
                                            >
                                                <span ref="strRef">{{user.chname}}</span>
                                            </div></el-tooltip>
                                        <i class="el-icon-caret-bottom"></i>
                                    </div>
                                    <ul class="monitor-navigation-admin" ref="userList">
                                        <li class="nav-item" @click="checkPersonalInfo">
                                            个人信息
                                        </li>
                                        <li class="nav-item" @click="outLogin">
                                            退出登录
                                        </li>
                                    </ul>
                                </el-popover>
                            </div>
                        </div>
                    </div>
                </div>
            </el-header>
            <el-container>
                <!-- 侧边导航栏 -->
                <el-aside width="auto">
                    <el-menu v-if="needLeftNav"
                        class="el-menu-vertical"
                        :default-active="defaultActive"
                        :collapse="!open && defaultOpen"
                        text-color="#7588a3"
                        background-color="#f4f5f8"
                        active-text-color="#409eff"
                        :unique-opened="true"
                        @select="handleSelect">
                        <template v-for="item in leftNavList">
                            <!-- 有子菜单 -->
                            <el-submenu
                                v-if="item.children && !!item.children.length"
                                :index="item.id"
                                :key="item.name"
                                @click="handleNavItemClick(item)">
                                <template slot="title">
                                    <i :class="[item.icon || 'cw-icon weops-folder', 'icon-class']"></i>
                                    <span>{{ item.name }}</span>
                                </template>
                                <el-menu-item v-for="child in item.children" :key="child.name" :index="child.id" @click="handleNavItemClick(child)">
                                    <template slot="title">
                                        <i class="cw-icon icon-class"></i>
                                        <span>{{ child.name }}</span>
                                    </template>
                                </el-menu-item>
                            </el-submenu>
                            <!-- 没有子菜单 -->
                            <el-menu-item
                                v-else
                                :index="item.id"
                                :key="item.name"
                                @click="handleNavItemClick(item)">
                                <i :class="[item.icon || 'cw-icon weops-folder', 'icon-class']"></i>
                                <span slot="title">{{ item.name }}</span>
                            </el-menu-item>
                        </template>
                        <div class="nav-slider-footer">
                            <i :class="['cw-icon',open ? 'weops-navigation-indent' : 'weops-navigation-expand']" @click="handleIconCLick"></i>
                        </div>
                    </el-menu>
                </el-aside>
                <!-- 主体部分 -->
                <el-main>
                    <Container :key="renderKey" :nav-toggle="nav.toggle" :user="user"></Container>
                    <personal-info ref="personalInfo"></personal-info>
                </el-main>
            </el-container>
        </el-container>

    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style lang="scss" scoped>
@import "./index.scss"
</style>
<!-- 改Popover弹出框样式 -->
<style lang="scss">
@import "./other.scss"
</style>
