from django.db import models

from apps.system_mgmt.constants import ADMIN


class GradedRole(models.Model):
    role = models.CharField(unique=True, max_length=100, verbose_name='角色名')
    superior_role = models.CharField(db_index=True, max_length=100, default=ADMIN, verbose_name='上级角色')

    class Meta:
        verbose_name = "分级角色表"
        verbose_name_plural = verbose_name
