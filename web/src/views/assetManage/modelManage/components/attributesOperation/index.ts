import { OPERATE_TYPE_LIST } from '@/common/constants/assetManage/modelManage'
import { Vue, Component, Prop, Watch } from 'vue-property-decorator'
import DrawerComponent from '@/components/comDrawer/index.vue'
@Component({
    name: 'attributes-operation',
    components: {
        DrawerComponent
    }
})
export default class AttributesOperation extends Vue {
    @Prop({
        type: String,
        default: () => ''
    })
    modelId: string
    isShow: boolean = false
    currentType: string = ''
    formData: any = {
        propertyID: '',
        name: '',
        valueType: '',
        group: '',
        is_only: false,
        is_required: false,
        editable: true,
        fieldEdit: {
            isEdit: false,
            defaultValue: false,
            regularCheck: '',
            minValue: '',
            maxValue: '',
            enumDefaultValue: ''
        }
    }
    formDataV2: any = {}
    rules = {
        propertyID: [
            {
                required: true,
                message: '请输入属性ID',
                trigger: 'blur'
            },
            {
                validator: (rule, value, callback) => this.validatePropertyID(rule, value, callback),
                trigger: 'blur'
            }
            // {
            //     validator: function(val) {
            //         return !val.startsWith('bk_')
            //     },
            //     message: '不能以“bk_”开头',
            //     trigger: 'blur'
            // }
        ],
        name: [
            {
                required: true,
                message: '请输入属性名',
                trigger: 'blur'
            }
        ],
        valueType: [
            {
                required: true,
                message: '请选择值类型',
                trigger: 'blur'
            }
        ],
        group: [
            {
                required: true,
                message: '请选择所属分组',
                trigger: 'blur'
            }
        ],
        is_only: [
            {
                required: true,
                message: '请选择是否唯一',
                trigger: 'blur'
            }
        ],
        editable: [
            {
                required: true,
                message: '请选择是否可编辑',
                trigger: 'blur'
            }
        ],
        is_required: [
            {
                required: true,
                message: '请选择是否必填',
                trigger: 'blur'
            }
        ]
    }
    valueTypeList = OPERATE_TYPE_LIST
    groupList: Array<any> = []
    loading: boolean = false
    operationMap = {
        'singlechar': 'regularCheck',
        'str': 'regularCheck',
        'bool': 'defaultValue'
    }
    oldData: any = ''
    dragStartId: string | number = ''
    dragEndId: string | number = ''
    dragStartIndex: string | number = ''
    dragEndIndex: string | number = ''
    alreadyAddList: Array<any> = []
    enumDefaultList: Array<any> = []
    attrData: any = {}
    unitOptions: any[] = []
    @Watch('alreadyAddList', {
        immediate: true,
        deep: true
    })
    onAlreadyAddListChanged(val) {
        this.enumDefaultList = val.filter(item => item.valueId && item.name).map(item => {
            return {
                id: item.name,
                name: item.name
            }
        })
        this.enumDefaultList = this.$ArrayObjDup(this.enumDefaultList, 'id')
        if (this.enumDefaultList.length === 1) {
            this.formData.fieldEdit.enumDefaultValue = this.enumDefaultList[0].id
        }
    }
    get username() {
        return this.$store.state.permission.user.username
    }
    get isAdd() {
        return this.currentType === '添加'
    }
    validatePropertyID(rule, value, callback) {
        if (!/^[a-zA-Z]([a-zA-Z0-9_]+)?$/.test(value)) {
            callback(new Error('请填写英文开头，下划线、数字、英文的组合'))
        } else {
            callback()
        }
    }
    verificationNumber(type) {
        const minValue = Number(this.formData.fieldEdit.minValue)
        const maxValue = Number(this.formData.fieldEdit.maxValue)
        if (this.formData.fieldEdit.minValue !== '' && this.formData.fieldEdit.maxValue !== '') {
            if (minValue >= maxValue) {
                if (type === 'min') {
                    this.$nextTick(() => {
                        this.formData.fieldEdit.minValue = maxValue - 1
                    })
                } else {
                    this.$nextTick(() => {
                        this.formData.fieldEdit.maxValue = minValue + 1
                    })
                }
            }
        }
    }
    handleErrorMsg(item, index, valueLabel, errorMsg) {
        if (!item[valueLabel]) {
            item[errorMsg] = '该字段是必填项'
        }
        this.alreadyAddList.forEach((tex, i) => {
            if (tex[errorMsg] !== '该字段是必填项' || (index === i && item[valueLabel])) {
                tex[errorMsg] = ''
            }
            this.alreadyAddList.forEach((nev, k) => {
                if (i !== k && nev[valueLabel] && tex[valueLabel] === nev[valueLabel]) {
                    nev[errorMsg] = '重复的值'
                    tex[errorMsg] = '重复的值'
                }
            })
        })
    }
    changeValueId(item, index) {
        this.handleErrorMsg(item, index, 'valueId', 'valueIdErrorMsg')
    }
    changeName(item, index) {
        this.handleErrorMsg(item, index, 'name', 'nameErrorMsg')
    }
    deleteListTypeData(index) {
        this.alreadyAddList.splice(index, 1)
    }
    changeValueType() {
        this.alreadyAddList = []
        if (['list', 'enum'].includes(this.formData.valueType)) {
            this.alreadyAddList = [
                {
                    id: this.$random(5),
                    name: '',
                    valueId: '',
                    valueIdErrorMsg: '',
                    nameErrorMsg: ''
                }
            ]
        }
    }
    addListTypeData() {
        this.alreadyAddList.push({
            id: this.$random(5),
            name: '',
            valueId: '',
            valueIdErrorMsg: '',
            nameErrorMsg: ''
        }
        )
    }
    dragstart(value, index) {
        this.oldData = value
        this.dragStartId = value.id
        this.dragStartIndex = index
    }
    dragenter(value, index) {
        this.dragEndId = value.id
        this.dragEndIndex = index
    }
    dragover(e) {
        e.preventDefault()
    }
    getDragend() {
        if (this.dragStartId !== this.dragEndId) {
            const oldIndex = this.alreadyAddList.findIndex(item => item.id === this.dragStartId)
            const newIndex = this.alreadyAddList.findIndex(item => item.id === this.dragEndId)
            // 删除之前DOM节点
            this.alreadyAddList.splice(oldIndex, 1)
            // 在拖拽结束目标位置增加新的DOM节点
            this.alreadyAddList.splice(newIndex, 0, this.oldData)
        }
        this.dragEndId = ''
    }
    show(data) {
        this.hiddenSlider()
        this.isShow = true
        // this.unitOptions = getCategories().map(option => ({
        //     id: option.name,
        //     ...option
        // }))
        this.currentType = data.type
        this.groupList = data.groupList
        this.formData.valueType = this.valueTypeList[0].id
        if (data.type === '编辑') {
            this.handleEditTypeFirst(data)
        }
        this.formDataV2 = this.$deepClone(this.formData)
    }
    changeUnit(value) {
        const id = value?.[1]
        if (id) {
            this.formData.unit = id
            // this.formData.unitName = getUnitNameById(this.unitOptions, id)
        }
    }
    handleEditTypeFirst(data) {
        this.attrData = data.rowData
        const { unit_info: unitInfo } = this.attrData
        this.formData = {
            propertyID: this.attrData.attr_id,
            name: this.attrData.attr_name || '',
            valueType: this.attrData.attr_type || '',
            group: this.attrData.attr_group || '',
            is_only: this.attrData.is_only || false,
            is_required: this.attrData.is_required || false,
            editable: this.attrData.editable || false,
            fieldEdit: {
                isEdit: this.attrData.editable || false,
                defaultValue: false,
                regularCheck: '',
                minValue: '',
                maxValue: '',
                enumDefaultValue: ''
            },
            unit: unitInfo?.unit || '',
            unitName: unitInfo?.unit_name || ''
            // unitGroup: getUnitIdPath(this.unitOptions, unitInfo.unit) || []
        }
        this.handleEditTypeSecond()
    }
    handleEditTypeSecond() {
        if (['bool'].includes(this.formData.valueType)) {
            this.formData.fieldEdit.defaultValue = this.attrData.option || false
        }
        if (['singlechar', 'str'].includes(this.formData.valueType)) {
            this.formData.fieldEdit.regularCheck = this.attrData.option || ''
        }
        if (['int', 'float'].includes(this.formData.valueType)) {
            this.formData.fieldEdit.minValue = this.attrData.option?.min || 0
            this.formData.fieldEdit.maxValue = this.attrData.option?.max || 0
        }
        if (['list', 'enum'].includes(this.formData.valueType)) {
            this.alreadyAddList = this.attrData.option.map(item => {
                if (item.is_default) {
                    this.formData.fieldEdit.enumDefaultValue = item.name
                }
                return {
                    id: this.$random(5),
                    name: item.name,
                    valueId: item.id,
                    valueIdErrorMsg: '',
                    nameErrorMsg: ''
                }
            })
        }
    }
    validate() {
        const validateForm: any = this.$refs.validateForm
        validateForm.validate(validator => {
            if (validator) {
                const params = this.handleParams()
                const enumFlag = this.alreadyAddList.every(item => !item.nameErrorMsg)
                enumFlag && this.save(params)
            }
        })
    }
    handleParams() {
        const params: any = {
            id: this.modelId,
            attr_id: this.formData.propertyID,
            attr_name: this.formData.name,
            attr_type: this.formData.valueType,
            is_required: this.formData.is_required,
            attr_group: '',
            is_only: this.formData.is_only,
            editable: this.formData.editable
        }
        this.handleNormalType(params)
        this.handleEnumType(params)
        return params
    }
    handleNormalType(params) {
        if (['singlechar', 'str', 'bool'].includes(this.formData.valueType)) {
            params.option = this.formData.fieldEdit[this.operationMap[this.formData.valueType]]
        }
        if (['int', 'float'].includes(this.formData.valueType)) {
            params.option = {
                min: Number(this.formData.fieldEdit.minValue),
                max: Number(this.formData.fieldEdit.maxValue)
            }
        }
        if (this.formData.valueType === 'list') {
            params.option = this.alreadyAddList.map(item => {
                return item.name
            })
        }
    }
    handleEnumType(params) {
        if (this.formData.valueType === 'enum') {
            const target = this.alreadyAddList.find(item => !item.valueId || !item.name || item.nameErrorMsg || item.valueIdErrorMsg)
            if (target) {
                this.alreadyAddList.forEach(item => {
                    !item.name ? item.nameErrorMsg = '该字段是必填项' : item.nameErrorMsg = ''
                    !item.valueId ? item.valueIdErrorMsg = '该字段是必填项' : item.valueIdErrorMsg = ''
                })
                return false
            }
            params.option = this.alreadyAddList.map(item => {
                const obj = {
                    id: item.valueId,
                    is_default: false,
                    name: item.name,
                    type: 'text'
                }
                if (item.name === this.formData.fieldEdit.enumDefaultValue) {
                    obj.is_default = true
                }
                return obj
            })
        }
    }
    save(params) {
        this.loading = true
        this.$api.ModelManage[this.isAdd ? 'createModelAttr' : 'updateModelAttr'](params).then(res => {
            if (!res.result) {
                this.$error(res.message)
                return false
            }
            this.$success(`${this.isAdd ? '新增' : '修改'}属性成功`)
            this.isShow = false
            this.$emit('getTableData')
        }).finally(() => {
            this.loading = false
        })
    }
    cancel() {
        const flag = this.$compareFormData(this.formData, this.formDataV2)
        if (!flag) {
            this.$confirm('放弃将导致未保存信息丢失', '是否放弃本次操作？', {
                center: true
            }).then(() => {
                this.isShow = false
            })
        } else {
            this.isShow = false
        }
    }
    hiddenSlider() {
        Object.assign(this.$data, this.$options.data.call(this))
    }
}
