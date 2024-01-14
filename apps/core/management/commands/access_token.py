import logging

from django.core.management import BaseCommand, CommandError
from dotenv import load_dotenv

from apps.core.utils.keycloak_utils import KeyCloakUtils


class Command(BaseCommand):
    help = '获取Access Token'

    def add_arguments(self, parser):
        parser.add_argument("--username", type=str)
        parser.add_argument("--password", type=str)

    def handle(self, *args, **options):
        load_dotenv()
        logger = logging.getLogger(__name__)

        if not options['username']:
            raise CommandError("参数 'username' 是必填的")
        username = options.get('username')

        if not options['password']:
            raise CommandError("参数 'password' 是必填的")
        password = options.get('password')

        client = KeyCloakUtils.get_openid_client()
        token = client.token(username, password)
        logger.info(token['access_token'])
