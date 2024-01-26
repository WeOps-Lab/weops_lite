from behave import given, when, then
from dotenv import load_dotenv

from apps.core.features.utils.mock_request_client import MockRequestClient

load_dotenv()


@when('用户点击获取自己的用户信息')
def 用户点击获取自己的用户信息(context):
    context.user_info = MockRequestClient().get('api/login_info/')


@then('用户的名称是 {username}')
def 用户的名称是_username(context, username):
    assert context.user_info['data']['user_info']['name'] == username
