import logging
import os

from apps.core.entities.user_token_entit import UserTokenEntity
from apps.core.utils.keycloak_client import KeyCloakClient


class TestKeycloakClient:
    def setup_method(self):
        self.logger = logging.getLogger(__name__)
        self.client = KeyCloakClient()
        self.keycloak_test_admin = os.getenv('KEYCLOAK_TEST_ADMIN')
        self.keycloak_test_admin_password = os.getenv('KEYCLOAK_TEST_ADMIN_PASSWORD')

    def test_get_userinfo(self):
        token_info: UserTokenEntity = self.client.get_token(self.keycloak_test_admin, self.keycloak_test_admin_password)
        self.client.get_userinfo(token_info.token)
