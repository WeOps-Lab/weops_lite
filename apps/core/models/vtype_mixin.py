from django.db import models
from django.db.models import JSONField, CharField, IntegerField, FloatField, DateTimeField, DateField, TimeField, Field, \
    BooleanField


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
