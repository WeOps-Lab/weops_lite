from django.urls import include, path
from rest_framework import routers

from apps.system_mgmt.views.log_entry_viewset import LogEntryViewSet
from apps.system_mgmt.views.user_manage import KeycloakGroupViewSet, KeycloakUserViewSet, KeycloakRoleViewSet

router = routers.DefaultRouter()
router.register(r"audit_log", LogEntryViewSet, basename="audit_log")
router.register(r"group", KeycloakGroupViewSet, basename="group")
router.register(r"user", KeycloakUserViewSet, basename="user")
router.register(r"role", KeycloakRoleViewSet, basename="role")
urlpatterns = [path("api/", include(router.urls)), ]
