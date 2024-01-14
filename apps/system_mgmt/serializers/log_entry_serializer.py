from rest_framework import serializers
from auditlog.models import LogEntry


class LogEntrySerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()

    class Meta:
        model = LogEntry
        fields = '__all__'
