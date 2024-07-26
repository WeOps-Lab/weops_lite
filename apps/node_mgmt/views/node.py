from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.drf_utils import CustomPageNumberPagination
from apps.core.utils.web_utils import WebUtils
from apps.node_mgmt.constants import SIDECAR_STATUS_ENUM
from apps.node_mgmt.filters.node import NodeFilter
from apps.node_mgmt.models.node import Node
from apps.node_mgmt.serializers.node import NodeSerializer


class NodeViewSet(mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Node.objects.all().order_by("-created_at")
    serializer_class = NodeSerializer
    filterset_class = NodeFilter
    pagination_class = CustomPageNumberPagination

    @swagger_auto_schema(
        operation_id="node_list",
        operation_description="节点列表",
    )
    @uma_permission('node_list')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="node_batch_create",
        operation_description="批量创建节点",
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "model_id": openapi.Schema(type=openapi.TYPE_STRING, description="模型ID"),
                    "node_id": openapi.Schema(type=openapi.TYPE_NUMBER, description="节点ID"),
                    "node_name": openapi.Schema(type=openapi.TYPE_STRING, description="节点名称"),
                    "node_ip": openapi.Schema(type=openapi.TYPE_STRING, description="节点IP"),
                },
                required=["model_id", "node_id", "node_name", "node_ip"],
            )
        ),
    )
    @action(methods=["post"], detail=False, url_path=r"batch_create")
    @uma_permission('node_batch_create')
    def batch_create(self, request, *args, **kwargs):
        for data in request.data:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="node_del",
        operation_description="删除节点",
    )
    @uma_permission('node_del')
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return WebUtils.response_success()

    @swagger_auto_schema(
        operation_id="node_enum",
        operation_description="节点管理的枚举值",
    )
    @uma_permission('node_enum')
    @action(methods=["get"], detail=False, url_path=r"enum")
    def enum(self, request, *args, **kwargs):
        return WebUtils.response_success(dict(sidecar_status=SIDECAR_STATUS_ENUM))
