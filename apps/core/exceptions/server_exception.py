from apps.core.exceptions.base_app_exception import BaseAppException


class ServerException(BaseAppException):
    MESSAGE = "服务端服务异常"
    ERROR_CODE = "50000"
    STATUS_CODE = 500
