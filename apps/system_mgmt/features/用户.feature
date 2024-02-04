Feature: 用户

  Scenario: 获取用户信息
    When 用户点击获取自己的用户信息
    Then 用户的名称是超管

  Scenario: 创建用户
    Given 假设用户信息如下，用户名：test，密码：test123，邮箱：test@qq.com，中文名：测试员
    When 根据用户信息创建用户，并记录用户ID
    Then 根据用户ID，查询用户信息并进行信息校验

  Scenario: 修改用户信息
    Given 查找用户名为test的用户信息，并记录
    When 修改用户中文名称为：测试人员，邮箱为：test@163.com
    Then 根据用户ID，查询用户信息并进行信息校验

  Scenario: 重置用户密码
    Given 查找用户名为test的用户信息，并记录
    When 重置用户密码为test321
    Then 用户登录，用户名：test，密码：test321

  Scenario: 删除用户
    Given 查找用户名为test的用户信息，并记录
    When 点击删除用户
    Then 不存在用户：test