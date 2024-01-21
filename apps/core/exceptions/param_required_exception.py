from apps.core.exceptions.client_exception import ClientException


class ParamRequiredException(ClientException):
    MESSAGE = "关键参数缺失"
    ERROR_CODE = "40001"
    STATUS_CODE = 400
