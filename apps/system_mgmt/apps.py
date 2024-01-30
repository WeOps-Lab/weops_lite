from django.apps import AppConfig
from django.db.models.signals import post_migrate


class SystemMgmtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.system_mgmt'
    verbose_name = '系统管理'

    def ready(self):
        # 初始化自定义菜单的默认菜单
        from apps.system_mgmt.utils.menu import init_menu
        post_migrate.connect(init_menu, sender=self)
