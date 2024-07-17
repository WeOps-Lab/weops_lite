import logging

from django.core.management import BaseCommand
from dotenv import load_dotenv


class Command(BaseCommand):
    help = '初始化模型'

    def handle(self, *args, **options):
        load_dotenv()
        logger = logging.getLogger(__name__)

        # 模型初始化
        logger.info(f'初始化模型！')

        from apps.cmdb_mgmt.migrate_model.service import MigrateModel
        MigrateModel().run()
