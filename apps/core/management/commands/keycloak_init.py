import json
import logging
import os

from django.core.management import BaseCommand
from dotenv import load_dotenv
from keycloak import KeycloakAdmin, KeycloakOpenIDConnection

from weops_lite.components.base import BASE_DIR
from weops_lite.components.keycloak import KEYCLOAK_URL, KEYCLOAK_ADMIN_USERNAME, KEYCLOAK_ADMIN_PASSWORD, \
    KEYCLOAK_REALM, KEYCLOAK_CLIENT_ID


class Command(BaseCommand):
    help = 'KeyCloak Realm 数据初始化'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('初始化KeyCloak Realm......')
        load_dotenv()
        logger = logging.getLogger(__name__)

        keycloak_admin = KeycloakAdmin(server_url=KEYCLOAK_URL,
                                       username=KEYCLOAK_ADMIN_USERNAME,
                                       password=KEYCLOAK_ADMIN_PASSWORD)

        realm_config_file_path = 'support-files/keycloak/realm-export-weops.json'
        with open(realm_config_file_path, 'r', encoding='utf8') as realm_config_file:
            realm_config = json.load(realm_config_file)

        target_realm = realm_config['realm']
        realms = keycloak_admin.get_realms()
        realm_exist = False
        for realm in realms:
            if realm['realm'] == target_realm:
                realm_exist = True
                break
        if realm_exist:
            logger.warning(f'Realm [{target_realm}] 已存在,跳过创建')
        else:
            logger.info(f'创建[{target_realm}]......')
            keycloak_admin.create_realm(payload=realm_config, skip_exists=True)

        #TODO: init realm super admin