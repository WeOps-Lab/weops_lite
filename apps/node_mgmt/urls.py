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

urlpatterns = router.urls

urlpatterns += [
]
