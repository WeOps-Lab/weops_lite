<template>
    <div>
        <drawer-component
            v-loading="pageLoading"
            :title="`${isAdd ? '新增' : '编辑'}资产权限`"
            :visible="isShow"
            :size="800"
            destroy-on-close
            append-to-body
            :before-close="beforeCloseDialog">
            <div slot="content" class="common-dialog-wrapper-main">
                <el-form
                    label-width="110"
                    :model="formData"
                    :rules="rules"
                    ref="validateForm"
                >
                    <el-form-item
                        label="应用模型"
                        prop="model_id">
                        <el-select
                            class="form-item"
                            v-model="formData.model_id"
                            size="small"
                            @change="searchInstList"
                        >
                            <el-option v-for="option in modelList"
                                :key="option.model_id"
                                :label="option.model_name"
                                :value="option.model_id">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item
                        label="权限类型"
                        prop="permission_type">
                        <el-checkbox
                            v-for="item in permissionTypeList"
                            :true-label="1"
                            :false-label="0"
                            :key="item.id"
                            v-model="item.value"
                            class="mr20"
                            @change="changeCheckbox(item)">
                            {{item.label}}
                        </el-checkbox>
                    </el-form-item>
                    <el-form-item
                        label="资产范围"
                        prop="resource_type">
                        <el-select
                            class="form-item"
                            v-model="formData.resource_type"
                            size="small"
                            @change="changeResourceType">
                            <el-option v-for="option in resourceTypeList"
                                :key="option.id"
                                :label="option.name"
                                :value="option.id">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item
                        v-if="isAssetRange"
                        label="资产实例"
                        prop="instance">
                        <el-button
                            :disabled="!formData.model_id || attrLoading"
                            size="small"
                            :type="'primary'"
                            @click="addInstance">
                            新增实例
                        </el-button>
                        <el-button
                            type="default"
                            size="small"
                            :disabled="!selectedInstances.length"
                            @click="deleteInstance(selectedInstances)">
                            批量删除
                        </el-button>
                        <com-table
                            v-show="instColumns.length"
                            class="mt10"
                            ref="comTable"
                            :data="formData.instanceList"
                            :columns="instColumns"
                            :height="tableHeight"
                            @select="handleSelect"
                            @select-all="handleSelect"
                        >
                            <template slot="operation" slot-scope="{ row }">
                                <el-button
                                    type="text"
                                    size="small"
                                    @click="deleteInstance([row])">
                                    移除
                                </el-button>
                            </template>
                            <template v-for="field in slotColumns" :slot="field.scopedSlots" slot-scope="{ row }">
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
                    </el-form-item>
                    <el-form-item
                        v-else
                        label="匹配条件"
                        prop="conditions">
                        <div class="rule-box">
                            <div class="first-level"
                                v-for="(item, index) in formData.conditions"
                                :key="item.id">
                                <div
                                    class="second-level"
                                    v-for="(tex, i) in item.child"
                                    :key="tex.id">
                                    <div :class="['tag mr10', i !== 0 && 'and-tag']">且</div>
                                    <condition-item
                                        :property-list="attrList"
                                        :user-list="userList"
                                        :group-list="groupList"
                                        :config="tex" />
                                    <i class="el-icon-circle-plus-outline ml10" @click="operateSecondRule('add', item)"></i>
                                    <i
                                        v-if="item.child.length > 1"
                                        class="el-icon-remove-outline ml5"
                                        @click="operateSecondRule('delete', item, i)">
                                    </i>
                                </div>
                                <div v-if="index === formData.conditions.length - 1" class="add-icon-box">
                                    <i class="el-icon-plus" @click="operateFirstRule('add')" />
                                </div>
                                <div v-else class="tag or-tag">
                                    或
                                </div>
                                <i
                                    v-if="formData.conditions.length > 1"
                                    class="el-icon-remove-outline delete-icon-first"
                                    @click="operateFirstRule('delete', index)" />
                            </div>
                        </div>
                    </el-form-item>
                </el-form>
            </div>
            <template slot="footer">
                <el-button
                    type="primary"
                    size="small"
                    @click="confirm">
                    确定
                </el-button>
                <el-button
                    type="default"
                    size="small"
                    @click="beforeCloseDialog">
                    取消
                </el-button>
            </template>
        </drawer-component>
        <add-instance
            ref="addInstance"
            :slot-columns="slotColumns"
            :group-list="groupList"
            :user-list="userList"
            :attr-list="attrList"
            :instance-columns="instColumns"
            :model-id="formData.model_id"
            :role="role"
            @change-list="getSelectList">
        </add-instance>
    </div>
