import logging

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from apps.core.utils.keycloak_utils import KeyCloakUtils


class KeyCloakLoginRequiredMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        super().__init__(get_response)
        self.logger = logging.getLogger(__name__)

    def process_view(self, request, view, args, kwargs):
        pass

    def process_response(self, request, response):
        return response
