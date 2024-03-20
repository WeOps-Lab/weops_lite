Feature: 实例管理

  Scenario Outline: 创建实例
    Given 初始化一个模型：<模型信息>
    And 声明实例信息：<实例信息>
    When 创建实例
    Then 实例已存在
    And 删除实例
    And 删除模型
    Examples:
      | 模型信息 | 实例信息 |
      | {"classification_id": "default", "model_id": "test", "model_name": "Test", "icn": "default"} | {"inst_name": "test001"} |

  Scenario Outline: 删除实例
    Given 初始化一个模型：<模型信息>
    And 声明实例信息：<实例信息>
    When 创建实例
    And 删除实例
    Then 实例不存在
    And 删除模型
    Examples:
      | 模型信息 | 实例信息 |
      | {"classification_id": "default", "model_id": "test", "model_name": "Test", "icn": "default"} | {"inst_name": "test001"} |

  Scenario Outline: 修改实例
    Given 初始化一个模型：<模型信息>
    And 初始化一个实例：<实例信息>
    When 修改实例属性：<实例属性>
    Then 实例属性修改成功
    And 删除实例
    And 删除模型
    Examples:
      | 模型信息 | 实例信息 | 实例属性 |
      | {"classification_id": "default", "model_id": "test", "model_name": "Test", "icn": "default"} | {"inst_name": "test001"} | {"inst_name": "new_test001"} |

  Scenario Outline: 创建实例关联
    Given 初始化模型与关联：<源模型> <目标模型> <模型关联>
    And 初始化源模型实例与目标模型实例：<源实例> <目标实例>
    When 创建实例关联
    Then 实例关联已存在
    And 删除实例关联
    And 删除源模型实例与目标模型实例
    And 删除初始化的模型与关联
    Examples:
      | 源模型 | 目标模型 | 模型关联 | 源实例 | 目标实例 |
      | {"classification_id":"default","model_id":"test1","model_name":"Test1","icn":"default"} | {"classification_id":"default","model_id":"test2","model_name":"Test2","icn":"default"} | "install_on" | {"inst_name":"test001"} | {"inst_name":"test002"} |

  Scenario Outline: 删除实例关联
    Given 初始化模型与关联：<源模型> <目标模型> <模型关联>
    And 初始化源模型实例与目标模型实例：<源实例> <目标实例>
    When 创建实例关联
    And 删除实例关联
    Then 实例关联不存在
    And 删除源模型实例与目标模型实例
    And 删除初始化的模型与关联
    Examples:
      | 源模型 | 目标模型 | 模型关联 | 源实例 | 目标实例 |
      | {"classification_id":"default","model_id":"test1","model_name":"Test1","icn":"default"} | {"classification_id":"default","model_id":"test2","model_name":"Test2","icn":"default"} | "install_on" | {"inst_name":"test001"} | {"inst_name":"test002"} |

