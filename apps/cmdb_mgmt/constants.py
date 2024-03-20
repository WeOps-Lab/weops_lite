# 模型标签
MODEL = "model"

# 模型分类标签
CLASSIFICATION = "classification"

# 实例标签
INSTANCE = "instance"

# 模型关联标签
MODEL_ASSOCIATION = "model_association"

# 实例关联标签
INSTANCE_ASSOCIATION = "instance_association"

# 模型间的关联类型
ASSOCIATION_TYPE = [
    {
        "bk_asst_id": "belong",
        "bk_asst_name": "属于",
        "ispre": True
    },
    {
        "bk_asst_id": "group",
        "bk_asst_name": "组成",
        "ispre": True
    },
    {
        "bk_asst_id": "run",
        "bk_asst_name": "运行于",
        "ispre": True
    },
    {
        "bk_asst_id": "install_on",
        "bk_asst_name": "安装于",
        "ispre": True
    },
    {
        "bk_asst_id": "contains",
        "bk_asst_name": "包含",
        "ispre": True
    }
]

# 默认的实例名属性
INST_NAME_INFO = {
    "attr_id": "inst_name",
    "attr_name": "实例名",
    "attr_type": "str",
    "isonly": True,
    "isrequired": True,
    "editable": False,
    "option": {},
    "attr_group": "default"
}
