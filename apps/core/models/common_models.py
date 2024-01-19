# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import JSONField, CharField, IntegerField, FloatField, DateTimeField, DateField, TimeField, Field, BooleanField


class TimeInfo(models.Model):
    """
    Add time fields to another models.
    """

    class Meta:
        verbose_name = "时间相关字段"
        abstract = True

    created_at = models.DateTimeField("创建时间", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)


class MaintainerInfo(models.Model):
    """
    Add maintainer fields to another models.
    """

    class Meta:
        verbose_name = "维护者相关字段"
        abstract = True

    created_by = models.CharField("创建者", max_length=32, default="")
    updated_by = models.CharField("更新者", max_length=32, default="")


class VtypeMixin(models.Model):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    DATETIME = "datetime"
    TIME = "time"
    DATE = "date"
    JSON = "json"
    BOOLEAN = "bool"
    DEFAULT = "default"

    VTYPE_FIELD_MAPPING = {
        STRING: CharField,
        INTEGER: IntegerField,
        FLOAT: FloatField,
        DATETIME: DateTimeField,
        DATE: DateField,
        TIME: TimeField,
        JSON: JSONField,
        BOOLEAN: BooleanField,
        DEFAULT: Field,
    }
    VTYPE_CHOICE = (
        (STRING, "字符串"),
        (INTEGER, "整型"),
        (FLOAT, "浮点型"),
        (DATETIME, "时间日期"),
        (TIME, "时间"),
        (DATE, "日期"),
        (JSON, "JSON"),
        (BOOLEAN, "布尔值"),
        (DEFAULT, "其它"),
    )

    vtype = models.CharField("类型", max_length=32, default=STRING)

    class Meta:
        verbose_name = "文本值类型"
        abstract = True
