from django_filters import rest_framework as filters

from apps.node_mgmt.models.node import Node


class NodeFilter(filters.FilterSet):
    model_id = filters.CharFilter(field_name='model_id', lookup_expr='exact')
    sidecar_status = filters.CharFilter(field_name='sidecar_status', lookup_expr='exact')
    node_name = filters.CharFilter(field_name='node_name', lookup_expr='icontains')
    node_ip = filters.CharFilter(field_name='node_name', lookup_expr='icontains')
    os_type = filters.CharFilter(field_name='os_type', lookup_expr='exact')

    class Meta:
        model = Node
        fields = ['sidecar_status', 'model_id', 'node_name', 'node_ip', 'os_type']
