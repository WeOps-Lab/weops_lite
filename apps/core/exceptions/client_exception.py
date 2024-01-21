from apps.core.exceptions.base_app_exception import BaseAppException


class ClientException(BaseAppException):
    MESSAGE = "客户端请求异常"
    ERROR_CODE = "40000"
    STATUS_CODE = 400
