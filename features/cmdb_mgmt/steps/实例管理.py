import json
from behave import given, when, then
from apps.core.features.utils.mock_request_client import MockRequestClient


@given("声明实例信息：{inst_info}")
def 声明实例信息(context, inst_info):
    context.inst_info = json.loads(inst_info)


@when("创建实例")
def 创建实例(context):
    resp = MockRequestClient().post('api/instance/', dict(model_id=context.model_id, instance_info=context.inst_info))
    context.inst_id = resp["data"]["_id"]


@then("实例已存在")
def 实例已存在(context):
    resp = MockRequestClient().get(f'api/instance/{context.inst_id}/')
    assert resp["data"]["_id"] == context.inst_id


@then("实例不存在")
def 实例不存在(context):
    try:
        MockRequestClient().get(f'api/instance/{context.inst_id}/')
        exist = True
    except:
        exist = False
    assert not exist


@then("删除实例")
def 删除实例(context):
    MockRequestClient().delete(f'api/instance/{context.inst_id}/')


@when("删除实例")
def 删除实例(context):
    MockRequestClient().delete(f'api/instance/{context.inst_id}/')


@given("初始化一个实例：{inst_info}")
def 初始化一个实例(context, inst_info):
    context.inst_info = json.loads(inst_info)
    resp = MockRequestClient().post('api/instance/', dict(model_id=context.model_id, instance_info=context.inst_info))
    context.inst_id = resp["data"]["_id"]


@when("修改实例属性：{update_inst_info}")
def 修改实例属性(context, update_inst_info):
    context.update_inst_info = json.loads(update_inst_info)
    resp = MockRequestClient().patch(f'api/instance/{context.inst_id}/', context.update_inst_info)
    context.new_inst_info = resp["data"]


@then("实例属性修改成功")
def 实例属性修改成功(context):
    for k, v in context.update_inst_info.items():
        assert v == context.update_inst_info[k]


@given("初始化模型与关联：{src_model_info} {dst_model_info} {asst_id}")
def 初始化模型与关联(context, src_model_info, dst_model_info, asst_id):
    context.src_model_info = json.loads(src_model_info)
    src_resp = MockRequestClient().post('api/model/', context.src_model_info)
    context.src_model_id = src_resp["data"]["model_id"]

    context.dst_model_info = json.loads(dst_model_info)
    dst_resp = MockRequestClient().post('api/model/', context.dst_model_info)
    context.dst_model_id = dst_resp["data"]["model_id"]

    asso_info = {
        "asst_id": asst_id,
        "src_model_id": context.src_model_id,
        "dst_model_id": context.dst_model_id,
        "model_asst_id": f"{context.src_model_id}_{asst_id}_{context.dst_model_id}",
        "mapping": "N:N"
    }
    context.asso_info = asso_info
    resp = MockRequestClient().post('api/model/association/', context.asso_info)
    context.model_asst_id = resp["data"]["model_asst_id"]


@given("初始化源模型实例与目标模型实例：{src_inst_info} {dst_inst_info}")
def 初始化源模型实例与目标模型实例(context, src_inst_info, dst_inst_info):
    context.src_inst_info = json.loads(src_inst_info)
    src_resp = MockRequestClient().post(
        'api/instance/', dict(model_id=context.src_model_id, instance_info=context.src_inst_info))
    context.src_inst_id = src_resp["data"]["_id"]

    context.dst_inst_info = json.loads(dst_inst_info)
    dst_resp = MockRequestClient().post(
        'api/instance/', dict(model_id=context.dst_model_id, instance_info=context.dst_inst_info))
    context.dst_inst_id = dst_resp["data"]["_id"]


@when("创建实例关联")
def 创建实例关联(context):
    inst_asso_info = {
        "model_asst_id": context.model_asst_id,
        "src_model_id": context.src_model_id,
        "dst_model_id": context.dst_model_id,
        "src_inst_id": context.src_inst_id,
        "dst_inst_id": context.dst_inst_id,
    }
    context.inst_asso_info = inst_asso_info
    resp = MockRequestClient().post('api/instance/association/', context.inst_asso_info)
    context.inst_asso_id = resp["data"]["_id"]


@then("实例关联已存在")
def 实例关联已存在(context):
    resp = MockRequestClient().post('api/instance/association_list/', context.inst_asso_info)
    assert context.inst_asso_id in {i["_id"] for i in resp["data"]}


@then("实例关联不存在")
def 实例关联不存在(context):
    resp = MockRequestClient().post('api/instance/association_list/', context.inst_asso_info)
    assert context.inst_asso_id not in {i["_id"] for i in resp["data"]}


@when("删除实例关联")
def 删除实例关联(context):
    MockRequestClient().delete(f'api/instance/association/{context.inst_asso_id}/')


@then("删除实例关联")
def 删除实例关联(context):
    MockRequestClient().delete(f'api/instance/association/{context.inst_asso_id}/')


@then("删除源模型实例与目标模型实例")
def 删除源模型实例与目标模型实例(context):
    MockRequestClient().delete(f'api/instance/{context.src_inst_id}/')
    MockRequestClient().delete(f'api/instance/{context.dst_inst_id}/')


@then("删除初始化的模型与关联")
def 删除初始化的模型与关联(context):
    MockRequestClient().delete(f'api/model/association/{context.model_asst_id}/')
    MockRequestClient().delete(f'api/model/{context.src_model_id}/')
    MockRequestClient().delete(f'api/model/{context.dst_model_id}/')
