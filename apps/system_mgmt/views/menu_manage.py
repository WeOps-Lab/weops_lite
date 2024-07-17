from django.db import transaction
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.drf_utils import CustomPageNumberPagination
from apps.core.utils.web_utils import WebUtils
from apps.system_mgmt.constants import APP_MODULE, MENU
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
    pagination_class = CustomPageNumberPagination
    search_fields = ['menu_name']

    @swagger_auto_schema(operation_id="menu_list", operation_description="菜单列表")
    @uma_permission("menu_list")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_id="menu_retrieve", operation_description="查询某个菜单")
    @uma_permission("menu_retrieve")
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return WebUtils.response_success(serializer.data)

    @swagger_auto_schema(operation_id="menu_create", operation_description="菜单创建")
    @uma_permission("menu_create")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = serializer.instance
        OperationLog.objects.create(
            operator=request.userinfo.get("username"),
            operate_type=OperationLog.ADD,
            operate_obj=instance.menu_name,
            operate_summary="自定义菜单管理新增自定义菜单:[{}]".format(instance.menu_name),
            app_module=APP_MODULE,
            obj_type=MENU,
        )
        return WebUtils.response_success(serializer.data)

    @swagger_auto_schema(operation_id="menu_update", operation_description="菜单更新")
    @uma_permission("menu_update")
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.default:
            return WebUtils.response_error(error_message="默认菜单不允许修改！", status=500)

        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        OperationLog.objects.create(
            operator=request.userinfo.get("username"),
            operate_type=OperationLog.MODIFY,
            operate_obj=instance.menu_name,
            operate_summary="自定义菜单管理修改自定义菜单:[{}]".format(instance.menu_name),
            app_module=APP_MODULE,
            obj_type=MENU,
        )
        return WebUtils.response_success(serializer.data)

    @swagger_auto_schema(operation_id="menu_partial_update", operation_description="菜单更新（部分属性）")
    @uma_permission("menu_partial_update")
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.default:
            return WebUtils.response_error(error_message="默认菜单不允许修改！", status=500)

        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        OperationLog.objects.create(
            operator=request.userinfo.get("username"),
            operate_type=OperationLog.MODIFY,
            operate_obj=instance.menu_name,
            operate_summary="自定义菜单管理修改自定义菜单:[{}]".format(instance.menu_name),
            app_module=APP_MODULE,
            obj_type=MENU,
        )
        return WebUtils.response_success(serializer.data)

    @swagger_auto_schema(operation_id="menu_delete", operation_description="菜单删除")
    @uma_permission("menu_delete")
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.use:
            return WebUtils.response_error(error_message="已启用的菜单不允许删除！", status=500)

        if instance.default:
            return WebUtils.response_error(error_message="默认菜单不允许删除！", status=500)

        instance.delete()
        OperationLog.objects.create(
            operator=request.userinfo.get("username"),
            operate_type=OperationLog.DELETE,
            operate_obj=instance.menu_name,
            operate_summary="自定义菜单管理删除自定义菜单:[{}]".format(instance.menu_name),
            app_module=APP_MODULE,
            obj_type=MENU,
        )
        return WebUtils.response_success()

    @swagger_auto_schema(operation_id="menu_use", operation_description="菜单启用")
    @uma_permission("menu_use")
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
            operator=request.userinfo.get("username"),
            operate_type=OperationLog.MODIFY,
            operate_obj=instance.menu_name,
            operate_summary="自定义菜单管理启用自定义菜单:[{}]".format(instance.menu_name),
            app_module=APP_MODULE,
            obj_type=MENU,
        )
        return WebUtils.response_success()

    @swagger_auto_schema(operation_id="get_menu_use", operation_description="查询启用的菜单")
    # @uma_permission("get_menu_use")
    @action(methods=["GET"], detail=False)
    def get_use_menu(self, request, *args, **kwargs):
        instance = self.queryset.get(use=True)
        return WebUtils.response_success(instance.menu)
