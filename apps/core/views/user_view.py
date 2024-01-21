import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.core.serializers.user_auth_serializer import UserAuthSerializer
from apps.core.utils.keycloak_utils import KeyCloakUtils


class UserView(ViewSet):
    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)

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
            client = KeyCloakUtils.get_openid_client()
            try:
                token = client.token(validated_data['username'], validated_data['password'])
                return Response({"token": token['access_token']})
            except Exception as e:
                return Response({"error_message": "用户名密码不匹配"})
        else:
            return Response({"error_message": serialize.error_messages})
