from django.urls import path
from rest_framework import routers

from apps.system_mgmt.views.group_manage import KeycloakGroupViewSet
from apps.system_mgmt.views.log_entry_viewset import LogEntryViewSet
from apps.system_mgmt.views.login_info import LoginInfoView
from apps.system_mgmt.views.logo import LogoViewSet
from apps.system_mgmt.views.menu_manage import MenuManageModelViewSet

from apps.system_mgmt.views.operation_log import OperationLogViewSet, CustomOperationLogViewSet
from apps.system_mgmt.views.role_manage import KeycloakRoleViewSet
from apps.system_mgmt.views.user_manage import KeycloakUserViewSet


router = routers.DefaultRouter()
router.register(r"api/audit_log", LogEntryViewSet, basename="audit_log")

router.register(r"api/group", KeycloakGroupViewSet, basename="group")
router.register(r"api/user", KeycloakUserViewSet, basename="user")
router.register(r"api/role", KeycloakRoleViewSet, basename="role")

router.register(r"api/menu", MenuManageModelViewSet, basename="menu")
router.register(r"api/operation_log", OperationLogViewSet, basename="operation_log")
router.register(r"api/operation_log/custom", CustomOperationLogViewSet, basename="operation_log_custom")

urlpatterns = router.urls

urlpatterns += [
    path(r"api/logo/", LogoViewSet.as_view({"get": "retrieve", "put": "update"})),
    path(r"api/logo/reset/", LogoViewSet.as_view({"post": "reset"})),
    path(r"api/login_info/", LoginInfoView.as_view()),
]
