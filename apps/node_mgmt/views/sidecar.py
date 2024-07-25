from django.conf import settings
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.web_utils import WebUtils
from apps.node_mgmt.services.sidecar import Sidecar
from common.download_loocal_file import download_local_file
from common.open_base import OpenAPIViewSet


class SidecarViewSet(ViewSet):
    @swagger_auto_schema(
        operation_id="sidecar_install_steps",
        operation_description="获取sidecar的安装步骤",
        manual_parameters=[
            openapi.Parameter("id", openapi.IN_PATH, description="节点ID", type=openapi.TYPE_INTEGER)
        ],
    )
    @uma_permission('sidecar_install_steps')
    @action(detail=False, methods=["get"], url_path="install_steps/(?P<id>.+?)")
    def install_steps(self, request, id):
        result = Sidecar(id=int(id)).get_installation_steps()
        return WebUtils.response_success(result)


class OpenSidecarViewSet(OpenAPIViewSet):
    @swagger_auto_schema(
        operation_id="download_sidecar_file",
        operation_description="获取sidecar的安装包文件",
        manual_parameters=[
            openapi.Parameter("file_name", openapi.IN_PATH, description="sidecar文件名称", type=openapi.TYPE_STRING)
        ],
    )
    @action(detail=False, methods=["get"], url_path="download_file/(?P<file_name>.+?)")
    def download_sidecar_file(self, request, file_name):
        # 获取文件目录
        local_path = settings.CURRENT_FILE_PATH.rstrip("/") + "/sidecar/installation_package/"
        return download_local_file(local_path, file_name)
