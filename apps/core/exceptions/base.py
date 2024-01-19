# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.utils.translation import gettext_lazy as _


class BlueException(Exception):

    ERROR_CODE = "0000000"
    MESSAGE = _("APP异常")
    STATUS_CODE = 500
    LOG_LEVEL = logging.ERROR

    def __init__(self, message=None, data=None, *args):
        """
        :param message: 错误消息
        :param data: 其他数据
        :param context: 错误消息 format dict
        :param args: 其他参数
        """
        super(BlueException, self).__init__(*args)
        self.message = self.MESSAGE if message is None else message
        self.data = data

    def render_data(self):
        return self.data

    def response_data(self):
        return {"result": False, "code": self.ERROR_CODE, "message": self.message, "data": self.render_data()}


class ClientBlueException(BlueException):

    MESSAGE = _("客户端请求异常")
    ERROR_CODE = "40000"
    STATUS_CODE = 400


class ServerBlueException(BlueException):

    MESSAGE = _("服务端服务异常")
    ERROR_CODE = "50000"
    STATUS_CODE = 500


class ResourceNotFound(ClientBlueException):

    MESSAGE = _("找不到请求的资源")
    ERROR_CODE = "40400"
    STATUS_CODE = 404


class ParamValidationError(ClientBlueException):

    MESSAGE = _("参数验证失败")
    ERROR_CODE = "40000"
    STATUS_CODE = 400


class ParamRequired(ClientBlueException):

    MESSAGE = _("关键参数缺失")
    ERROR_CODE = "40001"
    STATUS_CODE = 400
