from django.contrib import admin

from apps.system_mgmt.models import OperationLog, SysSetting, MenuManage


@admin.register(OperationLog)
class OperationLogAdmin(admin.ModelAdmin):
    list_display = ('operator', 'operate_type', 'operate_obj', 'app_module', 'obj_type')
    search_fields = ('operator', 'operate_type')


@admin.register(SysSetting)
class SysSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'desc')
    search_fields = ('key', 'desc')


@admin.register(MenuManage)
class MenuManageAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'default', 'use')
    search_fields = ('menu_name',)
