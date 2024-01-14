from keycloak import KeycloakAdmin, KeycloakOpenID

from weops_lite.components.keycloak import KEYCLOAK_URL, KEYCLOAK_ADMIN_PASSWORD, KEYCLOAK_ADMIN_USERNAME, \
    KEYCLOAK_REALM, KEYCLOAK_CLIENT_ID, KEYCLOAK_CLIENT_SECRET_KEY


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

    @staticmethod
    def get_openid_client():
        client = KeycloakOpenID(
            server_url=KEYCLOAK_URL,
            client_id=KEYCLOAK_CLIENT_ID,
            realm_name=KEYCLOAK_REALM,
            client_secret_key=KEYCLOAK_CLIENT_SECRET_KEY)
        return client
