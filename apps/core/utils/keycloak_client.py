import json
import logging
import traceback

from keycloak import KeycloakAdmin, KeycloakOpenID
from singleton_decorator import singleton
from apps.core.entities.user_token_entit import UserTokenEntity
from weops_lite.components.keycloak import (
    KEYCLOAK_URL_API,
    KEYCLOAK_ADMIN_PASSWORD,
    KEYCLOAK_ADMIN_USERNAME,
    KEYCLOAK_REALM,
    KEYCLOAK_CLIENT_ID,
)


@singleton
class KeyCloakClient:
    def __init__(self):
        self.admin_client = KeycloakAdmin(
            server_url=KEYCLOAK_URL_API,
            username=KEYCLOAK_ADMIN_USERNAME,
            password=KEYCLOAK_ADMIN_PASSWORD,
        )
        self.realm_client = KeycloakAdmin(
            server_url=KEYCLOAK_URL_API,
            username=KEYCLOAK_ADMIN_USERNAME,
            password=KEYCLOAK_ADMIN_PASSWORD,
            realm_name=KEYCLOAK_REALM,
            client_id="admin-cli",
            user_realm_name="master",
        )
        self.client_secret_key, self.client_id = None, None
        self.openid_client = None
        self.logger = logging.getLogger(__name__)

    def get_openid_client(self):
        if self.openid_client is None:
            self.openid_client = KeycloakOpenID(
                server_url=KEYCLOAK_URL_API,
                client_id=KEYCLOAK_CLIENT_ID,
                realm_name=KEYCLOAK_REALM,
                client_secret_key=self.get_client_secret_key(),
            )
        return self.openid_client

    def set_client_secret_and_id(self):
        """设置域id与secret"""
        client_secret_key, client_id = None, None
        clients = self.realm_client.get_clients()
        for client in clients:
            if client["clientId"] == KEYCLOAK_CLIENT_ID:
                client_id = client["id"]
                client_secret_key = client["secret"]
                break
        self.client_secret_key, self.client_id = client_secret_key, client_id

    def get_client_secret_key(self):
        """获取客户端secret_key"""
        if self.client_secret_key is None:
            self.set_client_secret_and_id()
        return self.client_secret_key

    def get_client_id(self):
        """获取客户端client_id"""
        if self.client_id is None:
            self.set_client_secret_and_id()
        return self.client_id

    def get_realm_client(self):
        return self.realm_client

    def token_is_valid(self, token) -> (bool, dict):
        try:
            openid_client = self.get_openid_client()
            token_info = openid_client.introspect(token)
            if token_info.get("active"):
                return True, token_info
            else:
                return False, {}
        except Exception:
            return False, {}

    def get_userinfo(self, token: str):
        openid_client = self.get_openid_client()
        return openid_client.userinfo(token)

    def get_roles(self, token: str) -> list:
        try:
            openid_client = self.get_openid_client()
            token_info = openid_client.introspect(token)
            return token_info["realm_access"]["roles"]
        except Exception:
            self.logger.error("获取用户角色失败")
            return []

    def is_super_admin(self, token: str) -> bool:
        try:
            openid_client = self.get_openid_client()
            token_info = openid_client.introspect(token)
            if "admin" in token_info["realm_access"]["roles"]:
                return True
            else:
                return False
        except:
            return False

    def has_permission(self, token: str, permission: str) -> bool:
        try:
            openid_client = self.get_openid_client()
            openid_client.uma_permissions(token, permission)
            return True
        except:
            return False

    def get_token(self, username: str, password: str) -> UserTokenEntity:
        try:
            openid_client = self.get_openid_client()
            token = openid_client.token(username, password)
            return UserTokenEntity(
                token=token["access_token"], error_message="", success=True
            )
        except Exception as e:
            self.logger.error(e)
            return UserTokenEntity(
                token=None, error_message="用户名密码不匹配", success=False
            )

    def create_user(self, username, password, email, lastname, role_name) -> bool:
        try:
            role = self.realm_client.get_realm_role(role_name)
            user = {
                "username": username,
                "credentials": [
                    {"value": password, "type": "password", "temporary": False}
                ],
                "email": email,
                "lastName": lastname,
                "enabled": True,
            }
            user_id = self.realm_client.create_user(user, True)
            self.realm_client.assign_realm_roles(user_id, role)
            return True
        except Exception as e:
            traceback.print_exception(e)
            return False

    def import_realm_from_file(self, realm_config_path: str) -> bool:
        try:
            with open(realm_config_path, "r", encoding="utf8") as realm_config_file:
                realm_config = json.load(realm_config_file)
            self.admin_client.create_realm(payload=realm_config, skip_exists=True)
            return True
        except Exception as e:
            self.logger.error(e)
            return False
