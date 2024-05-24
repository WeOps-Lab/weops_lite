from rest_framework import serializers

from apps.cmdb_mgmt.models.Instance_permission import InstancePermission, UserInstancePermission


class RoleInstancePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstancePermission
        fields = (
            'id',
            'created_at',
            'role_id',
            'model_id',
            'permission_type',
            'resource_type',
            'conditions',
        )
        read_only_fields = ('id', 'created_at')


class UserInstancePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInstancePermission
        fields = (
            'id',
            'created_at',
            'username',
            'model_id',
            'permission_type',
            'resource_type',
            'conditions',
        )
        read_only_fields = ('id', 'created_at')
