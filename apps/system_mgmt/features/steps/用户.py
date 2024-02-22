import json

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
def 验证用户登录(context):
    username = context.userinfo["username"]
    resp = MockRequestClient().get(f"api/user/?search={username}/")
    absent_username = True
    for user_info in resp["data"]["users"]:
        if user_info["username"] == username:
            absent_username = False
            break
    assert absent_username


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


@given('假设组织信息如下，组织信息：{groupinfo}')
def 设置组织信息(context, groupinfo):
    context.groupinfo = json.loads(groupinfo)


@given('假设子组织信息如下，子组织信息：{subgroupinfo}')
def 设置子组织信息(context, subgroupinfo):
    context.subgroupinfo = json.loads(subgroupinfo)


@when('根据组织信息创建组织，并记录组织ID')
def 创建组织(context):
    resp = MockRequestClient().post('api/group/', context.groupinfo)
    context.group_id = resp["data"]["id"]


@when('根据子组织信息创建子组织，并记录子组织ID')
def 创建子组织(context):
    data = dict(parent_group_id=context.group_id, **context.subgroupinfo)
    resp = MockRequestClient().post('api/group/', data)
    context.subgroup_id = resp["data"]["id"]


@then('根据组织ID，查询组织信息并进行信息校验')
def 校验组织信息(context):
    resp = MockRequestClient().get(f'/api/group/?search={context.groupinfo["group_name"]}')
    groupinfo = None
    for group_info in resp["data"]:
        if group_info["id"] == context.group_id:
            groupinfo = group_info
            break
    assert groupinfo["name"] == context.groupinfo["group_name"]


@then('根据子组织ID，查询子组织信息并进行信息校验')
def 校验子组织信息(context):
    resp = MockRequestClient().get(f'/api/group/{context.subgroup_id}/')
    assert resp["data"]["name"] == context.subgroupinfo["group_name"]


@when('点击删除组织')
def 删除组织(context):
    MockRequestClient().delete(f'api/group/delete_groups/', [context.group_id])


@then('点击删除组织')
def 删除组织(context):
    MockRequestClient().delete(f'api/group/delete_groups/', [context.group_id])


@then('点击删除子组织')
def 删除子组织(context):
    MockRequestClient().delete(f'api/group/delete_groups/', [context.subgroup_id])


@then('不存在组织')
def 验证组织不存在(context):

    resp = MockRequestClient().get(f'/api/group/?search={context.groupinfo["group_name"]}')
    absent_group = True
    for group_info in resp["data"]:
        if group_info["id"] == context.group_id:
            absent_group = False
            break
    assert absent_group


@when('组织添加角色')
def 组织添加角色(context):
    MockRequestClient().patch(f'api/group/{context.group_id}/assign_roles/', [context.role_id])


@when('组织移除角色')
def 组织移除角色(context):
    MockRequestClient().delete(f'api/group/{context.group_id}/unassign_roles/', [context.role_id])


@then('存在组织角色')
def 存在组织角色(context):
    resp = MockRequestClient().get(f'api/group/{context.group_id}/roles/')
    exist = False
    for role_info in resp["data"]:
        if role_info["id"] == context.role_id:
            exist = True
            break
    assert exist


@then('不存在组织角色')
def 不存在组织角色(context):
    resp = MockRequestClient().get(f'api/group/{context.group_id}/roles/')
    no_exist = True
    for role_info in resp["data"]:
        if role_info["id"] == context.role_id:
            no_exist = False
            break
    assert no_exist


@when('组织添加用户')
def 组织添加用户(context):
    MockRequestClient().patch(f'api/group/{context.group_id}/assign_users/', [context.user_id])


@when('组织移除用户')
def 组织移除用户(context):
    MockRequestClient().delete(f'api/group/{context.group_id}/unassign_users/', [context.user_id])


@then('存在组织用户')
def 存在组织用户(context):
    resp = MockRequestClient().get(f'api/group/{context.group_id}/users/')
    exist = False
    for user_info in resp["data"]:
        if user_info["id"] == context.user_id:
            exist = True
            break
    assert exist


@then('不存在组织用户')
def 不存在组织用户(context):
    resp = MockRequestClient().get(f'api/group/{context.group_id}/users/')
    no_exist = True
    for user_info in resp["data"]:
        if user_info["id"] == context.user_id:
            no_exist = False
            break
    assert no_exist
