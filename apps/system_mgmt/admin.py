from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from apps.system_mgmt.models import OperationLog, SysSetting, MenuManage


@admin.register(OperationLog)
class OperationLogAdmin(ImportExportModelAdmin):
    list_display = ('operator', 'operate_type', 'operate_obj', 'app_module', 'obj_type')
    search_fields = ('operator', 'operate_type')


@admin.register(SysSetting)
class SysSettingAdmin(ImportExportModelAdmin):
    list_display = ('key', 'value', 'desc')
    search_fields = ('key', 'desc')


@admin.register(MenuManage)
class MenuManageAdmin(ImportExportModelAdmin):
    list_display = ('menu_name', 'default', 'use')
    search_fields = ('menu_name',)
