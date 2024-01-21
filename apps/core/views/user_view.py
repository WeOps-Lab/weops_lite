import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.core.serializers.user_auth_serializer import UserAuthSerializer
from apps.core.services.core_user_service import CoreUserService
from apps.core.utils.keycloak_utils import KeyCloakUtils
from apps.core.utils.web_utils import WebUtils


class UserView(ViewSet):
    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.core_user_service = CoreUserService()

    @swagger_auto_schema(
        method="post",
        request_body=UserAuthSerializer,
        operation_description="获取用户token",
    )
    @action(methods=["POST"], detail=False, url_path=r"access_token")
    def access_token(self, request):
        serialize = UserAuthSerializer(data=request.data)
        if serialize.is_valid():
            validated_data = serialize.validated_data
            user_token_entity = self.core_user_service.get_user_access_token(validated_data['username'],
                                                                             validated_data['password'])
            if user_token_entity.success:
                return WebUtils.response_success({"token": user_token_entity.token})
            else:
                return WebUtils.response_error(error_message=user_token_entity.error_message)
        else:
            return WebUtils.response_error(error_message=serialize.error_messages)
