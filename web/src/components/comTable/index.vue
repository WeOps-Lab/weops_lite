<template>
    <div :key="tableKey" class="table-container" :class="{ 'border-none': noneBorder }">
        <el-table
            ref="table"
            v-bind="$attrs"
            :default-expand-all="defaultExpandAll"
            :row-key="rowKey"
            :expand-row-keys="expandRowKeys"
            :size="size"
            @select="onselect"
            @cell-click="cellClick"
            @row-click="rowClick"
            @select-all="selectAll"
            @selection-change="selectChange"
            @sort-change="sortChange"
            @filter-change="filterChange"
            @expand-change="expandChange"
            @cell-mouse-enter="cellMouseEnter"
            @cell-mouse-leave="cellMouseLeave">
            <template v-for="column in setting.selectFields">
                <el-table-column
                    v-if="['selection', 'index'].includes(column.type)"
                    v-bind="column"
                    :key="column.type + '_opertion'"
                >
                </el-table-column>
                <el-table-column
                    v-else
                    v-bind="column"
                    :key="column.key"
                    :show-overflow-tooltip="column.noNeedTip ? false : true"
                    :prop="column.key"
                    :column-key="column.key"
                    :filter-method="column.filters ? (value, row, col) => columnFilterMethod(value, row, col, column.filterRemote) : undefined"
                    :render-header="column.renderHeader">
                    <template slot-scope="props">
                        <template v-if="column.scopedSlots">
                            <slot :name="column.scopedSlots" :row="props.row" :colKey="column.key" :index="props.$index"></slot>
                        </template>
                        <span v-else>{{ props.row[column.key] || (props.row[column.key] === 0 ? props.row[column.key] : '--')}}</span>
                    </template>
                </el-table-column>
            </template>
            <el-table-column v-if="showSetting" fixed="right" align="left" width="40">
                <template slot="header">
                    <div class="setting" @click="showPopover">
                        <i class="el-icon-s-tools"></i>
                    </div>
                </template>
            </el-table-column>
            <template slot="empty">
                <slot name="empty"></slot>
            </template>
        </el-table>
        <div class="pagination_box" v-if="pagination.count">
            <el-pagination
                background
                :current-page.sync="pagination.current"
                :page-sizes="[10, 20, 50, 100]"
                :page-size="pagination.limit"
                layout="total, sizes, next, pager, prev"
                :total="pagination.count"
                :small="pagination.small"
                @size-change="limitChange"
                @current-change="handlePageChange">
            </el-pagination>
        </div>
        <div v-if="showSetting" class="table-content-setting">
            <el-dialog
                title="列表字段设置"
                append-to-body
                :close-on-click-modal="false"
                :destroy-on-close="false"
                :visible.sync="settingVisible"
                width="800px">
                <div class="setting-fields-checkout-group">
                    <div class="source-list">
                        <div class="header">待选择列表</div>
                        <div class="content-box">
                            <div class="organization-box">
                                <div class="mb10 mt10">
                                    <el-checkbox
                                        :indeterminate="indeterminate"
                                        v-model="isCheckAll"
                                        @change="changeAllCheck">
                                        全选
                                    </el-checkbox>
                                </div>
                                <el-checkbox-group
                                    v-model="settingKeys"
                                    @change="changeCheckbox">
                                    <el-checkbox
                                        :key="item.key"
                                        :label="item.key"
                                        :disabled="item.disabled"
                                        v-for="item in setting.fields">
                                        <span :title="item.label">{{ item.label }}</span>
                                    </el-checkbox>
                                </el-checkbox-group>
                            </div>
                        </div>
                    </div>
                    <div class="selection-container">
                        <p>已选择（共<span>{{ settingKeys.length }}</span>条）<span class="clear" @click="deleteAllField">清空</span></p>
                        <ul>
                            <draggable
                                v-if="settingKeys.length"
                                :list="settingKeys"
                                :scroll="true"
                                animation="500"
                                handle=".mover"
                                ghost-class="ghost"
                                force-fallback="true">
                                <li v-for="item in settingKeys" :key="item">
                                    <span class="cw-icon weops-drag-drop mover"></span>
                                    {{ showFieldName(item) }}
                                    <i class="el-icon-close" style="font-size: 12px;" @click="deleteField(item)"></i>
                                </li>
                            </draggable>
                        </ul>
                    </div>
                </div>
                <span slot="footer" class="dialog-footer">
                    <el-button size="small" @click="hidePopover">取 消</el-button>
                    <el-button size="small" type="primary" @click="confirmPopover">确 定</el-button>
                </span>
            </el-dialog>
        </div>
    </div>
</template>

<script lang="ts" src="./index.ts"></script>

<style scoped lang="scss" scope>
@import "./index.scss"
</style>