</template>
<script lang="ts">
    import { Vue, Component, Prop } from 'vue-property-decorator'
    import DrawerComponent from '@/components/comDrawer/index.vue'
    import ComTable from '@/components/comTable/index.vue'
    import AddInstance from '../addInstance/index.vue'
    import { COMMON_RULE } from '@/common/constants'
    import { TableData } from '@/common/types'
    import { getAssetAttrValue } from '@/controller/func/common'
    import conditionItem from '../selectInput/index.vue'

@Component({
    name: 'permission-settings',
    components: {
        DrawerComponent,
        ComTable,
        AddInstance,
        conditionItem
    }
})
export default class permissionSettings extends Vue {
    @Prop({
        type: Object,
        default: () => ({})
    })
    role: any

    @Prop({
        type: Array,
        default: () => []
    })
    modelList: Array<any>

    isShow: boolean = false
    pageLoading: boolean = false
    attrLoading: boolean = false
    resourceTypeList: Array<any> = [
        { name: '指定资产', id: 'fixed' },
        { name: '条件筛选', id: 'changing' }
    ]
    initRuleItem: {
            id: number,
            [key: string]: any
    } = {
        id: this.$random(5),
        field: '',
        type: '',
        value: ''
    }
    formData = {
        model_id: '',
        permission_type: '',
        resource_type: 'fixed',
        conditions: [
            {
                id: this.$random(5),
                child: [{
                    ...this.initRuleItem,
                    id: this.$random(5)
                }]
            }
        ],
        instanceList: []
    }
    rules = {
        resource_type: [
            COMMON_RULE
        ],
        permission_type: [
            COMMON_RULE
        ],
        model_id: [
            COMMON_RULE
        ],
        instance: [
            {
                validator: (rule, value, callback) => {
                    if (!this.formData.instanceList.length) {
                        callback(new Error('必填项'))
                    } else {
                        callback()
                    }
                },
                trigger: 'blur'
            }
        ],
        conditions: [
            {
                validator: (rule, value, callback) => this.validateConditions(rule, value, callback),
                trigger: 'blur'
            }
        ]
    }
    instColumns: Array<TableData> = []
    selectedInstances: Array<any> = []
    groupList: Array<any> = []
    userList: Array<any> = []
    attrList: Array<any> = []
    permissionTypeList: Array<any> = [
        {id: 'query', label: '查询', value: 0},
        {id: 'manage', label: '管理', value: 0}
    ]
    instDetail: any = {}

    get isAdd() {
        return this.instDetail.type === 'add'
    }
    get isAssetRange() {
        return this.formData.resource_type === 'fixed'
    }
    get slotColumns() {
        return this.instColumns.filter(item => item.scopedSlots && item.scopedSlots !== 'operation')
    }
    get tableHeight() {
        return 'calc(100vh - 390px)'
    }

