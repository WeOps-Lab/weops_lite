export const PROPERTY_COLUMNS = [
    {
        label: '属性名',
        key: 'attr_name',
        align: 'left',
        minWidth: '100px'
    },
    {
        label: '属性ID',
        key: 'attr_id',
        align: 'left',
        minWidth: '100px'
    },
    {
        label: '值类型',
        key: 'attr_type',
        align: 'left',
        scopedSlots: 'attrType',
        minWidth: '100px'
    },
    {
        label: '是否必填',
        key: 'is_required',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'require'
    },
    {
        label: '可编辑',
        key: 'editable',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'editable'
    },
    {
        label: '是否唯一',
        key: 'is_only',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'is_only'
    },
    {
        label: '操作',
        key: 'operation',
        align: 'left',
        width: '140px',
        scopedSlots: 'operation'
    }
]

// 值类型
export const OPERATE_TYPE_LIST = [
    // {
    //     id: 'singlechar',
    //     name: '短字符'
    // },
    {
        id: 'str',
        name: '字符串'
    },
    {
        id: 'int',
        name: '数字'
    },
    {
        id: 'enum',
        name: '枚举'
    },
    // {
    //     id: 'date',
    //     name: '日期'
    // },
    {
        id: 'time',
        name: '时间'
    },
    {
        id: 'user',
        name: '用户'
    },
    {
        id: 'pwd',
        name: '密码'
    },
    {
        id: 'bool',
        name: '布尔'
    }
    // {
    //     id: 'organization',
    //     name: '组织'
    // }
]

// 关联表头
export const RELATION_COLUMNS = [
    {
        label: '关联名称',
        key: 'model_asst_id',
        align: 'left',
        minWidth: '140px',
        scopedSlots: 'model_asst_id'
    },
    {
        label: '源模型',
        key: 'src_model_id',
        align: 'left',
        minWidth: '120px',
        scopedSlots: 'src_model_id'
    },
    {
        label: '目标模型',
        key: 'dst_model_id',
        align: 'left',
        minWidth: '120px',
        scopedSlots: 'dst_model_id'
    },
    {
        label: '关联关系',
        key: 'asst_id',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'asst_id'
    },
    {
        label: '约束条件',
        key: 'mapping',
        align: 'left',
        minWidth: '100px',
        scopedSlots: 'mapping'
    },
    {
        label: '操作',
        key: 'operation',
        align: 'left',
        width: '140px',
        scopedSlots: 'operation'
    }
]

// 约束条件
export const TARGET_BIND_LIST = [
    {
        id: 'n:n',
        name: 'N-N'
    },
    {
        id: '1:n',
        name: '1-N'
    },
    {
        id: '1:1',
        name: '1-1'
    }
]

// 模型详情tab
export const MODEL_DETAIL_PANELS = [
    { name: 'property', label: '字段属性' },
    { name: 'relation', label: '关联关系' }
]

const validateMark = (rule, value, callback) => {
    if (!/^[a-z][^A-Z]*$/.test(value)) {
        callback(new Error('请输入正确的格式，可使用小写字母、数字、下划线，需以字母开头'))
        return
    }
    callback()
}

// 模型分组rule
export const GROUP_OPETATE_RULE = {
    onlyMark: [
        {
            required: true,
            message: '请输入唯一标识',
            trigger: 'blur'
        },
        { validator: validateMark, trigger: 'blur' }
    ],
    name: [
        {
            required: true,
            message: '请输入唯一名称',
            trigger: 'blur'
        }
    ]
}
