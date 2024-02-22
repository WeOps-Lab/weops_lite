import pytest
from apps.core.utils.keycloak_client import KeyCloakClient


class TestKeycloakClient:
    @pytest.fixture
    def client(self, mocker):
        mocker.patch("apps.core.utils.keycloak_client.KeycloakAdmin")
        mocker.patch("apps.core.utils.keycloak_client.KeycloakOpenID")
        mocker.patch(
            "apps.core.utils.keycloak_client.KEYCLOAK_CLIENT_ID", new="weops_lite"
        )
        return KeyCloakClient()

    def test_set_client_secret_and_id(self, client, mocker):
        mocker.patch.object(
            client.realm_client,
            "get_clients",
            return_value=[
                {"clientId": "weops_lite", "id": "weops_lite", "secret": "test_secret"}
            ],
        )
        client_secret_key, client_id = client.set_client_secret_and_id()
        assert client_secret_key == "test_secret"
        assert client_id == "weops_lite"

    def test_get_client_secret_key(self, client):
        assert client.get_client_secret_key() == client.client_secret_key

    def test_get_client_id(self, client):
        assert client.get_client_id() == client.client_id

    def test_token_is_valid(self, client, mocker):
        mocker.patch.object(
            client.openid_client, "introspect", return_value={"active": True}
        )
        is_valid, _ = client.token_is_valid("test_token")
        assert is_valid

    def test_get_userinfo(self, client, mocker):
        mocker.patch.object(
            client.openid_client, "userinfo", return_value={"username": "test_user"}
        )
        userinfo = client.get_userinfo("test_token")
        assert userinfo["username"] == "test_user"

    def test_create_user(self, client, mocker):
        mocker.patch.object(
            client.realm_client, "get_realm_role", return_value="test_role"
        )
        mocker.patch.object(
            client.realm_client, "create_user", return_value="test_user_id"
        )
        mocker.patch.object(
            client.realm_client, "assign_realm_roles", return_value=None
        )
        result = client.create_user(
            "test_user", "test_password", "test_email", "test_lastname", "test_role"
        )
        assert result

    def test_import_realm_from_file(self, client, mocker):
        mocker.patch(
            "builtins.open", mocker.mock_open(read_data='{"realm": "test_realm"}')
        )
        mocker.patch.object(client.admin_client, "create_realm", return_value=True)
        result = client.import_realm_from_file("test_realm_config_path")
        assert result

    def test_token_is_valid_with_exception(self, client, mocker):
        mocker.patch.object(client.openid_client, "introspect", side_effect=Exception())
        is_valid, _ = client.token_is_valid("test_token")
        assert not is_valid

    def test_get_userinfo_with_exception(self, client, mocker):
        mocker.patch.object(client.openid_client, "userinfo", side_effect=Exception())
        with pytest.raises(Exception):
            client.get_userinfo("test_token")

    def test_create_user_with_exception(self, client, mocker):
        mocker.patch.object(
            client.realm_client, "get_realm_role", side_effect=Exception()
        )
        result = client.create_user(
            "test_user", "test_password", "test_email", "test_lastname", "test_role"
        )
        assert not result

    def test_import_realm_from_file_with_exception(self, client, mocker):
        mocker.patch(
            "builtins.open", mocker.mock_open(read_data='{"realm": "test_realm"}')
        )
        mocker.patch.object(
            client.admin_client, "create_realm", side_effect=Exception()
        )
        result = client.import_realm_from_file("test_realm_config_path")
        assert not result

    def test_get_token_with_exception(self, client, mocker):
        mocker.patch.object(client.openid_client, "token", side_effect=Exception())
        token_entity = client.get_token("test_username", "test_password")
        assert token_entity.token is None
        assert not token_entity.success

    def test_get_realm_client(self, client):
        assert client.get_realm_client() == client.realm_client

    def test_get_roles(self, client, mocker):
        mocker.patch.object(
            client.openid_client,
            "introspect",
            return_value={"realm_access": {"roles": ["admin", "user"]}},
        )
        roles = client.get_roles("test_token")
        assert roles == ["admin", "user"]

    def test_get_token_with_exception(self, client, mocker):
        mocker.patch.object(client.openid_client, "token", side_effect=Exception())
        token_entity = client.get_token("test_username", "test_password")
        assert token_entity.token is None
        assert not token_entity.success

    def test_get_roles_with_exception(self, client, mocker):
        mocker.patch.object(client.openid_client, "introspect", side_effect=Exception())
        with pytest.raises(Exception):
            client.get_roles("test_token")
