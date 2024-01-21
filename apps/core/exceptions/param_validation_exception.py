from apps.core.exceptions.client_exception import ClientException


class ParamValidationException(ClientException):
    MESSAGE = "参数验证失败"
    ERROR_CODE = "40000"
    STATUS_CODE = 400
