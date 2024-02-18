import logging
import os
import requests
from dotenv import load_dotenv

from apps.core.entities.user_token_entit import UserTokenEntity
from apps.core.utils.keycloak_client import KeyCloakClient


class MockRequestClient:
    def __init__(self):
        load_dotenv()
        self.logger = logging.getLogger(__name__)
        self.client = KeyCloakClient()
        self.keycloak_test_admin = os.getenv('KEYCLOAK_TEST_ADMIN')
        self.keycloak_test_admin_password = os.getenv('KEYCLOAK_TEST_ADMIN_PASSWORD')
        self.test_base_url = os.getenv('TEST_BASE_URL')
        self.admin_token_info: UserTokenEntity = self.client.get_token(self.keycloak_test_admin,
                                                                       self.keycloak_test_admin_password)

    def get(self, url, role='admin'):
        headers = {
            'Authorization': f'{self.admin_token_info.token}'
        }
        response = requests.get(f'{self.test_base_url}/{url}', headers=headers)
        response.raise_for_status()
        return response.json()

    def post(self, url, data, role='admin'):
        headers = {
            'Authorization': f'{self.admin_token_info.token}',
            'Content-Type': 'application/json'
        }
        response = requests.post(f'{self.test_base_url}/{url}', json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def put(self, url, data, role='admin'):
        headers = {
            'Authorization': f'{self.admin_token_info.token}',
            'Content-Type': 'application/json'
        }
        response = requests.put(f'{self.test_base_url}/{url}', json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def delete(self, url, data=None, role='admin'):
        headers = {
            'Authorization': f'{self.admin_token_info.token}',
            'Content-Type': 'application/json'
        }
        response = requests.delete(f'{self.test_base_url}/{url}', json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def patch(self, url, data, role='admin'):
        headers = {
            'Authorization': f'{self.admin_token_info.token}',
            'Content-Type': 'application/json'
        }
        response = requests.patch(f'{self.test_base_url}/{url}', json=data, headers=headers)
        response.raise_for_status()
        return response.json()
