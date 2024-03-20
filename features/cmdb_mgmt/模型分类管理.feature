Feature: 模型分类管理

  Scenario Outline: 创建模型分类
    Given 声明模型分类信息：<模型分类>
    When 创建模型分类
    Then 模型分类已存在
    And 删除模型分类
    Examples:
      | 模型分类 |
      | {"classification_id": "test", "classification_name": "测试"} |

  Scenario Outline: 删除模型分类
    Given 声明模型分类信息：<模型分类>
    When 创建模型分类
    And 删除模型分类
    Then 模型分类不存在
    Examples:
      | 模型分类 |
      | {"classification_id": "test", "classification_name": "测试"} |
