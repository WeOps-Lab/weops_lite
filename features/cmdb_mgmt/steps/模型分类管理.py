import json
from behave import given, when, then
from apps.core.features.utils.mock_request_client import MockRequestClient


@given("声明模型分类信息：{classfication_info}")
def 声明模型分类信息(context, classfication_info):
    context.classfication_info = json.loads(classfication_info)


@when("创建模型分类")
def 创建模型分类(context):
    resp = MockRequestClient().post('api/classification/', context.classfication_info)
    context.classfication_id = resp["data"]["classification_id"]


@then("模型分类已存在")
def 模型分类已存在(context):
    resp = MockRequestClient().get('api/classification/')
    classfication_map = {i["classification_id"]: i for i in resp["data"]}

    assert context.classfication_info["classification_id"] == classfication_map[context.classfication_id]["classification_id"]
    assert context.classfication_info["classification_name"] == classfication_map[context.classfication_id]["classification_name"]


@when("删除模型分类")
def 删除模型分类(context):
    MockRequestClient().delete(f'api/classification/{context.classfication_id}/')


@then("删除模型分类")
def 删除模型分类(context):
    MockRequestClient().delete(f'api/classification/{context.classfication_id}/')


@then("模型分类不存在")
def 模型分类不存在(context):
    resp = MockRequestClient().get('api/classification/')
    classfication_set = {i["classification_id"] for i in resp["data"]}
    assert context.classfication_id not in classfication_set
