import base64
import os

from django.conf import settings

from apps.core.models.vtype_mixin import VtypeMixin

# 普通用户角色
NORMAL = "normal"

# 超管用户角色
ADMIN = "admin"

# 默认logo
DEFAULT_LOGO_PATH = os.path.join(settings.BASE_DIR, "assets/img/default-logo.png")

# 系统设置表中提前置入的设置项
with open(DEFAULT_LOGO_PATH, "rb") as logo_file:
    SYSTEM_LOGO_INFO = {
        "key": "system_logo",
        "value": base64.b64encode(logo_file.read()).decode("utf8"),
        "vtype": VtypeMixin.STRING,
        "desc": "系统默认Logo",
    }

# 菜单管理默认菜单
MENU_DATA = {
    "menu_name": "默认菜单",
    "default": True,
    "use": True,
    "menu": list,
    "created_by": "admin",
    "updated_by": "admin",
}

# keycloak默认角色（查询角色列表要过滤掉默认角色）
BUILT_IN_ROLES = {
    f"default-roles-{os.getenv('KEYCLOAK_REALM')}",
    "default-roles-master",
    "uma_authorization",
    "offline_access",
}

# 模块
APP_MODULE = "系统管理"

# 本模块下的操作对象类型
USER = "用户"
ROLE = "角色"
GROUP = "用户组织"
MENU = "自定义菜单"
LOGO = "LOGO"
