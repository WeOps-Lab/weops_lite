<template>
    <div class="asso-list" v-loading="loading">
        <div class="operate-box">
            <div class="operate-box-left">
                <el-button
                    v-permission="operatePower"
                    :type="'primary'"
                    size="small"
                    @click="addRelation">
                    新建关联
                </el-button>
                <el-button
                    size="small"
                    @click="expandAll(true)">
                    全部展开
                </el-button>
                <el-button
                    size="small"
                    @click="expandAll(false)">
                    全部收起
                </el-button>
            </div>
        </div>
        <div class="asso-list-main">
            <collapse :collapse-list="resourcList">
                <template slot="content" slot-scope="{ collRow }">
                    <com-table
                        v-if="showTable(collRow)"
                        ref="comTable"
                        :data="collRow.list"
                        :columns="collRow.columns"
                        :max-height="tableMaxHeight"
                    >
                        <template slot="operation" slot-scope="{ row }">
                            <el-button
                                v-permission="operatePower"
                                class="mr10"
                                type="text"
                                size="small"
                                @click="cancelRelate(row)"
                            >
                                取消关联
                            </el-button>
                        </template>
                        <template v-for="field in collRow.slotColumns" :slot="field.scopedSlots" slot-scope="{ row }">
                            <div :key="field.key">
                                <el-tag
                                    v-if="field.attr_type === 'bool'"
                                    :type="row[field.key] ? 'success' : ''">
                                    {{getShowValue(field, row)}}
                                </el-tag>
                                <span v-else>{{ getShowValue(field, row) }}</span>
                            </div>
                        </template>
                    </com-table>
                </template>
            </collapse>
            <el-empty
                v-if="!resourcList.length"
                :image-size="80"
                class="exception-wrap-item exception-part"
                description="暂无数据"
            >
            </el-empty>
        </div>
        <add-relation
            ref="addRelation"
            :connect-type-list="connectTypeList"
            :model-info-list="modelInfoList"
            :group-list="groupList"
            :user-list="userList"
            :inst-info="instInfo"
            @refreshList="initData"
        />
    </div>
</template>

<script lang="ts" src="./index.ts"></script>
<style lang="scss" scoped>
.asso-list {
    .asso-list-main {
        height: calc(100vh - 300px);
        overflow: auto;
    }
}
</style>
