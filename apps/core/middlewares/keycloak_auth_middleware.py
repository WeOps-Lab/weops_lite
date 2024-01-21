import logging

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status

from apps.core.utils.keycloak_client import KeyCloakClient
from apps.core.utils.web_utils import WebUtils
from weops_lite.components.base import DEBUG


class KeyCloakAuthMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        super().__init__(get_response)
        self.logger = logging.getLogger(__name__)
        self.keyclock_client = KeyCloakClient()

    def process_view(self, request, view, args, kwargs):
        # 开发模式，默认放行
        if DEBUG is True:
            return None

        # 只对/api的路径进行处理，其他路径默认放行
        if not request.path.startswith('/api') or request.path.startswith('/api/public/'):
            return None

        token = request.META.get('HTTP_AUTHORIZATION')
        if token is None:
            return WebUtils.response_error(error_message='请提供Token', status=status.HTTP_401_UNAUTHORIZED)

        if self.keyclock_client.token_is_valid(token):
            return None
        else:
            return WebUtils.response_error(error_message='Token不合法', status=status.HTTP_401_UNAUTHORIZED)
