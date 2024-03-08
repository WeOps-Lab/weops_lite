from django.urls import include, path
from rest_framework import routers

from apps.system_mgmt.views.group_manage import KeycloakGroupViewSet
from apps.system_mgmt.views.log_entry_viewset import LogEntryViewSet
from apps.system_mgmt.views.login_info import LoginInfoView
from apps.system_mgmt.views.logo import LogoViewSet
from apps.system_mgmt.views.menu_manage import MenuManageModelViewSet
from apps.system_mgmt.views.operation_log import OperationLogViewSet, CustomOperationLogViewSet
from apps.system_mgmt.views.role_manage import KeycloakRoleViewSet
from apps.system_mgmt.views.user_manage import KeycloakUserViewSet

# 创建路由分组
api_router = routers.DefaultRouter()
api_router.register(r"audit_log", LogEntryViewSet, basename="audit_log")
api_router.register(r"group", KeycloakGroupViewSet, basename="group")
api_router.register(r"user", KeycloakUserViewSet, basename="user")
api_router.register(r"role", KeycloakRoleViewSet, basename="role")
api_router.register(r"menu", MenuManageModelViewSet, basename="menu")
api_router.register(r"operation_log", OperationLogViewSet, basename="operation_log")
api_router.register(r"operation_log/custom", CustomOperationLogViewSet, basename="operation_log_custom")

logo_router = routers.DefaultRouter()
logo_router.register(r"", LogoViewSet, basename="logo")

urlpatterns = [
    path(r"api/", include(api_router.urls)),
    path(r"api/logo/", include(logo_router.urls)),
    path(r"api/logo/reset/", LogoViewSet.as_view({"post": "reset"})),
    path(r"api/login_info/", LoginInfoView.as_view()),
]