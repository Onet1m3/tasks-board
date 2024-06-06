from django.contrib.auth.models import User
from rest_framework import serializers


__all__ = (
    'UserSignUpSerializer',
)


class UserSignUpSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            "password",
            "username"
        ]

    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
