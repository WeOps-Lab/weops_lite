import logging

from apps.system_mgmt.constants import MENU_DATA
from apps.system_mgmt.models import MenuManage


logger = logging.getLogger("apps")


def init_menu(**kwargs):
    """
    初始化默认的菜单
    """
    _, created = MenuManage.objects.get_or_create(menu_name=MENU_DATA["menu_name"], defaults=MENU_DATA)
    logger.info("初始化默认菜单完成. create={}".format(created))