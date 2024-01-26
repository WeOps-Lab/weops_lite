Feature: 用户认证

  Scenario: 用户登录
    When 管理员用户输入账号和密码
    Then 成功获取用户的AccessToken