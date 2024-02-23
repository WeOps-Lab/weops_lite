import json
from behave import given, when, then
from apps.core.utils.keycloak_client import KeyCloakClient
from apps.core.features.utils.mock_request_client import MockRequestClient


@given("初始化一个用户，用户信息：{userinfo}")
def 初始化一个用户(context, userinfo):
    context.userinfo = json.loads(userinfo)
    resp = MockRequestClient().post('api/user/', context.userinfo)
    context.user_id = resp["data"]["id"]


@given("假设用户信息如下，用户信息：{userinfo}")
def 设置用户信息(context, userinfo):
    context.userinfo = json.loads(userinfo)


@when('根据用户信息创建用户，并记录用户ID')
def 创建用户(context):
    resp = MockRequestClient().post('api/user/', context.userinfo)
    context.user_id = resp["data"]["id"]


@then('根据用户ID，查询用户信息并进行信息校验')
def 查询用户信息(context):
    resp = MockRequestClient().get(f'api/user/{context.user_id}/')
    new_userinfo = getattr(context, "new_userinfo", {})
    new_email = new_userinfo.get("email", context.userinfo["email"])
    new_lastName = new_userinfo.get("lastName", context.userinfo["lastName"])

    assert context.userinfo["username"] == resp["data"]["username"]
    assert new_email == resp["data"]["email"]
    assert new_lastName == resp["data"]["lastName"]


@then('点击删除用户')
def 删除用户(context):
    MockRequestClient().delete(f'api/user/{context.user_id}/')


@given("查找用户名为{username}的用户信息，并记录")
def 查找并设置用户信息(context, username):
    resp = MockRequestClient().get(f"api/user/?search={username}")
    for user_info in resp["data"]["users"]:
        if user_info["username"] == username:
            context.user_info = user_info
            break


@when('修改用户为：{new_userinfo}')
def 修改用户信息(context, new_userinfo):
    new_userinfo = json.loads(new_userinfo)
    data = {}
    if "email" in new_userinfo:
        data.update(email=new_userinfo["email"])
    if "lastName" in new_userinfo:
        data.update(lastName=new_userinfo["lastName"])

    MockRequestClient().put(f'api/user/{context.user_id}/', data)
    context.new_userinfo = new_userinfo


@when('重置用户密码为{new_password}')
def 重置用户密码(context, new_password):
    context.new_password = new_password
    MockRequestClient().patch(f'api/user/{context.user_id}/', dict(password=new_password))


@then('用户登录')
def 验证用户登录(context):
    username, password = context.userinfo["username"], context.new_password
    resp = KeyCloakClient().get_token(username, password)
    assert resp.success


@when('点击删除用户')
def 删除用户(context):
    MockRequestClient().delete(f'api/user/{context.user_id}/')


@then('不存在用户')
def 不存在用户(context):
    username = context.userinfo["username"]
    resp = MockRequestClient().get(f"api/user/?search={username}/")
    absent_username = True
    for user_info in resp["data"]["users"]:
        if user_info["username"] == username:
            absent_username = False
            break
    assert absent_username
