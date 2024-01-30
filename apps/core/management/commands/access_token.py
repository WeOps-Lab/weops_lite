import logging

from django.core.management import BaseCommand
from dotenv import load_dotenv

from apps.core.utils.keycloak_client import KeyCloakClient


class Command(BaseCommand):
    help = '获取Access Token'

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str, required=True, help="用户名")
        parser.add_argument("--password", type=str, required=True, help="密码")

    def handle(self, *args, **options):
        load_dotenv()
        logger = logging.getLogger(__name__)

        username = options['username']
        password = options['password']

        entity = KeyCloakClient().get_token(username, password)
        if entity.success:
            with open('token', mode='w', encoding='utf-8') as f:
                f.writelines(entity.token)
            logger.info('Token已写入token文件中')
        else:
            logger.error(entity.error_message)
