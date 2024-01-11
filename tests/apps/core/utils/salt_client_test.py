from apps.core.utils.salt_client import SaltClient


class TestSaltClient:
    def setup_method(self):
        self.client = SaltClient()

    def test_client(self):
        print(self.client.headers)
