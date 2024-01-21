import logging

from django.core.management import BaseCommand, CommandError
from dotenv import load_dotenv

from apps.core.utils.keycloak_client import KeyCloakClient
from weops_lite.components.keycloak import KEYCLOAK_CLIENT_ID


class Command(BaseCommand):
    help = '创建KeyCloak用户'

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str, required=True, help='用户名')
        parser.add_argument("--password", type=str, required=True, help='密码')
        parser.add_argument("--email", type=str, required=True, help='邮箱地址')
        parser.add_argument("--lastname", type=str, required=True, help='用户显示名称')
        parser.add_argument("--role_name", nargs="?", default='normal', type=str)

    def handle(self, *args, **options):
        load_dotenv()
        logger = logging.getLogger(__name__)

        username = options['username']
        password = options['password']
        email = options['email']
        lastname = options['lastname']
        role_name = options['role_name']

        client = KeyCloakClient()
        result = client.create_user(username, password, email, lastname, role_name)
        if result is True:
            logger.info(f"用户[{username}]创建成功")
        else:
            logger.error(f"用户[{username}]创建失败")
