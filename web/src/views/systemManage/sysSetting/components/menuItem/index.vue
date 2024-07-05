<template>
    <draggable
        v-model="menuList"
        :options="{ group: 'menus', animation: 150, draggable: '.menu-item' }"
        @change="handleChange">
        <template v-for="childData in menuList">
            <div :key="childData.id" class="menu-item">
                <div class="menu-item-row">
                    <i class="icon" :class="childData.isUrl ? 'el-icon-link' : childData.isPage ? 'el-icon-tickets' : 'el-icon-folder-opened'"></i>
                    <template v-if="!childData.isEdit">
                        <span>{{ childData.name }}</span>
                        <span
                            class="cw-icon weops-edit"
                            @click="handleEditStatus(childData, true)"></span>
                    </template>
                    <template v-else>
                        <div class="menu-name-input">
                            <el-input
                                size="small"
                                style="width: 200px;"
                                :class="{ 'error-tip': !childData.name && editConfrim }"
                                :clearable="true"
                                placeholder="请输入"
                                v-model="childData.name"
                                @enter="handleConfirmEdit(childData)" />
                            <el-tooltip v-if="!childData.name && editConfrim" effect="dark" content="请输入名称" placement="top">
                                <span>
                                    <i class="el-icon-info"></i>
                                </span>
                            </el-tooltip>
                        </div>
                        <span
                            class="cw-icon weops-complete ml10"
                            @click="handleConfirmEdit(childData)"></span>
                    </template>
                    <div :class="{ 'page-icon': true, 'sys-page-icon': childData.id === 'SysSetting' }">
                        <span v-if="childData.isUrl">外链</span>
                        <span v-if="childData.isPage && !childData.isUrl">(原始页面: {{ childData.originName }})</span>
                        <el-popconfirm
                            width="288px"
                            :title="'确认要删除这个' + (childData.isPage ? '页面' : '目录下所有的页面') + '吗？'"
                            icon="el-icon-info"
                            icon-color="red"
                            @confirm="handleDelete(childData)"
                        >
                            <i v-if="childData.id !== 'SysSetting'" class="el-icon-close delete" slot="reference"></i>
                        </el-popconfirm>
                    </div>
                </div>
                <menu-item
                    v-if="childData.children"
                    :all-menu="allMenu"
                    :menu="childData.children"
                    @delete="deleteMenuItem"
                    @edit-external-chain="editExternalChain"
                    @change="(menu) => changeMenuItem(menu, childData)" />
            </div>
        </template>
    </draggable>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss">
@import "./index.scss"
</style>
