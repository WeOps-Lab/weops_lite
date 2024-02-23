import pytest

from apps.core.utils.keycloak_client import KeyCloakClient


@pytest.fixture
def keycloak_client(mocker):
    mocker.patch("apps.core.utils.keycloak_client.KeycloakAdmin")
    mocker.patch("apps.core.utils.keycloak_client.KeycloakOpenID")
    mocker.patch("apps.core.utils.keycloak_client.KEYCLOAK_CLIENT_ID", new="weops_lite")
    return KeyCloakClient()
