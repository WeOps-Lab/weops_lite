from rest_framework import serializers

from apps.node_mgmt.models.node import Node


class NodeSerializer(serializers.ModelSerializer):
    sidecar_status = serializers.CharField(read_only=True)
    node_ip = serializers.CharField(allow_blank=True)

    class Meta:
        model = Node
        fields = ['id', 'model_id', 'node_id', 'node_name', 'node_ip', 'os_type', 'sidecar_status']
