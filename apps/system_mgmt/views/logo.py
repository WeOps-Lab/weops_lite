from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.core.decorators.uma_permission import uma_permission
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

    @uma_permission('SysSetting_logo_change')
    def update(self, request, *args, **kwargs):
        file_obj = request.FILES.get("file", "")
        instance = self.get_object()
        data = request.data
        data["file"] = file_obj
        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        current_ip = getattr(request, "current_ip", "127.0.0.1")
        OperationLog.objects.create(
            operator=request.user.get('username', None),
            operate_type=OperationLog.MODIFY,
            operate_obj="Logo设置",
            operate_summary="修改Logo为:[{}]".format(file_obj.name if file_obj else ""),
            current_ip=current_ip,
            app_module="系统管理",
            obj_type="系统设置",
        )
        return Response(serializer.data)

    @uma_permission('SysSetting_logo_change')
    def reset(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.value = SYSTEM_LOGO_INFO["value"]
        instance.save()
        serializer = self.get_serializer(instance)
        current_ip = getattr(request, "current_ip", "127.0.0.1")
        OperationLog.objects.create(
            operator=request.user.get('username', None),
            operate_type=OperationLog.MODIFY,
            operate_obj="Logo设置",
            operate_summary="logo恢复默认",
            current_ip=current_ip,
            app_module="系统管理",
            obj_type="系统设置",
        )
        return Response(serializer.data)
