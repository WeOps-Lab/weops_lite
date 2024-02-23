import pytest
from apps.core.constants import AUTH_TOKEN_HEADER_NAME
from apps.core.decorators.uma_permission import uma_permission

from apps.core.utils.keycloak_client import KeyCloakClient
from weops_lite.components.base import DEBUG


class MockRequest:
    def __init__(self, headers=None):
        self.META = headers


class TestUmaPermission:

    def test_uma_permission_with_valid_token_for_super_admin(
        self, mocker, keycloak_client
    ):
        mocker.patch.object(keycloak_client, "is_super_admin", return_value=True)

        @uma_permission("permission")
        def wrapped_func(request):
            return "success"

        request = MockRequest(headers={AUTH_TOKEN_HEADER_NAME: "Bearer valid_token"})
        response = wrapped_func(request)

        assert response == "success"

    def test_uma_permission_with_valid_token_and_permission(
        self, mocker, keycloak_client
    ):
        mocker.patch.object(keycloak_client, "is_super_admin", return_value=False)
        mocker.patch.object(keycloak_client, "has_permission", return_value=True)

        @uma_permission("permission")
        def wrapped_func(request):
            return "success"

        request = MockRequest(headers={AUTH_TOKEN_HEADER_NAME: "Bearer valid_token"})
        response = wrapped_func(request)

        assert response == "success"

    def test_uma_permission_with_invalid_token(self, mocker, keycloak_client):
        mocker.patch.object(keycloak_client, "is_super_admin", return_value=False)

        @uma_permission("permission")
        def wrapped_func(request):
            return "success"

        request = MockRequest(headers={})
        response = wrapped_func(request)
        assert response.status_code == 403

    def test_uma_permission_with_invalid_permission(self, mocker, keycloak_client):
        mocker.patch.object(keycloak_client, "is_super_admin", return_value=False)
        mocker.patch.object(keycloak_client, "has_permission", return_value=False)

        @uma_permission("permission")
        def wrapped_func(request):
            return "success"

        request = MockRequest(headers={"HTTP_AUTHORIZATION": "Bearer valid_token"})
        response = wrapped_func(request)

        assert response.status_code == 403
