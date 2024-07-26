from rest_framework import routers

from apps.node_mgmt.views.node import NodeViewSet

router = routers.DefaultRouter()
router.register(r"api/node", NodeViewSet, basename="node")

urlpatterns = router.urls
