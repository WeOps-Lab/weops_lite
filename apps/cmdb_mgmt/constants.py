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
        "asst_id": "belong",
        "asst_name": "属于",
        "is_pre": True
    },
    {
        "asst_id": "group",
        "asst_name": "组成",
        "is_pre": True
    },
    {
        "asst_id": "run",
        "asst_name": "运行于",
        "is_pre": True
    },
    {
        "asst_id": "install_on",
        "asst_name": "安装于",
        "is_pre": True
    },
    {
        "asst_id": "contains",
        "asst_name": "包含",
        "is_pre": True
    },
    {
        "asst_id": "default",
        "asst_name": "关联",
        "is_pre": True
    }
]


# 需要进行ID与NAME转化的属性类型
ENUM = "enum"
USER = "user"
ORGANIZATION = "organization"

# 默认的实例名属性
INST_NAME_INFOS = [
    {
        "attr_id": "inst_name",
        "attr_name": "实例名",
        "attr_type": "str",
        "is_only": True,
        "is_required": True,
        "editable": True,
        "option": {},
        "attr_group": "default",
        "is_pre": True
    },
    {
        "attr_id": ORGANIZATION,
        "attr_name": "所属组织",
        "attr_type": ORGANIZATION,
        "is_only": False,
        "is_required": True,
        "editable": True,
        "option": [],
        "attr_group": "default",
        "is_pre": True
    }
]

# 创建模型分类时校验属性
CREATE_CLASSIFICATION_CHECK_ATTR_MAP = dict(
    is_only={"classification_id": "模型分类ID", "classification_name": "模型分类名称"},
    is_required={"classification_id": "模型分类ID", "classification_name": "模型分类名称"},
)
# 更新模型分类时校验属性
UPDATE_CLASSIFICATION_check_attr_map = dict(
    is_only={"classification_name": "模型分类名称"},
    is_required={"classification_name": "模型分类名称"},
    editable={"classification_name": "模型分类名称"},
)
# 创建模型时校验属性
CREATE_MODEL_CHECK_ATTR = dict(
    is_only={"model_id": "模型ID", "model_name": "模型名称"},
    is_required={"model_id": "模型ID", "model_name": "模型名称"},
)
# 更新模型时校验属性
UPDATE_MODEL_CHECK_ATTR_MAP = dict(
    is_only={"model_name": "模型名称"},
    is_required={"model_name": "模型名称"},
    editable={"model_name": "模型名称", "classification_id": "模型分类ID", "icn": "图标"},
)

# 需要进行类型转换的数据类型
NEED_CONVERSION_TYPE = {
    "bool": lambda x: True if x in {"true", "True", "TRUE", True} else False,
    "int": int,
    "float": float,
    "str": str,
    "list": list,
}

EDGE_TYPE = 2
ENTITY_TYPE = 1
