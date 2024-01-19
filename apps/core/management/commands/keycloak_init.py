import json
import logging

from django.core.management import BaseCommand
from dotenv import load_dotenv

from apps.core.utils.keycloak_utils import KeyCloakUtils
from weops_lite.components.keycloak import KEYCLOAK_URL


class Command(BaseCommand):
    help = 'KeyCloak Realm 数据初始化'

    def handle(self, *args, **options):
        load_dotenv()
        logger = logging.getLogger(__name__)
        logger.info(f'初始化KeyCloak Realm,KeyCloak URL:[{KEYCLOAK_URL}]')

        keycloak_admin = KeyCloakUtils.get_admin_client()

        realm_config_file_path = 'support-files/keycloak/realm-export-weops.json'
        with open(realm_config_file_path, 'r', encoding='utf8') as realm_config_file:
            realm_config = json.load(realm_config_file)

        keycloak_admin.create_realm(payload=realm_config, skip_exists=True)
        logger.info(f'初始化KeyCloak Realm 完成')
