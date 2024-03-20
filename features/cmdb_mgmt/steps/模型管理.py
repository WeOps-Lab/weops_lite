import json
from behave import given, when, then
from apps.core.features.utils.mock_request_client import MockRequestClient


@given("声明模型信息：{model_info}")
def 声明模型信息(context, model_info):
    context.model_info = json.loads(model_info)


@when("创建模型")
def 创建模型(context):
    resp = MockRequestClient().post('api/model/', context.model_info)
    context.model_id = resp["data"]["model_id"]


@then("模型已存在")
def 模型已存在(context):
    resp = MockRequestClient().get('api/model/')
    model_map = {i["model_id"]: i for i in resp["data"]}
    assert context.model_info["model_id"] == model_map[context.model_id]["model_id"]
    assert context.model_info["model_name"] == model_map[context.model_id]["model_name"]


@then("模型不存在")
def 模型不存在(context):
    resp = MockRequestClient().get('api/model/')
    model_set = {i["model_id"] for i in resp["data"]}
    assert context.model_id not in model_set


@when("删除模型")
def 删除模型(context):
    MockRequestClient().delete(f'api/model/{context.model_id}/')


@then("删除模型")
def 删除模型(context):
    MockRequestClient().delete(f'api/model/{context.model_id}/')


@given("初始化一个模型：{model_info}")
def 初始化一个模型(context, model_info):
    context.model_info = json.loads(model_info)
    resp = MockRequestClient().post('api/model/', context.model_info)
    context.model_id = resp["data"]["model_id"]


@when("创建模型属性：{attr_info}")
def 创建模型属性(context, attr_info):
    context.attr_info = json.loads(attr_info)
    resp = MockRequestClient().post(f'api/model/{context.model_id}/attr/', context.attr_info)
    context.attr_id = resp["data"]["attr_id"]


@then("模型属性已存在")
def 模型属性已存在(context):
    resp = MockRequestClient().get(f'api/model/{context.model_id}/attr_list/')
    attr_map = {i["attr_id"]: i for i in resp["data"]}

    assert context.attr_info["attr_id"] == attr_map[context.attr_id]["attr_id"]
    assert context.attr_info["attr_name"] == attr_map[context.attr_id]["attr_name"]


@then("模型属性不存在")
def 模型属性不存在(context):
    resp = MockRequestClient().get(f'api/model/{context.model_id}/attr_list/')
    attr_set = {i["attr_id"] for i in resp["data"]}

    assert context.attr_id not in attr_set


@when("删除模型属性")
def 删除模型属性(context):
    MockRequestClient().delete(f'api/model/{context.model_id}/attr/{context.attr_id}/')


@given("初始源模型：{src_model_info}，初始目标模型：{dst_model_info}")
def 初始化源模型与目标模型(context, src_model_info, dst_model_info):
    context.src_model_info = json.loads(src_model_info)
    src_resp = MockRequestClient().post('api/model/', context.src_model_info)
    context.src_model_id = src_resp["data"]["model_id"]

    context.dst_model_info = json.loads(dst_model_info)
    dst_resp = MockRequestClient().post('api/model/', context.dst_model_info)
    context.dst_model_id = dst_resp["data"]["model_id"]


@when("创建模型关联关系：{asst_id}")
def 创建模型关联关系(context, asst_id):
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


@then("模型关联关系已存在")
def 模型关联关系已存在(context):
    resp = MockRequestClient().get(f'api/model/{context.src_model_id}/association/')
    asso_map = {i["model_asst_id"]: i for i in resp["data"]}

    assert context.src_model_id == asso_map[context.model_asst_id]["src_model_id"]
    assert context.dst_model_id == asso_map[context.model_asst_id]["dst_model_id"]


@then("模型关联关系不存在")
def 模型关联关系不存在(context):
    resp = MockRequestClient().get(f'api/model/{context.src_model_id}/association/')
    asso_set = {i["model_asst_id"] for i in resp["data"]}

    assert context.model_asst_id not in asso_set


@when("删除模型关联关系")
def 删除模型关联关系(context):
    MockRequestClient().delete(f'api/model/association/{context.model_asst_id}/')


@then("删除模型关联关系")
def 删除模型关联关系(context):
    MockRequestClient().delete(f'api/model/association/{context.model_asst_id}/')


@then("删除源模型与目标模型")
def 删除源模型与目标模型(context):
    MockRequestClient().delete(f'api/model/{context.src_model_id}/')
    MockRequestClient().delete(f'api/model/{context.dst_model_id}/')
