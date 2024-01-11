import logging

from apps.core.utils.salt_client import SaltClient


class TestSaltClient:
    def setup_method(self):
        self.logger = logging.getLogger(__name__)
        self.client = SaltClient()

    def test_init_client(self):
        self.logger.info(f'获取Token成功:{self.client.headers}')

    def test_execute_salt_ssh(self):
        result = self.client.execute_salt_ssh('cmd.run', '*', 'ps -ef')
        self.logger.info(f'任务执行结果为:{result}')

    def test_execute_salt_local(self):
        result = self.client.execute_salt_local('test.ping', '*', '')
        self.logger.info(f'任务执行结果为:{result}')

        result = self.client.execute_salt_local('cmd.run', '*', 'df -h')
        self.logger.info(f'任务执行结果为:{result}')
