import json
from behave import given, when, then
from apps.core.features.utils.mock_request_client import MockRequestClient


@given("初始化一个角色，角色信息：{roleinfo}")
def 初始化一个角色(context, roleinfo):
    context.roleinfo = json.loads(roleinfo)
    resp = MockRequestClient().post('api/role/', context.roleinfo)
    context.role_id = resp["data"]["id"]


@given("假设角色信息如下，角色信息：{roleinfo}")
def 设置角色信息(context, roleinfo):
    context.roleinfo = json.loads(roleinfo)


@when('根据角色信息创建角色，并记录角色ID')
def 创建角色(context):
    resp = MockRequestClient().post('api/role/', context.roleinfo)
    context.role_id = resp["data"]["id"]


@then('根据角色ID，查询角色信息并进行信息校验')
def 查询角色信息(context):
    resp = MockRequestClient().get(f'api/role/')
    roleinfo = None
    for role_info in resp["data"]:
        if role_info["id"] == context.role_id:
            roleinfo = role_info
            break

    new_roleinfo = getattr(context, "new_roleinfo", {})
    name = new_roleinfo.get("name", context.roleinfo["name"])
    description = new_roleinfo.get("description", context.roleinfo["description"])

    assert name == roleinfo["name"]
    assert description == roleinfo["description"]


@when('点击删除角色')
def 删除角色(context):
    MockRequestClient().delete(f'api/role/{context.roleinfo["name"]}/')


@then('点击删除角色')
def 删除角色(context):
    MockRequestClient().delete(f'api/role/{context.roleinfo["name"]}/')


@then('不存在角色')
def 验证角色不存在(context):
    resp = MockRequestClient().get(f'api/role/')
    absent_role = True
    for role_info in resp["data"]:
        if role_info["id"] == context.role_id:
            absent_role = False
            break
    assert absent_role


@when('对角色进行授权，角色权限：{permissions}')
def 角色授权(context, permissions):
    permissions = json.loads(permissions)
    MockRequestClient().patch(f'api/role/{context.roleinfo["name"]}/permissions/', permissions)


@then('角色权限校验，角色权限：{permissions}')
def 角色权限校验(context, permissions):
    permissions = json.loads(permissions)
    resp = MockRequestClient().get(f'api/role/{context.roleinfo["name"]}/permissions/')
    absent_permissions = set(permissions) - set(resp["data"])
    no_loss = False if absent_permissions else True
    assert no_loss


@when('设置用户角色')
def 设置用户角色(context):
    MockRequestClient().put(f'api/role/{context.role_id}/assign/{context.user_id}/', {})


@when('移除用户角色')
def 移除用户角色(context):
    MockRequestClient().delete(f'api/role/{context.role_id}/withdraw/{context.user_id}/')


@then('存在用户角色')
def 存在用户角色(context):
    resp = MockRequestClient().get(f'api/user/roles/{context.roleinfo["name"]}/')
    exist = False
    for user_info in resp["data"]:
        if user_info["username"] == context.userinfo["username"]:
            exist = True
            break
    assert exist


@then('不存在用户角色')
def 不存在用户角色(context):
    resp = MockRequestClient().get(f'api/user/roles/{context.roleinfo["name"]}/')
    no_exist = True
    for user_info in resp["data"]:
        if user_info["username"] == context.userinfo["username"]:
            no_exist = False
            break
    assert no_exist
