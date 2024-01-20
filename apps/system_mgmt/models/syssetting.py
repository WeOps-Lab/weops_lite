from django.db import models

from apps.core.models.maintainer_info import MaintainerInfo
from apps.core.models.time_info import TimeInfo
from apps.core.models.vtype_mixin import VtypeMixin


class SysSetting(TimeInfo, MaintainerInfo, VtypeMixin):
    key = models.CharField(verbose_name="设置项", max_length=100, unique=True)
    value = models.TextField(verbose_name="设置值")
    desc = models.CharField(verbose_name="设置描述", max_length=200, default="")

    class Meta:
        verbose_name = "系统设置"

    @property
    def real_value(self):
        try:
            func = self.VTYPE_FIELD_MAPPING.get(self.vtype, self.VTYPE_FIELD_MAPPING[self.DEFAULT])
            value = func().to_python(self.value)
            return value
        except Exception:
            return self.value

    def get_ins_summary(self):
        return "{}[系统设置: {}]".format(self._meta.verbose_name, self.desc)
