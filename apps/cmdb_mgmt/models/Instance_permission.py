from django.db import models
from django.db.models import JSONField

from apps.core.models.maintainer_info import MaintainerInfo
from apps.core.models.time_info import TimeInfo


class InstancePermission(TimeInfo, MaintainerInfo):

    role_id = models.CharField(max_length=100, db_index=True, verbose_name="角色ID")
    model_id = models.CharField(max_length=100, db_index=True, verbose_name="模型ID")
    conditions = JSONField(default=list, verbose_name="条件列表")
