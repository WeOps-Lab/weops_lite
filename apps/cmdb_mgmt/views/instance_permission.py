from rest_framework import viewsets

from apps.cmdb_mgmt.filters.instance_permission import RoleInstancePermissionFilter, UserInstancePermissionFilter
from apps.cmdb_mgmt.models.Instance_permission import InstancePermission, UserInstancePermission
from apps.cmdb_mgmt.serializers.instance_permission import RoleInstancePermissionSerializer, \
    UserInstancePermissionSerializer
from apps.core.decorators.uma_permission import uma_permission
from apps.core.utils.drf_utils import CustomPageNumberPagination
from apps.core.utils.web_utils import WebUtils


class RoleInstancePermissionViewSet(viewsets.ModelViewSet):
    queryset = InstancePermission.objects.all().order_by("-created_at")
    serializer_class = RoleInstancePermissionSerializer
    filterset_class = RoleInstancePermissionFilter
    pagination_class = CustomPageNumberPagination

    @uma_permission('r_permission_create')
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return WebUtils.response_success(serializer.data)

    @uma_permission('r_permission_list')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @uma_permission('r_permission_del')
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return WebUtils.response_success()

    @uma_permission('r_permission_detail')
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return WebUtils.response_success(serializer.data)

    @uma_permission('r_permission_update')
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return WebUtils.response_success(serializer.data)


class UserInstancePermissionViewSet(viewsets.ModelViewSet):
    queryset = UserInstancePermission.objects.all().order_by("-created_at")
    serializer_class = UserInstancePermissionSerializer
    filterset_class = UserInstancePermissionFilter
    pagination_class = CustomPageNumberPagination
