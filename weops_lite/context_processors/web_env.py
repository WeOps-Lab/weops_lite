# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv

load_dotenv()


def custom_settings(request):
    """
    :summary: 这里可以返回前端需要的公共变量
    :param request:
    :return:
    """
    # TODO 前端需要的环境变量
    context = {
        "KEYCLOAK_URL": os.getenv("KEYCLOAK_URL"),
        "KEYCLOAK_REALM": os.getenv("KEYCLOAK_REALM"),
        "KEYCLOAK_UI_CLIENT_ID": os.getenv("KEYCLOAK_UI_CLIENT_ID"),
    }
    return context
