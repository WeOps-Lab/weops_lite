Feature: 角色管理

  Scenario Outline: 创建角色
    Given 假设角色信息如下，角色信息：<角色信息>
    When 根据角色信息创建角色，并记录角色ID
    Then 根据角色ID，查询角色信息并进行信息校验
    And 点击删除角色
    Examples:
      |角色信息|
      |{"name": "普通角色1", "description": "这是一名普通角色"}|


  Scenario Outline: 删除角色
    Given 初始化一个角色，角色信息：<角色信息>
    When 点击删除角色
    Then 不存在角色
    Examples:
      |角色信息|
      |{"name": "普通角色4", "description": "这是一名普通角色"}|

  Scenario Outline: 角色授权
    Given 初始化一个角色，角色信息：<角色信息>
    When 对角色进行授权，角色权限：<授予的权限>
    Then 角色权限校验，角色权限：<授予的权限>
    And 点击删除角色
    Examples:
      |角色信息|授予的权限|
      |{"name": "普通角色7", "description": "这是一名普通角色"}|["SysLog_view","operation_log_list"]|


  Scenario Outline: 为用户添加角色
    Given 初始化一个用户，用户信息：<用户信息>
    And 初始化一个角色，角色信息：<角色信息>
    When 设置用户角色
    Then 存在用户角色
    And 点击删除用户
    And 点击删除角色
    Examples:
      |用户信息|角色信息|
      |{"username":"test13", "password":"pwd13", "email":"test13@163.com", "lastName":"测试13"}|{"name": "普通角色10", "description": "这是一名普通角色"}|


  Scenario Outline: 移除用户角色
    Given 初始化一个用户，用户信息：<用户信息>
    And 初始化一个角色，角色信息：<角色信息>
    When 设置用户角色
    And 移除用户角色
    Then 不存在用户角色
    And 点击删除用户
    And 点击删除角色
    Examples:
      |用户信息|角色信息|
      |{"username":"test16", "password":"pwd16", "email":"test16@163.com", "lastName":"测试16"}|{"name": "普通角色13", "description": "这是一名普通角色"}|
