from apps.core.exceptions.base_app_exception import BaseAppException


class UploadFileUtils:
    def __init__(self, file_obj):
        if not file_obj:
            raise BaseAppException("文件不存在，请添加文件!")
        self.file_obj = file_obj

    def _check_mime_type(self, correct_mime_type):
        # 限制文件MIME Type
        if self.file_obj.content_type not in correct_mime_type:
            raise BaseAppException("文件类型错误, 请上传正确格式!")

    def _check_file_name(self, end_rule=None):
        # 限制文件后缀
        if end_rule:
            file_name = self.file_obj.name.strip('"')
            if not file_name.endswith(end_rule):
                raise BaseAppException("文件类型错误, 请上传正确格式!")

    def file_receiving(self):
        """接收文件"""
        upload_file = b""
        for chunk in self.file_obj.chunks():
            upload_file += chunk
        return upload_file

    def py_file_check(self):
        """py文件检查"""
        self._check_file_name(end_rule="py")

    def image_file_check(self):
        self._check_mime_type(["image/png", "image/jpeg"])
        self._check_file_name(end_rule=("jpg", "jpeg", "png", "svg"))
