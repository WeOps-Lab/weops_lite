import base64
import os

from django.conf import settings

from apps.core.models.vtype_mixin import VtypeMixin

# 普通用户
NORMAL = "normal"

# 默认logo
DEFAULT_LOGO_PATH = os.path.join(settings.BASE_DIR, "static/img/default-logo.png")

# 系统设置表中提前置入的设置项
with open(DEFAULT_LOGO_PATH, "rb") as logo_file:
    SYSTEM_LOGO_INFO = {
        "key": "system_logo",
        "value": base64.b64encode(logo_file.read()).decode("utf8"),
        "vtype": VtypeMixin.STRING,
        "desc": "系统默认Logo",
    }
