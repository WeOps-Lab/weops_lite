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
