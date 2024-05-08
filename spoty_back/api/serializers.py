from rest_framework import serializers

from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        
    def create(self, validated_data):
        return User.objects.create_superuser(**validated_data)