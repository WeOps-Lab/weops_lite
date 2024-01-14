import logging

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status

from apps.core.utils.keycloak_utils import KeyCloakUtils


class KeyCloakAuthMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        super().__init__(get_response)
        self.logger = logging.getLogger(__name__)

    def process_view(self, request, view, args, kwargs):
        # 只对/api的路径进行处理，其他路径默认放行
        if not request.path.startswith('/api'):
            return None

        # 查看视图是否有 login_exempt的豁免标记
        if getattr(view, "login_exempt", False):
            return None

        token = request.META.get('HTTP_AUTHORIZATION')
        if token is None:
            return HttpResponse("请提供Token", status=status.HTTP_401_UNAUTHORIZED)
        else:
            client = KeyCloakUtils.get_openid_client()

            try:
                token_info = client.introspect(token)
                if token_info.get('active'):
                    if 'admin' in token_info['resource_access']['weops_lite']['roles']:
                        request.META['X-SUPERUSER'] = True
                    return None
                else:
                    return HttpResponse("Token不合法", status=status.HTTP_401_UNAUTHORIZED)
            except:
                return HttpResponse("Token不合法", status=status.HTTP_401_UNAUTHORIZED)