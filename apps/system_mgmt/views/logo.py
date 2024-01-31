from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.web_utils import WebUtils
from apps.system_mgmt.constants import SYSTEM_LOGO_INFO
from apps.system_mgmt.models.operation_log import OperationLog
from apps.system_mgmt.models.syssetting import SysSetting
from apps.system_mgmt.serializers.logo import LogSerializer


class LogoViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = SysSetting.objects.all()
    serializer_class = LogSerializer

    def get_object(self):
        obj, created = self.get_queryset().get_or_create(
            key=SYSTEM_LOGO_INFO["key"],
            defaults=SYSTEM_LOGO_INFO,
        )
        return obj

    @swagger_auto_schema(
        operation_id="logo",
        operation_description="获取logo",
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return WebUtils.response_success(serializer.data)

    @swagger_auto_schema(
        operation_id="logo_update",
        operation_description="更新logo",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'file': openapi.Schema(type=openapi.TYPE_FILE, description="logo文件", format='binary'),
            },
            required=['file'],
        )
    )
    @uma_permission('logo_update')
    def update(self, request, *args, **kwargs):
        file_obj = request.FILES.get("file", "")
        instance = self.get_object()
        data = request.data
        data["file"] = file_obj
        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        OperationLog.objects.create(
            operator=request.userinfo.get("username"),
            operate_type=OperationLog.MODIFY,
            operate_obj="Logo设置",
            operate_summary="修改Logo为:[{}]".format(file_obj.name if file_obj else ""),
            app_module="系统管理",
            obj_type="系统设置",
        )
        return WebUtils.response_success(serializer.data)

    @swagger_auto_schema(
        operation_id="logo_reset",
        operation_description="重置为默认logo",
    )
    @uma_permission('logo_reset')
    def reset(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.value = SYSTEM_LOGO_INFO["value"]
        instance.save()
        serializer = self.get_serializer(instance)
        OperationLog.objects.create(
            operator=request.userinfo.get("username"),
            operate_type=OperationLog.MODIFY,
            operate_obj="Logo设置",
            operate_summary="logo恢复默认",
            app_module="系统管理",
            obj_type="系统设置",
        )
        return WebUtils.response_success(serializer.data)
