<template>
    <div
        class="assets-overview page-container"
        v-loading="pageLoading">
        <el-input
            v-model="searchValue"
            style="width: 300px;"
            :clearable="true"
            size="small"
            :right-icon="'bk-icon icon-search'"
            placeholder="请输入关键字"
            suffix-icon="el-icon-search"
            @change="filterList"
            @clear="filterList">
        </el-input>
        <div ref="overviewList" class="overview-list">
            <waterfall
                v-if="isHideList"
                :col="4"
                :gutter-width="20"
                :data="showMenusList">
                <div
                    v-for="item in showMenusList"
                    :key="item.classification_id"
                    class="overview-item">
                    <div class="title">
                        {{item.classification_name}}
                    </div>
                    <div class="model-list">
                        <div
                            v-for="tex in item.children"
                            :key="tex.model_id"
                            class="model-item"
                            @click="goAssetRecord(item, tex)">
                            <div>
                                <img :src="tex.icon" alt="">
                                <span>{{tex.model_name}}</span>
                            </div>
                            <div class="count">{{tex.count || 0}}</div>
                        </div>
                    </div>
                </div>
            </waterfall>
            <el-empty
                v-if="!showMenusList.length"
                :image-size="80"
                class="exception-wrap-item exception-part"
                description="暂无数据"
            >
            </el-empty>
        </div>
    </div>
</template>

<script lang="ts">
    import {Vue, Component} from 'vue-property-decorator'
    import waterfall from 'vue-waterfall2'
    import { underscoreToCamelCase } from '@/common/dealMenu'
    import vue from 'vue'
    vue.use(waterfall)
    @Component({})
    export default class AssetsOverview extends Vue {
        pageLoading: boolean = false
        menusList: any[] = []
        showMenusList: any[] = []
        searchValue: string = ''
        isHideList: boolean = true
        classification: any[] = []

        mounted() {
            this.handleAssetsOverview()
        }
        filterList() {
            this.isHideList = false
            this.$nextTick(() => {
                this.isHideList = true
                this.showMenusList = []
                if (!this.searchValue) {
                    this.showMenusList = JSON.parse(JSON.stringify(this.menusList))
                    return false
                }
                const list = JSON.parse(JSON.stringify(this.menusList))
                list.forEach(item => {
                    item.children = item.children.filter(tex => tex.model_name.toLowerCase().includes(this.searchValue.toLowerCase()))
                })
                this.showMenusList = list.filter(item => item.children.length)
            })
        }
        goAssetRecord(item, tex) {
            this.$router.push({
                name: underscoreToCamelCase(item.classification_id),
                query: {
                    modelId: tex.model_id
                }
            })
        }
        initMenus() {
            this.menusList = [
                {
                    id: 'bk_host_manage',
                    name: '主机管理',
                    children: []
                }
            ]
            for (const k in this.classification) {
                this.menusList.push({
                    classification_id: k.classification_id,
                    classification_name: this.classification[k.classification_name],
                    children: []
                })
            }
        }
        getIconUrl(tex) {
            try {
                return require(`@/assets/svg/model/${tex.icn || 'cc-default_默认'}.svg`)
            } catch (e) {
                return require('@/assets/svg/model/cc-default_默认.svg')
            }
        }
        handleAssetsOverview() {
            this.pageLoading = true
            Promise.all([this.getModelInfoList(), this.getClassification(), this.getModelInstCount()]).then(res => {
                const [
                    { result: listResult, message: listMessage, data: listData },
                    { result: classificationResult, message: classificationMessage, data: classificationData },
                    { result: countResult, message: countMessage, data: countData }
                ] = res
                if (!listResult) {
                    this.$error(listMessage)
                    return false
                }
                if (!classificationResult) {
                    this.$error(classificationMessage)
                    return false
                }
                if (!countResult) {
                    this.$error(countMessage)
                    return false
                }
                this.classification = classificationData
                this.initMenus()
                Object.values(listData).forEach((item: any) => {
                    this.$set(item, 'icon', this.getIconUrl(item))
                    item.count = countData[item.model_id] || 0
                })
                this.menusList = this.classification.map(item => {
                    item.children = listData.filter(tex => tex.classification_id === item.classification_id && tex.model_name)
                    return item
                })
                this.menusList = this.menusList.filter(item => item.children.length)
                this.showMenusList = JSON.parse(JSON.stringify(this.menusList))
            }).finally(() => {
                this.pageLoading = false
            })
        }
        getModelInfoList() {
            return this.$api.ModelManage.getModel()
        }
        getClassification() {
            return this.$api.ModelManage.getClassification()
        }
        getModelInstCount() {
            return this.$api.AssetData.getModelInstCount()
        }
    }
</script>

<style lang="scss" scoped>
    .assets-overview {
        display: flex;
        flex-direction: column;
        .overview-list {
            padding-top: 16px;
            height: calc(100vh - 120px);
            overflow-y: scroll;
            /deep/ .vue-waterfall-column {
                width: calc((100% - 60px) / 4) !important;
            }
            /deep/ .vue-waterfall.is-transition img {
                opacity: 1 !important;
            }
            .overview-item {
                box-sizing: border-box;
                padding: 15px;
                margin-bottom: 20px;
                border-radius: 8px;
                border: 1px solid #edeff3;
                background: #fff;
                .title {
                    font-weight: 700;
                    padding-bottom: 15px;
                    border-bottom: 1px solid #edeff3;
                }
                .model-list {
                    font-size: 13px;
                    margin-top: 10px;
                    .model-item {
                        display: flex;
                        justify-content: space-between;
                        height: 38px;
                        line-height: 38px;
                        cursor: pointer;
                        padding: 0 10px;
                        border-radius: 2px;
                        &:hover {
                            background-color: #edeff3;
                        }
                        .count {
                            color: #7588a3;
                        }
                        img {
                            width: 20px;
                            height: 20px;
                            margin-right: 5px;
                            position: relative;
                            top: 4px;
                        }
                    }
                }
            }
        }
    }
</style>
