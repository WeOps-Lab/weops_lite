from django.urls import include, path
from rest_framework import routers

from apps.system_mgmt.views import LogEntryViewSet

router = routers.DefaultRouter()
router.register(r'auditlogs', LogEntryViewSet)
urlpatterns = [path('api/', include(router.urls)), ]
