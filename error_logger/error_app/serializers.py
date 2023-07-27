from rest_framework import serializers

from error_app.models import ErrorLog


class ErrorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorLog
        fields = "__all__"
