import logging
import os

from keycloak import KeycloakOpenID

from apps.core.utils.keycloak_client import KeyCloakClient
from weops_lite.components.keycloak import KEYCLOAK_URL, KEYCLOAK_REALM, KEYCLOAK_CLIENT_SECRET_KEY


class TestUmaPermission:
    def setup_method(self):
        self.logger = logging.getLogger(__name__)
        self.client = KeyCloakClient()
        self.openid_client = KeycloakOpenID(
            server_url=KEYCLOAK_URL,
            client_id='weops-lite-web',
            realm_name=KEYCLOAK_REALM,
            client_secret_key=KEYCLOAK_CLIENT_SECRET_KEY)
        self.keycloak_test_admin = os.getenv('KEYCLOAK_TEST_ADMIN')
        self.keycloak_test_admin_password = os.getenv('KEYCLOAK_TEST_ADMIN_PASSWORD')
        self.test_token = self.openid_client.token(self.keycloak_test_admin, self.keycloak_test_admin_password)[
            'access_token']

    def test_is_superadmin(self):
        result = self.client.is_super_admin(self.test_token)
        self.logger.info(result)

        result = self.client.has_permission(self.test_token, 'sys_group_create')
        self.logger.info(result)
