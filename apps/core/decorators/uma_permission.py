from functools import wraps

from rest_framework import status
from rest_framework.response import Response

from apps.core.utils.keycloak_utils import KeyCloakUtils


def uma_permission(permission):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(self, request, *args, **kwargs):
            token = request.META.get('HTTP_AUTHORIZATION')
            if token is None:
                return Response({'error': '用户Token缺失'}, status=status.HTTP_403_FORBIDDEN)

            try:
                KeyCloakUtils().get_openid_client().uma_permissions(token, permission)
                return view_func(self, request, *args, **kwargs)
            except:
                return Response({'error': '用户无此权限'}, status=status.HTTP_403_FORBIDDEN)

        return wrapper

    return decorator
