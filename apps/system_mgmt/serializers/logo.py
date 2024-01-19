import base64

from django.db import transaction
from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.serializers import ModelSerializer

from apps.system_mgmt.models.syssetting import SysSetting


class LogSerializer(ModelSerializer):
    file = serializers.ImageField(max_length=None, allow_null=True, required=False, write_only=True)

    class Meta:
        model = SysSetting
        fields = ("key", "value", "file")
        extra_kwargs = {"key": {"read_only": True}, "value": {"read_only": True}}

    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)
        self.img_base64 = ""

    def validate_file(self, file_obj):
        UploadFileUtils(file_obj).image_file_check()
        self.img_base64 = base64.b64encode(file_obj.read()).decode("utf8")
        return file_obj

    @transaction.atomic
    def update(self, instance, validated_data):
        validated_data["value"] = self.img_base64
        validated_data.pop("file")
        return super().update(instance, validated_data)


class UploadFileUtils:
    def __init__(self, file_obj):
        if not file_obj:
            raise Exception("文件不存在，请添加文件!")
        self.file_obj = file_obj

    def _check_mime_type(self, correct_mime_type):
        # 限制文件MIME Type
        if self.file_obj.content_type not in correct_mime_type:
            raise Exception("文件类型错误, 请上传正确格式!")

    def _check_file_name(self, end_rule=None):
        # 限制文件后缀
        if end_rule:
            file_name = self.file_obj.name.strip('"')
            if not file_name.endswith(end_rule):
                raise Exception("文件类型错误, 请上传正确格式!")

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
