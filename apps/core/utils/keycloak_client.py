import json
import logging
import traceback

from dotenv import load_dotenv
from keycloak import KeycloakAdmin, KeycloakOpenID
from singleton_decorator import singleton
from apps.core.entities.user_token_entit import UserTokenEntity
from weops_lite.components.keycloak import KEYCLOAK_URL, KEYCLOAK_ADMIN_PASSWORD, KEYCLOAK_ADMIN_USERNAME, \
    KEYCLOAK_REALM, KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET_KEY


@singleton
class KeyCloakClient:
    def __init__(self):
        self.admin_client = KeycloakAdmin(server_url=KEYCLOAK_URL, username=KEYCLOAK_ADMIN_USERNAME,
                                          password=KEYCLOAK_ADMIN_PASSWORD)
        self.realm_client = KeycloakAdmin(server_url=KEYCLOAK_URL, username=KEYCLOAK_ADMIN_USERNAME,
                                          password=KEYCLOAK_ADMIN_PASSWORD, realm_name=KEYCLOAK_REALM,
                                          client_id="admin-cli", user_realm_name="master")
        self.openid_client = KeycloakOpenID(
            server_url=KEYCLOAK_URL,
            client_id=KEYCLOAK_CLIENT_ID,
            realm_name=KEYCLOAK_REALM,
            client_secret_key=KEYCLOAK_CLIENT_SECRET_KEY)
        self.logger = logging.getLogger(__name__)

    def get_realm_client(self):
        return self.realm_client

    def token_is_valid(self, token) -> (bool, dict):
        token_info = self.openid_client.introspect(token)
        if token_info.get('active'):
            return True, token_info
        else:
            return False, {}

    def get_userinfo(self, token: str):
        return self.openid_client.userinfo(token)

    def get_roles(self, token: str) -> list:
        token_info = self.openid_client.introspect(token)
        return token_info['realm_access']['roles']

    def is_super_admin(self, token: str) -> bool:
        token_info = self.openid_client.introspect(token)
        if 'admin' in token_info['realm_access']['roles']:
            return True
        else:
            return False

    def has_permission(self, token: str, permission: str) -> bool:
        try:
            self.openid_client.uma_permissions(token, permission)
            return True
        except:
            return False

    def get_token(self, username: str, password: str) -> UserTokenEntity:
        try:
            token = self.openid_client.token(username, password)
            return UserTokenEntity(token=token['access_token'], error_message='', success=True)
        except Exception as e:
            self.logger.error(e)
            return UserTokenEntity(token=None, error_message='用户名密码不匹配', success=False)

    def create_user(self, username, password, email, lastname, role_name) -> bool:
        try:
            client_id = self.realm_client.get_client_id(KEYCLOAK_CLIENT_ID)
            role = self.realm_client.get_client_role(client_id, role_name)
            user = {
                'username': username,
                'credentials': [{"value": password, "type": 'password', 'temporary': False}],
                'email': email,
                'lastName': lastname,
                'enabled': True
            }
            user_id = self.realm_client.create_user(user)
            self.realm_client.assign_client_role(user_id, client_id, role)
            return True
        except Exception as e:
            traceback.print_exception(e)
            return False

    def import_realm_from_file(self, realm_config_path: str) -> bool:
        try:
            with open(realm_config_path, 'r', encoding='utf8') as realm_config_file:
                realm_config = json.load(realm_config_file)
            self.admin_client.create_realm(payload=realm_config, skip_exists=True)
            return True
        except Exception as e:
            self.logger.error(e)
            return False
