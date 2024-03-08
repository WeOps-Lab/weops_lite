from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets


class SidecarAgentApiViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_id="server_info",
        operation_description="获取服务器信息"
    )
    @csrf_exempt
    def list(self, request):
        return JsonResponse({
            'cluster_id': '',
            'node_id': '',
            'version': '5.0.0'
        })
