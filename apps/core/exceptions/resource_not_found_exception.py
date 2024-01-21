from apps.core.exceptions.client_exception import ClientException


class ResourceNotFoundException(ClientException):
    MESSAGE = "找不到请求的资源"
    ERROR_CODE = "40400"
    STATUS_CODE = 404
