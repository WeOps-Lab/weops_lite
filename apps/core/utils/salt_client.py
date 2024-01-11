import requests

from weops_lite.components.saltstack import SALT_API_URL, SALT_API_PASSWORD, SALT_API_USERNAME


class SaltClient:
    def __init__(self):
        try:
            self.headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
            response = requests.post(f"{SALT_API_URL}/login", headers=self.headers, json={
                'username': SALT_API_USERNAME,
                'password': SALT_API_PASSWORD,
                'eauth': 'pam',
            })
            response.raise_for_status()
        except Exception as err:
            raise ValueError(f"Error in login process: {err}")
        
        result = response.json()
        token = result['return'][0]['token']
        self.headers['X-Auth-Token'] = token
