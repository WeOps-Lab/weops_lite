Feature: 用户管理

  Scenario Outline: 创建用户
    Given 假设用户信息如下，用户信息：<用户信息>
    When 根据用户信息创建用户，并记录用户ID
    Then 根据用户ID，查询用户信息并进行信息校验
    And 点击删除用户
    Examples:
      |用户信息|
      |{"username":"test1", "password":"pwd1", "email":"test1@163.com", "lastName":"测试1"}|

  Scenario Outline: 修改用户信息(只支持修改email、lastName)
    Given 初始化一个用户，用户信息：<用户信息>
    When 修改用户为：<要修改的用户信息>
    Then 根据用户ID，查询用户信息并进行信息校验
    And 点击删除用户
    Examples:
      |用户信息|要修改的用户信息|
      |{"username":"test4", "password":"pwd4", "email":"test4@163.com", "lastName":"测试4"}|{"email":"test44@163.com"}|
      |{"username":"test5", "password":"pwd5", "email":"test5@163.com", "lastName":"测试5"}|{"lastName":"测试55"}|
      |{"username":"test6", "password":"pwd6", "email":"test6@163.com", "lastName":"测试6"}|{"email":"test66@163.com", "lastName":"测试66"}|

  Scenario Outline: 重置用户密码
    Given 初始化一个用户，用户信息：<用户信息>
    When 重置用户密码为<新密码>
    Then 用户登录
    And 点击删除用户
    Examples:
      |用户信息|新密码|
      |{"username":"test7", "password":"pwd7", "email":"test7@163.com", "lastName":"测试7"}|pwd77|

  Scenario Outline: 删除用户
    Given 初始化一个用户，用户信息：<用户信息>
    When 点击删除用户
    Then 不存在用户
    Examples:
      |用户信息|
      |{"username":"test10", "password":"pwd10", "email":"test10@163.com", "lastName":"测试10"}|
