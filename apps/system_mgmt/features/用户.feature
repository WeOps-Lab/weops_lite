Feature: 用户

  Scenario: 获取用户信息
    When 用户点击获取自己的用户信息
    Then 用户的名称是 管理员