from rest_framework import serializers


__all__ = (
    'SimpleResponseSuccessSchemas',
    'SimpleResponseErrorSchemas',
)

class SimpleResponseSuccessSchemas(serializers.Serializer):
    success = serializers.BooleanField(default=True)
    msg = serializers.CharField()


class SimpleResponseErrorSchemas(serializers.Serializer):
    success = serializers.BooleanField(default=False)
    msg = serializers.CharField()