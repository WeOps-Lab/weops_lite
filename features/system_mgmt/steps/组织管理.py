import json
from behave import given, when, then
from apps.core.features.utils.mock_request_client import MockRequestClient


@given('初始化一个组织，组织信息：{groupinfo}')
def 初始化一个组织(context, groupinfo):
    context.groupinfo = json.loads(groupinfo)
    resp = MockRequestClient().post('api/group/', context.groupinfo)
    context.group_id = resp["data"]["id"]


@given('初始化一个子组织，子组织信息：{subgroupinfo}')
def 初始化一个子组织(context, subgroupinfo):
    context.subgroupinfo = json.loads(subgroupinfo)
    data = dict(parent_group_id=context.group_id, **context.subgroupinfo)
    resp = MockRequestClient().post('api/group/', data)
    context.subgroup_id = resp["data"]["id"]


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
    resp = MockRequestClient().get(f'api/group/?search={context.groupinfo["group_name"]}')
    groupinfo = None
    for group_info in resp["data"]:
        if group_info["id"] == context.group_id:
            groupinfo = group_info
            break
    assert groupinfo["name"] == context.groupinfo["group_name"]


@then('根据子组织ID，查询子组织信息并进行信息校验')
def 校验子组织信息(context):
    resp = MockRequestClient().get(f'api/group/{context.subgroup_id}/')
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

    resp = MockRequestClient().get(f'api/group/?search={context.groupinfo["group_name"]}')
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
