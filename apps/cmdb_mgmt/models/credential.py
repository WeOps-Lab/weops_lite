from django.db import models


class RoleCredentialPermission(models.Model):
    model_id = models.CharField(max_length=100, db_index=True, verbose_name="模型ID")
    inst_id = models.BigIntegerField(db_index=True, verbose_name="凭据实例ID")
    role = models.CharField(max_length=100, db_index=True, verbose_name="角色")


class UserCredentialPermission(models.Model):
    model_id = models.CharField(max_length=100, db_index=True, verbose_name="模型ID")
    inst_id = models.BigIntegerField(db_index=True, verbose_name="凭据实例ID")
    user = models.CharField(max_length=100, db_index=True, verbose_name="用户")
