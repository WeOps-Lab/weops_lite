from functools import wraps

from rest_framework import status
from rest_framework.response import Response

from apps.core.utils.keycloak_utils import KeyCloakUtils
from weops_lite.components.keycloak import KEYCLOAK_REALM


def uma_permission(permission):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):
            token = request.META.get('HTTP_AUTHORIZATION')
            if token is None:
                return Response({'error': '用户Token缺失'}, status=status.HTTP_403_FORBIDDEN)

            client = KeyCloakUtils.get_openid_client()
            token_info = client.introspect(token)
            if 'admin' in token_info['resource_access'][KEYCLOAK_REALM]['roles']:
                return view_func(self, request, *args, **kwargs)

            try:
                client.uma_permissions(token, permission)
                return view_func(self, request, *args, **kwargs)
            except:
                return Response({'error': '用户无此权限'}, status=status.HTTP_403_FORBIDDEN)

        return wrapper

    return decorator
