from django.db import models


class OperationLog(models.Model):
    class Meta:
        verbose_name = "操作记录"
        verbose_name_plural = verbose_name

    ADD = "add"
    INCREASE = "increase"
    MODIFY = "modify"
    EXEC = "exec"
    DELETE = "delete"
    REMOVE = "remove"
    DOWNLOAD = "download"
    UPLOAD = "upload"
    LOGIN = "login"
    IMPORT = "import"
    EXPORT = "export"
    OPERATE_TYPE_CHOICES = (
        (ADD, "新增"),
        (INCREASE, "添加"),
        (MODIFY, "修改"),
        (EXEC, "执行"),
        (DELETE, "删除"),
        (REMOVE, "移除"),
        (DOWNLOAD, "下载"),
        (UPLOAD, "上传"),
        (LOGIN, "登陆"),
    )
    OPERATE_TYPE_DICT = dict(OPERATE_TYPE_CHOICES)

    operator = models.CharField(max_length=128, null=True, db_index=True, verbose_name='操作者')
    operate_type = models.CharField(max_length=10, choices=OPERATE_TYPE_CHOICES, db_index=True, verbose_name='操作类型')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')
    operate_obj = models.CharField(max_length=200, default="", db_index=True, verbose_name='操作对象')
    operate_summary = models.TextField(default="", verbose_name='操作概要')
    app_module = models.CharField(max_length=20, default="", db_index=True, verbose_name='所属模块')
    obj_type = models.CharField(max_length=30, default="", db_index=True, verbose_name='对象类型')
