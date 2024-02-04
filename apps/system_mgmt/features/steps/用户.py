from behave import given, when, then
from apps.core.utils.keycloak_client import KeyCloakClient

from apps.core.features.utils.mock_request_client import MockRequestClient


@when('用户点击获取自己的用户信息')
def 用户点击获取自己的用户信息(context):
    resp = MockRequestClient().get('api/login_info/')
    context.user_info = resp["data"]["user_info"]


@then('用户的名称是{username}')
def 用户的名称是_username(context, username):
    assert context.user_info['name'] == username


@given("假设用户信息如下，用户名：{username}，密码：{password}，邮箱：{email}，中文名：{lastName}")
def 设置用户信息(context, username, password, email, lastName):
    context.username = username
    context.password = password
    context.email = email
    context.lastName = lastName


@when('根据用户信息创建用户，并记录用户ID')
def 创建用户(context):
    data = dict(
        username=context.username,
        password=context.password,
        email=context.email,
        lastName=context.lastName,
    )
    resp = MockRequestClient().post('api/user/', data)
    context.user_id = resp["data"]["id"]


@then('根据用户ID，查询用户信息并进行信息校验')
def 查询用户信息(context):
    resp = MockRequestClient().get(f'api/user/{context.user_id}/')

    assert context.username == resp["data"]["username"]
    assert context.email == resp["data"]["email"]
    assert context.lastName == resp["data"]["lastName"]


@given("查找用户名为{username}的用户信息，并记录")
def 查找并设置用户信息(context, username):
    resp = MockRequestClient().get(f"api/user/?search={username}")
    for user_info in resp["data"]["users"]:
        if user_info["username"] == username:
            context.user_info = user_info
            break


@when('修改用户中文名称为：{new_lastName}，邮箱为：{new_email}')
def 修改用户信息(context, new_lastName, new_email):
    data = dict(
        email=new_email,
        lastName=new_lastName,
    )
    MockRequestClient().put(f'api/user/{context.user_info["id"]}/', data)
    context.user_id = context.user_info["id"]
    context.username = context.user_info["username"]
    context.email = new_email
    context.lastName = new_lastName


@when('重置用户密码为{new_password}')
def 重置用户密码(context, new_password):
    context.new_password = new_password
    MockRequestClient().patch(f'api/user/{context.user_info["id"]}/', dict(password=new_password))


@then('用户登录，用户名：{username}，密码：{password}')
def 验证用户登录(context, username, password):
    resp = KeyCloakClient().get_token(username, password)
    assert resp.success


@when('点击删除用户')
def 删除用户(context):
    MockRequestClient().delete(f'api/user/{context.user_info["id"]}/')


@then('不存在用户：{username}')
def 验证用户登录(context, username):
    resp = MockRequestClient().get(f"api/user/?search={username}/")
    absent_username = True
    for user_info in resp["data"]["users"]:
        if user_info["username"] == username:
            absent_username = False
            break
    assert absent_username

