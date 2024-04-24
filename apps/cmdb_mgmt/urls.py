from rest_framework import routers

from apps.cmdb_mgmt.views.change_record import ChangeRecordViewSet
from apps.cmdb_mgmt.views.classfication import ClassificationViewSet
from apps.cmdb_mgmt.views.instance import InstanceViewSet
from apps.cmdb_mgmt.views.model import ModelViewSet

router = routers.DefaultRouter()
router.register(r"api/classification", ClassificationViewSet, basename="classification")
router.register(r"api/model", ModelViewSet, basename="model")
router.register(r"api/instance", InstanceViewSet, basename="instance")
router.register(r"api/change_record", ChangeRecordViewSet, basename="change_record")


urlpatterns = router.urls
