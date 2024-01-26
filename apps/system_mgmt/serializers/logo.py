import base64

from django.db import transaction
from rest_framework import serializers
from rest_framework.fields import empty
from rest_framework.serializers import ModelSerializer

from apps.system_mgmt.models.syssetting import SysSetting
from apps.system_mgmt.utils.upload_file import UploadFileUtils


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

