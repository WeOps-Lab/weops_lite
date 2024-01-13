from keycloak import KeycloakAdmin

from weops_lite.components.keycloak import KEYCLOAK_URL, KEYCLOAK_ADMIN_PASSWORD, KEYCLOAK_ADMIN_USERNAME, \
    KEYCLOAK_REALM


class KeyCloakUtils:
    @staticmethod
    def get_admin_client():
        return KeycloakAdmin(server_url=KEYCLOAK_URL, username=KEYCLOAK_ADMIN_USERNAME,
                             password=KEYCLOAK_ADMIN_PASSWORD)

    @staticmethod
    def get_realm_client():
        return KeycloakAdmin(server_url=KEYCLOAK_URL, username=KEYCLOAK_ADMIN_USERNAME,
                             password=KEYCLOAK_ADMIN_PASSWORD, realm_name=KEYCLOAK_REALM,
                             client_id="admin-cli", user_realm_name="master")
