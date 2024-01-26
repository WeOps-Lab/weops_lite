import logging
import os

from behave import given, when, then

from apps.core.utils.keycloak_client import KeyCloakClient

logger = logging.getLogger(__name__)
client = KeyCloakClient()
keycloak_test_admin = os.getenv('KEYCLOAK_TEST_ADMIN')
keycloak_test_admin_password = os.getenv('KEYCLOAK_TEST_ADMIN_PASSWORD')


@when('管理员用户输入账号和密码')
def 管理员用户输入账号和密码(context):
    logger.info('管理员用户输入账号和密码')


@then('成功获取用户的AccessToken')
def 成功获取用户的AccessToken(context):
    logger.info('成功获取用户的AccessToken')
