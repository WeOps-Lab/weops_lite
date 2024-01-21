import json
import logging

from django.core.management import BaseCommand
from dotenv import load_dotenv

from apps.core.utils.keycloak_client import KeyCloakClient
from weops_lite.components.keycloak import KEYCLOAK_URL


class Command(BaseCommand):
    help = 'KeyCloak Realm 数据初始化'

    def handle(self, *args, **options):
        load_dotenv()
        logger = logging.getLogger(__name__)

        logger.info(f'初始化KeyCloak Realm,KeyCloak URL:[{KEYCLOAK_URL}]')

        client = KeyCloakClient()

        realm_config_file_path = 'support-files/keycloak/realm-export-weops.json'
        result = client.import_realm_from_file(realm_config_file_path)
        if result is True:
            logger.info(f'初始化KeyCloak Realm 完成')
        else:
            logger.error(f'初始化KeyCloak Realm 失败')
