from django.db import models
from django.db.models import JSONField

from apps.core.models.maintainer_info import MaintainerInfo
from apps.core.models.time_info import TimeInfo


class MenuManage(TimeInfo, MaintainerInfo):
    menu_name = models.CharField(max_length=64, unique=True, help_text="菜单名称")
    default = models.BooleanField(default=False, help_text="是否是内置菜单")
    use = models.BooleanField(default=False, help_text="是否启用(只能有一个)")
    menu = JSONField(help_text="菜单内容")

    class Meta:
        verbose_name = "菜单管理"
