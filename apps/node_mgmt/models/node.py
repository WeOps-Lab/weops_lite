from django.db import models
from django.db.models import JSONField

from apps.core.models.maintainer_info import MaintainerInfo
from apps.core.models.time_info import TimeInfo
from apps.node_mgmt.constants import NOT_INSTALLED


class Node(TimeInfo, MaintainerInfo):

    # 节点信息
    model_id = models.CharField(max_length=100, db_index=True, verbose_name="模型ID")
    node_id = models.BigIntegerField(unique=True, verbose_name="节点ID")
    node_name = models.CharField(max_length=100, verbose_name="节点名称")
    node_ip = models.CharField(max_length=100, verbose_name="IP地址")

    # sidecar同步信息
    sidecar_status = models.CharField(default=NOT_INSTALLED, max_length=100, verbose_name="sidecar状态")
    sidecar_sync_time = models.DateTimeField(null=True, blank=True, verbose_name="sidecar同步时间")
    sidecar_config = JSONField(default=dict, verbose_name="sidecar配置信息")
