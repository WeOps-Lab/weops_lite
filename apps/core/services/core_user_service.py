import logging

from apps.core.domain_models.user_token_entit import UserTokenEntity
from apps.core.utils.keycloak_utils import KeyCloakUtils


class CoreUserService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.client = KeyCloakUtils.get_openid_client()

    def get_user_access_token(self, username: str, password: str) -> UserTokenEntity:
        """
        获取用户的Access Token
        :param username:
        :param password:
        :return:
        """
        try:
            token = self.client.token(username, password)
            return UserTokenEntity(token=token['access_token'], error_message='', success=True)
        except Exception:
            return UserTokenEntity(token=None, error_message='用户名密码不匹配', success=False)
