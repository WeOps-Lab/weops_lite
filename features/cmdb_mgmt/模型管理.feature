Feature: 模型管理

  Scenario Outline: 创建模型
    Given 声明模型信息：<模型信息>
    When 创建模型
    Then 模型已存在
    And 删除模型
    Examples:
      | 模型信息 |
      | {"classification_id": "default", "model_id": "sqlserver", "model_name": "SqlServer", "icn": "default"} |

  Scenario Outline: 删除模型
    Given 声明模型信息：<模型信息>
    When 创建模型
    And 删除模型
    Then 模型不存在
    Examples:
      | 模型信息 |
      | {"classification_id": "default", "model_id": "sqlserver", "model_name": "SqlServer", "icn": "default"} |


  Scenario Outline: 创建模型属性
    Given 初始化一个模型：<模型信息>
    When 创建模型属性：<属性信息>
    Then 模型属性已存在
    And 删除模型
    Examples:
      | 模型信息 | 属性信息 |
      | {"classification_id": "default", "model_id": "sqlserver", "model_name": "SqlServer", "icn": "default"} | {"attr_id": "ip_addr", "attr_name": "ip地址", "attr_type": "string", "isonly": true, "isrequired": true, "editable": true, "option": {}, "attr_group": "default"} |

  Scenario Outline: 删除模型属性
    Given 初始化一个模型：<模型信息>
    When 创建模型属性：<属性信息>
    And 删除模型属性
    Then 模型属性不存在
    And 删除模型
    Examples:
      | 模型信息 | 属性信息 |
      | {"classification_id": "default", "model_id": "sqlserver", "model_name": "SqlServer", "icn": "default"} | { "attr_id": "ip_addr", "attr_name": "ip地址", "attr_type": "string", "isonly": true, "isrequired": true, "editable": true, "option": {}, "attr_group": "default"} |


  Scenario Outline: 创建模型关联关系
    Given 初始源模型：<源模型信息>，初始目标模型：<目标模型信息>
    When 创建模型关联关系：<关联类型>
    Then 模型关联关系已存在
    And 删除模型关联关系
    And 删除源模型与目标模型
    Examples:
      | 源模型信息 | 目标模型信息 | 关联类型 |
      | {"classification_id": "default", "model_id": "sqlserver", "model_name": "SqlServer", "icn": "default"} | {"classification_id": "default", "model_id": "test_host", "model_name": "测试主机", "icn": "default"} | "install_on" |

  Scenario Outline: 删除模型关联关系
    Given 初始源模型：<源模型信息>，初始目标模型：<目标模型信息>
    When 创建模型关联关系：<关联类型>
    And 删除模型关联关系
    Then 模型关联关系不存在
    And 删除源模型与目标模型
    Examples:
      | 源模型信息 | 目标模型信息 | 关联类型 |
      | {"classification_id": "default", "model_id": "sqlserver", "model_name": "SqlServer", "icn": "default"} | {"classification_id": "default", "model_id": "test_host", "model_name": "测试主机", "icn": "default"} | "install_on" |

