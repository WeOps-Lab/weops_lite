from django.db import transaction

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.system_mgmt.filters.menu_manage import MenuManageFilter
from apps.system_mgmt.models import MenuManage
from apps.system_mgmt.models.operation_log import OperationLog
from apps.system_mgmt.serializers.menu_manage import MenuManageModelSerializer


class MenuManageModelViewSet(ModelViewSet):
    """
    自定义菜单管理
    """

    queryset = MenuManage.objects.all()
    serializer_class = MenuManageModelSerializer
    ordering = ["created_at"]
    ordering_fields = ["created_at"]
    filter_class = MenuManageFilter

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.default:
            return Response(data={"success": False, "detail": "默认菜单不允许修改！"}, status=500)

        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        OperationLog.objects.create(
            operator=request.user.get('username', None),
            operate_type=OperationLog.MODIFY,
            operate_obj=instance.menu_name,
            operate_summary="自定义菜单管理修改自定义菜单:[{}]".format(instance.menu_name),
            current_ip=getattr(request, "current_ip", "127.0.0.1"),
            app_module="系统管理",
            obj_type="自定义菜单管理",
        )
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        return super(MenuManageModelViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = serializer.instance
        OperationLog.objects.create(
            operator=request.user.get('username', None),
            operate_type=OperationLog.ADD,
            operate_obj=instance.menu_name,
            operate_summary="自定义菜单管理新增自定义菜单:[{}]".format(instance.menu_name),
            current_ip=getattr(request, "current_ip", "127.0.0.1"),
            app_module="系统管理",
            obj_type="自定义菜单管理",
        )
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.use:
            return Response(data={"success": False, "detail": "已启用的菜单不允许删除！"}, status=500)

        if instance.default:
            return Response(data={"success": False, "detail": "默认菜单不允许删除！"}, status=500)

        instance.delete()
        OperationLog.objects.create(
            operator=request.user.get('username', None),
            operate_type=OperationLog.DELETE,
            operate_obj=instance.menu_name,
            operate_summary="自定义菜单管理删除自定义菜单:[{}]".format(instance.menu_name),
            current_ip=getattr(request, "current_ip", "127.0.0.1"),
            app_module="系统管理",
            obj_type="自定义菜单管理",
        )
        return Response(data={"success": True})

    @transaction.atomic
    @action(methods=["PATCH"], detail=True)
    def use_menu(self, request, *args, **kwargs):
        """
        关闭启用的
        设置此对象为启用
        """
        instance = self.get_object()
        self.queryset.update(use=False)
        instance.use = True
        instance.save()
        OperationLog.objects.create(
            operator=request.user.get('username', None),
            operate_type=OperationLog.MODIFY,
            operate_obj=instance.menu_name,
            operate_summary="自定义菜单管理启用自定义菜单:[{}]".format(instance.menu_name),
            current_ip=getattr(request, "current_ip", "127.0.0.1"),
            app_module="系统管理",
            obj_type="自定义菜单管理",
        )
        return Response(data={"success": True})

    @action(methods=["GET"], detail=False)
    def get_use_menu(self, request, *args, **kwargs):
        instance = self.queryset.get(use=True)
        return Response(instance.menu)
