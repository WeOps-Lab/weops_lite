import wrapt
from rest_framework import status
from rest_framework.response import Response

from apps.core.constants import AUTH_TOKEN_HEADER_NAME
from apps.core.utils.keycloak_utils import KeyCloakUtils
from weops_lite.components.keycloak import KEYCLOAK_CLIENT_ID


def uma_permission(permission):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        token = args[0].META.get(AUTH_TOKEN_HEADER_NAME)
        if token is None:
            return Response({'error': '用户Token缺失'}, status=status.HTTP_403_FORBIDDEN)
        client = KeyCloakUtils.get_openid_client()
        token_info = client.introspect(token)
        if 'admin' in token_info['resource_access'][KEYCLOAK_CLIENT_ID]['roles']:
            return wrapped(*args, **kwargs)

        try:
            client.uma_permissions(token, permission)
            return wrapped(*args, **kwargs)
        except:
            return Response({'error': '用户无此权限'}, status=status.HTTP_403_FORBIDDEN)

    return wrapper
