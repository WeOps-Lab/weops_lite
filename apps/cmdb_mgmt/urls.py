from rest_framework import routers

from apps.cmdb_mgmt.views.classfication import ClassificationViewSet
from apps.cmdb_mgmt.views.model import ModelViewSet

router = routers.DefaultRouter()
router.register(r"api/classification", ClassificationViewSet, basename="classification")
router.register(r"api/model", ModelViewSet, basename="model")

urlpatterns = router.urls