    changeResourceType() {
        this.formData.instanceList = []
        this.formData.conditions = [
            {
                id: this.$random(5),
                child: [{
                    ...this.initRuleItem,
                    id: this.$random(5)
                }]
            }
        ]
    }
    validateConditions(rule, value, callback) {
        if (!this.formData.conditions.length) {
            callback(new Error('必填项'))
            return
        }
        for (let index = 0; index < this.formData.conditions.length; index++) {
            for (let childInd = 0; childInd < this.formData.conditions[index].child.length; childInd++) {
                const child = this.formData.conditions[index].child[childInd]
                if (Object.values(child).some(item => !item.length)) {
                    callback(new Error('必填项'))
                    return
                }
            }
        }
        callback()
    }
    operateSecondRule(type, item, i?) {
        if (type === 'add') {
            item.child.push({
                ...this.initRuleItem,
                id: this.$random(5)
            })
            return
        }
        item.child.splice(i, 1)
    }
    operateFirstRule(type, index?) {
        if (type === 'add') {
            this.formData.conditions.push({
                id: this.$random(5),
                child: [
                    {
                        ...this.initRuleItem,
                        id: this.$random(5)
                    }
                ]
            })
        } else {
            this.formData.conditions.splice(index, 1)
        }
    }
    changeCheckbox(option) {
        if (option.id === 'manage') {
            this.setPermissionType('query', 1)
        }
        if (option.id === 'query' && !option.value) {
            this.setPermissionType('manage', 0)
        }
        const checkedIds = this.permissionTypeList.filter(item => item.value).map(item => item.id)
        if (!checkedIds.length) {
            this.formData.permission_type = ''
            return
        }
        this.formData.permission_type = checkedIds.length === 2 ? 'manage' : 'query'
    }
    setPermissionType(id, value) {
        this.permissionTypeList.forEach(item => {
            if (item.id === id) {
                this.$set(item, 'value', value)
            }
        })
    }
    getSelectList(list) {
        this.formData.instanceList = list
    }
    addInstance() {
        const addInstance: any = this.$refs.addInstance
        addInstance.show(this.formData.instanceList)
    }
    searchInstList(val) {
        this.formData.instanceList = []
        this.formData.conditions = [
            {
                id: this.$random(5),
                child: [{
                    ...this.initRuleItem,
                    id: this.$random(5)
                }]
            }
        ]
        this.instColumns = []
        this.attrList = []
        this.getModelAttrList()
    }
    initPage(row) {
        this.pageLoading = true
        if (!this.isAdd) {
            for (const key in row) {
                if (['model_id', 'permission_type', 'resource_type'].includes(key)) {
                    this.formData[key] = row[key]
                }
            }
            this.permissionTypeList.forEach(item => {
                if (this.formData['permission_type'] === 'manage') {
                    item.value = 1
                    return
                }
                if (item.id === 'query') {
                    item.value = 1
                }
            })
            if (!this.isAssetRange) {
                this.formData.conditions = row.conditions.map(item => {
                    item.forEach(children => {
                        if (children.type === 'time') {
                            children.value = [children.start, children.end]
                            return
                        }
                        if (children.type === 'bool') {
                            children.value = children.value ? '1' : '0'
                        }
                    })
                    return {
                        id: this.$random(5),
                        child: item
                    }
                })
            }
            this.getModelAttrList()
        }
        Promise.all([this.getGroups(), this.getUserList(), this.isAssetRange && !this.isAdd && this.getList(row.conditions)]).finally(() => {
            this.pageLoading = false
        })
    }
    async getList(conditions) {
        const params = {
            query_list: conditions[0] || [],
            model_id: this.formData.model_id
        }
        const res = await this.$api.AssetData.getInstanceList(params)
        const { result, data, message } = res
        if (!result) {
            return this.$error(message)
        }
        this.formData.instanceList = data.insts
    }
    async getModelAttrList() {
        if (!this.formData.model_id) {
                return
        }
        this.attrLoading = true
        try {
            const params = {
               id: this.formData.model_id
            }
            const { result, message, data } = await this.$api.ModelManage.getModelAttrList(params)
            if (!result) {
                return this.$error(message)
            }
            this.attrList = data.filter(item => item.attr_type !== 'pwd').map(attr => {
                if (attr.attr_type === 'bool') {
                    attr.option = [
                        {id: '1', name: '是'},
                        {id: '0', name: '否'}
                    ]
                }
                return attr
            })
            const propertyList = this.$copy(data)
            propertyList.forEach(item => {
                item.key = item.attr_id
                item.label = item.attr_name
                item.minWidth = '100px'
                item.align = 'left'
                item.scopedSlots = item.attr_id
            })
            this.instColumns = this.getColumns(propertyList)
            this.$nextTick(() => {
                const resourceTable: any = this.$refs.comTable
                resourceTable?.updateColumns(this.instColumns)
            })
        } finally {
            this.attrLoading = false
        }
    }
    getColumns(list) {
        const operateColumn = {
            label: '操作',
            key: 'operation',
            align: 'left',
            width: '100px',
            fixed: 'right',
            scopedSlots: 'operation'
        }
        return [
            {
                type: 'selection',
                fixed: true
            },
            ...list,
            operateColumn
        ]
    }
    async getGroups() {
        const res = await this.$api.GroupManage.getGroups()
        const { result, message, data } = res
        if (!result) {
            return this.$error(message)
        }
        this.groupList = this.convertArray(data)
    }
    convertArray(arr) {
        const result = []
        arr.forEach(item => {
            const newItem = {
                value: item.id,
                label: item.name
            }
            if (item.subGroups && !!item.subGroups.length) {
                newItem.children = this.convertArray(item.subGroups)
            }
            result.push(newItem)
        })
        return result
    }
    async getUserList() {
        const { result, message, data } = await this.$api.UserManageMain.getAllUsers()
        if (!result) {
            return this.$error(message)
        }
        this.userList = data.map(item => {
            return {
                name: item.lastName,
                id: item.username
            }
        })
    }
    getShowValue(field, tex) {
        return getAssetAttrValue(field, tex, {
            groupList: this.groupList,
            userList: this.userList
        })
    }
    handleSelect(selections) {
        this.selectedInstances = selections
    }
    // 批量删除
    deleteInstance(list) {
        list.forEach(item => {
            const index = this.formData.instanceList.findIndex(inst => inst._id === item._id)
            if (index !== -1) {
                this.formData.instanceList.splice(index, 1)
                const comTable: any = this.$refs.comTable
                comTable.clearSelection()
            }
        })
    }
    show(data) {
        Object.assign(this.$data, this.$options.data.call(this))
        this.isShow = true
        if (this.role.superior_role !== 'admin') {
            this.resourceTypeList = [
                { name: '指定资产', id: 'fixed' }
            ]
        }
        this.instDetail = this.$copy(data)
        this.initPage(this.instDetail.row)
    }
    confirm() {
        const validateForm: any = this.$refs.validateForm
        validateForm.validate(valid => {
            if (valid) {
                this.addResource()
            }
        })
    }
    async addResource() {
        const params = {
            role_id: this.role.name
        }
        const url = this.isAdd ? 'createInstPermission' : 'updateInstPermission'
        const msg = this.isAdd ? '创建成功！' : '修改成功！'
        for (const key in this.formData) {
            if (['model_id', 'permission_type', 'resource_type'].includes(key)) {
                params[key] = this.formData[key]
            }
        }
        if (this.isAssetRange) {
            params.conditions = [[
                {
                    field: 'id',
                    type: 'id[]',
                    value: this.formData.instanceList.map(item => item._id)
                }
            ]]
        } else {
            const conditions = this.$Copy(this.formData.conditions)
            conditions.forEach(item => {
                item.child.forEach(
                    child => {
                        if (child.type === 'time') {
                            child.start = child.value.at()
                            child.end = child.value.at(-1)
                            delete child.value
                            return
                        }
                        if (child.type.includes('int')) {
                            child.value = +child.value
                            return
                        }
                        if (child.type === 'bool') {
                            child.value = Boolean(+child.value)
                        }
                    }
                )
            })
            params.conditions = conditions.map(item => item.child)
        }
        if (!this.isAdd) {
            params.id = this.instDetail.row?.id
        }
        const { result, message } = await this.$api.InstancePermission[url](params)
        if (!result) {
            return this.$error(message)
        }
        this.$success(msg)
        this.beforeCloseDialog()
        this.$emit('updateList')
    }
    beforeCloseDialog() {
        this.isShow = false
    }
}
</script>
<style lang="scss" scoped>
.form-item {
    width: 400px;
}
.rule-box {
    display: flex;
    flex-direction: column;
    margin-top: 20px;
    width: 100%;
    overflow: hidden;
    i {
        cursor: pointer;
    }
    .or-tag,
    .add-icon-box {
        visibility: visible !important;
        position: absolute;
        left: 0;
        bottom: 10px;
    }
    .tag {
        visibility: hidden;
        border-radius: 50%;
        width: 25px;
        height: 25px;
        background-color: #409EFF;
        color: #fff;
        text-align: center;
        line-height: 25px;
        font-size: 12px;
    }
    .first-level {
        padding-left: 40px;
        padding-bottom: 40px;
        position: relative;
        .delete-icon-first {
            position: absolute;
            right: 8px;
            top: 8px;
            font-size: 16px !important;
            cursor: pointer;
        }
        .add-icon-box {
            width: 25px;
            height: 25px;
            display: flex;
            justify-content: center;
            align-items: center;
            border: 1px solid #eee;
            .bk-icon {
                font-size: 16px !important;
            }
        }
        .second-level {
            display: flex;
            padding: 0 10px 10px 10px;
            align-items: center;
            background: #f4f5f8;
            border-radius: 2px;
            &:nth-child(1) {
                padding-top: 10px;
            }
            .bk-icon {
                font-size: 16px !important;
                cursor: pointer;
            }
            .and-tag {
                position: relative;
                margin-top: -50px;
                visibility: visible;
                transform: scale(0.8);
            }
        }
        &::after {
            position: absolute;
            left: 12px;
            top: -10px;
            content: "";
            width: 1px;
            height: calc(100% - 25px);
            background-color: #eee;
            transform: scaleX(0.5);
        }
    }
}
</style>
