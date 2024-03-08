import json
import os

from django.conf import settings

AUTH_TOKEN_HEADER_NAME = 'HTTP_AUTHORIZATION'

DEBUG_USERINFO = {
    "username": "debug-user",
    "email": "",
}

# 域配置文件路径
REALM_FILE_PATH = os.path.join(settings.BASE_DIR, "support-files/keycloak/realm-export-v1.json")

with open(REALM_FILE_PATH, "r", encoding="utf-8") as f:
    REALM_SETTINGS = json.load(f)

# 默认组织ID
DEFAULT_GROUP_ID = REALM_SETTINGS["groups"][0]["id"]

# 默认图名称
GRAPH_NAME = "cmdb"
