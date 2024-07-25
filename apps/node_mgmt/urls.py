from rest_framework import routers

from apps.node_mgmt.views.node import NodeViewSet
from apps.node_mgmt.views.sidecar import SidecarViewSet, OpenSidecarViewSet

router = routers.DefaultRouter()
router.register(r"api/node", NodeViewSet, basename="node")
router.register(r"api/sidecar", SidecarViewSet, basename="sidecar")
router.register(r"openapi/sidecar", OpenSidecarViewSet, basename="open_sidecar")

urlpatterns = router.urls
