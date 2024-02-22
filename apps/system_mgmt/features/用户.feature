Feature: 用户

  Scenario: 获取用户信息
    When 用户点击获取自己的用户信息
    Then 用户的名称是超管

  Scenario Outline: 创建用户
    Given 假设用户信息如下，用户信息：<用户信息>
    When 根据用户信息创建用户，并记录用户ID
    Then 根据用户ID，查询用户信息并进行信息校验
    And 点击删除用户
    Examples:
      |用户信息|
      |{"username":"test1", "password":"pwd1", "email":"test1@163.com", "lastName":"测试1"}|
      |{"username":"test2", "password":"pwd2", "email":"test2@163.com", "lastName":"测试2"}|
      |{"username":"test3", "password":"pwd3", "email":"test3@163.com", "lastName":"测试3"}|

  Scenario Outline: 修改用户信息(只支持修改email、lastName)
    Given 假设用户信息如下，用户信息：<用户信息>
    When 根据用户信息创建用户，并记录用户ID
    And 修改用户为：<要修改的用户信息>
    Then 根据用户ID，查询用户信息并进行信息校验
    And 点击删除用户
    Examples:
      |用户信息|要修改的用户信息|
      |{"username":"test4", "password":"pwd4", "email":"test4@163.com", "lastName":"测试4"}|{"email":"test44@163.com"}|
      |{"username":"test5", "password":"pwd5", "email":"test5@163.com", "lastName":"测试5"}|{"lastName":"测试55"}|
      |{"username":"test6", "password":"pwd6", "email":"test6@163.com", "lastName":"测试6"}|{"email":"test66@163.com", "lastName":"测试66"}|

  Scenario Outline: 重置用户密码
    Given 假设用户信息如下，用户信息：<用户信息>
    When 根据用户信息创建用户，并记录用户ID
    And 重置用户密码为<新密码>
    Then 用户登录
    And 点击删除用户
    Examples:
      |用户信息|新密码|
      |{"username":"test7", "password":"pwd7", "email":"test7@163.com", "lastName":"测试7"}|pwd77|
      |{"username":"test8", "password":"pwd8", "email":"test8@163.com", "lastName":"测试8"}|pwd88|
      |{"username":"test9", "password":"pwd9", "email":"test9@163.com", "lastName":"测试9"}|pwd99|


  Scenario Outline: 删除用户
    Given 假设用户信息如下，用户信息：<用户信息>
    When 根据用户信息创建用户，并记录用户ID
    And 点击删除用户
    Then 不存在用户
    Examples:
      |用户信息|
      |{"username":"test10", "password":"pwd10", "email":"test10@163.com", "lastName":"测试10"}|
      |{"username":"test11", "password":"pwd11", "email":"test11@163.com", "lastName":"测试11"}|
      |{"username":"test12", "password":"pwd12", "email":"test12@163.com", "lastName":"测试12"}|

  Scenario Outline: 创建角色
    Given 假设角色信息如下，角色信息：<角色信息>
    When 根据角色信息创建角色，并记录角色ID
    Then 根据角色ID，查询角色信息并进行信息校验
    And 点击删除角色
    Examples:
      |角色信息|
      |{"name": "普通角色1", "description": "这是一名普通角色"}|
      |{"name": "普通角色2", "description": "这是一名普通角色"}|
      |{"name": "普通角色3", "description": "这是一名普通角色"}|

  Scenario Outline: 删除角色
    Given 假设角色信息如下，角色信息：<角色信息>
    When 根据角色信息创建角色，并记录角色ID
    And 点击删除角色
    Then 不存在角色
    Examples:
      |角色信息|
      |{"name": "普通角色4", "description": "这是一名普通角色"}|
      |{"name": "普通角色5", "description": "这是一名普通角色"}|
      |{"name": "普通角色6", "description": "这是一名普通角色"}|

  Scenario Outline: 角色授权
    Given 假设角色信息如下，角色信息：<角色信息>
    When 根据角色信息创建角色，并记录角色ID
    And 对角色进行授权，角色权限：<授予的权限>
    Then 角色权限校验，角色权限：<授予的权限>
    And 点击删除角色
    Examples:
      |角色信息|授予的权限|
      |{"name": "普通角色7", "description": "这是一名普通角色"}|["SysLog_view","operation_log_list"]|
      |{"name": "普通角色8", "description": "这是一名普通角色"}|["SysLog_view","operation_log_list"]|
      |{"name": "普通角色9", "description": "这是一名普通角色"}|["SysLog_view","operation_log_list"]|

  Scenario Outline: 为用户添加角色
    Given 假设用户信息如下，用户信息：<用户信息>
    And 假设角色信息如下，角色信息：<角色信息>
    When 根据用户信息创建用户，并记录用户ID
    And 根据角色信息创建角色，并记录角色ID
    And 设置用户角色
    Then 存在用户角色
    And 点击删除用户
    And 点击删除角色
    Examples:
      |用户信息|角色信息|
      |{"username":"test13", "password":"pwd13", "email":"test13@163.com", "lastName":"测试13"}|{"name": "普通角色10", "description": "这是一名普通角色"}|
      |{"username":"test14", "password":"pwd14", "email":"test14@163.com", "lastName":"测试14"}|{"name": "普通角色11", "description": "这是一名普通角色"}|
      |{"username":"test15", "password":"pwd15", "email":"test15@163.com", "lastName":"测试15"}|{"name": "普通角色12", "description": "这是一名普通角色"}|

  Scenario Outline: 移除用户角色
    Given 假设用户信息如下，用户信息：<用户信息>
    And 假设角色信息如下，角色信息：<角色信息>
    When 根据用户信息创建用户，并记录用户ID
    And 根据角色信息创建角色，并记录角色ID
    And 设置用户角色
    And 移除用户角色
    Then 不存在用户角色
    And 点击删除用户
    And 点击删除角色
    Examples:
      |用户信息|角色信息|
      |{"username":"test16", "password":"pwd16", "email":"test16@163.com", "lastName":"测试16"}|{"name": "普通角色13", "description": "这是一名普通角色"}|
      |{"username":"test17", "password":"pwd17", "email":"test17@163.com", "lastName":"测试17"}|{"name": "普通角色14", "description": "这是一名普通角色"}|
      |{"username":"test18", "password":"pwd18", "email":"test18@163.com", "lastName":"测试18"}|{"name": "普通角色15", "description": "这是一名普通角色"}|

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
      |{"group_name": "组织2"}|{"group_name": "子组织2"}|
      |{"group_name": "组织3"}|{"group_name": "子组织3"}|

  Scenario Outline: 删除组织
    Given 假设组织信息如下，组织信息：<组织信息>
    When 根据组织信息创建组织，并记录组织ID
    And 点击删除组织
    Then 不存在组织
    Examples:
      |组织信息|
      |{"group_name": "组织4"}|
      |{"group_name": "组织5"}|
      |{"group_name": "组织6"}|

  Scenario Outline: 给组织添加组织角色
    Given 假设组织信息如下，组织信息：<组织信息>
    And 假设角色信息如下，角色信息：<角色信息>
    When 根据组织信息创建组织，并记录组织ID
    And 根据角色信息创建角色，并记录角色ID
    And 组织添加角色
    Then 存在组织角色
    And 点击删除组织
    And 点击删除角色
    Examples:
      |组织信息|角色信息|
      |{"group_name": "组织7"}|{"name": "普通角色16", "description": "这是一名普通角色"}|
      |{"group_name": "组织8"}|{"name": "普通角色17", "description": "这是一名普通角色"}|
      |{"group_name": "组织9"}|{"name": "普通角色18", "description": "这是一名普通角色"}|

  Scenario Outline: 给组织添加用户
    Given 假设组织信息如下，组织信息：<组织信息>
    And 假设用户信息如下，用户信息：<用户信息>
    When 根据组织信息创建组织，并记录组织ID
    And 根据用户信息创建用户，并记录用户ID
    And 组织添加用户
    Then 存在组织用户
    And 点击删除用户
    And 点击删除组织
    Examples:
      |组织信息|用户信息|
      |{"group_name": "组织10"}|{"username":"test19", "password":"pwd19", "email":"test19@163.com", "lastName":"测试19"}|
      |{"group_name": "组织11"}|{"username":"test20", "password":"pwd20", "email":"test20@163.com", "lastName":"测试20"}|
      |{"group_name": "组织12"}|{"username":"test21", "password":"pwd21", "email":"test21@163.com", "lastName":"测试21"}|

  Scenario Outline: 移除组织角色
    Given 假设组织信息如下，组织信息：<组织信息>
    And 假设角色信息如下，角色信息：<角色信息>
    When 根据组织信息创建组织，并记录组织ID
    And 根据角色信息创建角色，并记录角色ID
    And 组织添加角色
    And 组织移除角色
    Then 不存在组织角色
    And 点击删除组织
    And 点击删除角色
    Examples:
      |组织信息|角色信息|
      |{"group_name": "组织13"}|{"name": "普通角色19", "description": "这是一名普通角色"}|
      |{"group_name": "组织14"}|{"name": "普通角色20", "description": "这是一名普通角色"}|
      |{"group_name": "组织15"}|{"name": "普通角色21", "description": "这是一名普通角色"}|

  Scenario Outline: 移除组织用户
    Given 假设组织信息如下，组织信息：<组织信息>
    And 假设用户信息如下，用户信息：<用户信息>
    When 根据组织信息创建组织，并记录组织ID
    And 根据用户信息创建用户，并记录用户ID
    And 组织添加用户
    And 组织移除用户
    Then 不存在组织用户
    And 点击删除用户
    And 点击删除组织
    Examples:
      |组织信息|用户信息|
      |{"group_name": "组织16"}|{"username":"test22", "password":"pwd22", "email":"test22@163.com", "lastName":"测试22"}|
      |{"group_name": "组织17"}|{"username":"test23", "password":"pwd23", "email":"test23@163.com", "lastName":"测试23"}|
      |{"group_name": "组织18"}|{"username":"test24", "password":"pwd24", "email":"test24@163.com", "lastName":"测试24"}|