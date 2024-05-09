from django.db import models
from django.db.models import JSONField

from apps.core.models.maintainer_info import MaintainerInfo
from apps.core.models.time_info import TimeInfo


QUERY = "query"
MANAGE = "manage"

PERMISSION_TYPE_CHOICES = [
    (QUERY, "查询"),
    (MANAGE, "管理"),
]


class InstancePermission(TimeInfo, MaintainerInfo):

    role_id = models.CharField(max_length=100, db_index=True, verbose_name="角色ID")
    model_id = models.CharField(max_length=100, db_index=True, verbose_name="模型ID")
    permission_type = models.CharField(max_length=100, db_index=True, choices=PERMISSION_TYPE_CHOICES, default=QUERY, verbose_name="权限类型")
    conditions = JSONField(default=list, verbose_name="条件列表")


class UserInstancePermission(TimeInfo, MaintainerInfo):

    username = models.CharField(max_length=100, db_index=True, verbose_name="用户名")
    model_id = models.CharField(max_length=100, db_index=True, verbose_name="模型ID")
    permission_type = models.CharField(max_length=100, db_index=True, choices=PERMISSION_TYPE_CHOICES, default=QUERY, verbose_name="权限类型")
    conditions = JSONField(default=list, verbose_name="条件列表")
