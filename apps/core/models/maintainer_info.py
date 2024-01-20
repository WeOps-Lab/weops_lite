from django.db import models


class MaintainerInfo(models.Model):
    """
    Add maintainer fields to another models.
    """

    class Meta:
        verbose_name = "维护者相关字段"
        abstract = True

    created_by = models.CharField("创建者", max_length=32, default="")
    updated_by = models.CharField("更新者", max_length=32, default="")
