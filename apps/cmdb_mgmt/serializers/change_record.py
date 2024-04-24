from rest_framework import serializers

from apps.cmdb_mgmt.models.change_record import ChangeRecord


class ChangeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeRecord
        fields = (
            'id',
            'inst_id',
            'model_id',
            'label',
            'type',
            'before_data',
            'after_data',
            'operator',
            'created_at',
        )
        read_only_fields = ('id', 'created_at')

