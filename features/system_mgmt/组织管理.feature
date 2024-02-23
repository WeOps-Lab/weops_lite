Feature: 组织管理

  Scenario Outline: 创建组织
    Given 假设组织信息如下，组织信息：<组织信息>
    And 假设子组织信息如下，子组织信息：<子组织信息>
    When 根据组织信息创建组织，并记录组织ID
    And 根据子组织信息创建子组织，并记录子组织ID
    Then 根据组织ID，查询组织信息并进行信息校验
    And 根据子组织ID，查询子组织信息并进行信息校验
    And 点击删除子组织
    And 点击删除组织
    Examples:
      |组织信息|子组织信息|
      |{"group_name": "组织1"}|{"group_name": "子组织1"}|

  Scenario Outline: 删除组织
    Given 初始化一个组织，组织信息：<组织信息>
    When 点击删除组织
    Then 不存在组织
    Examples:
      |组织信息|
      |{"group_name": "组织4"}|

  Scenario Outline: 给组织添加组织角色
    Given 初始化一个组织，组织信息：<组织信息>
    And 初始化一个角色，角色信息：<角色信息>
    When 组织添加角色
    Then 存在组织角色
    And 点击删除组织
    And 点击删除角色
    Examples:
      |组织信息|角色信息|
      |{"group_name": "组织7"}|{"name": "普通角色16", "description": "这是一名普通角色"}|

  Scenario Outline: 给组织添加用户
    Given 初始化一个组织，组织信息：<组织信息>
    And 初始化一个用户，用户信息：<用户信息>
    When 组织添加用户
    Then 存在组织用户
    And 点击删除用户
    And 点击删除组织
    Examples:
      |组织信息|用户信息|
      |{"group_name": "组织10"}|{"username":"test19", "password":"pwd19", "email":"test19@163.com", "lastName":"测试19"}|

  Scenario Outline: 移除组织角色
    Given 初始化一个组织，组织信息：<组织信息>
    And 初始化一个角色，角色信息：<角色信息>
    When 组织添加角色
    And 组织移除角色
    Then 不存在组织角色
    And 点击删除组织
    And 点击删除角色
    Examples:
      |组织信息|角色信息|
      |{"group_name": "组织13"}|{"name": "普通角色19", "description": "这是一名普通角色"}|

  Scenario Outline: 移除组织用户
    Given 初始化一个组织，组织信息：<组织信息>
    And 初始化一个用户，用户信息：<用户信息>
    When 组织添加用户
    And 组织移除用户
    Then 不存在组织用户
    And 点击删除用户
    And 点击删除组织
    Examples:
      |组织信息|用户信息|
      |{"group_name": "组织16"}|{"username":"test22", "password":"pwd22", "email":"test22@163.com", "lastName":"测试22"}|
