from .models import User, Profile
from rest_framework import serializers

class RegisterSerializers(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'last_name', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            username=validated_data['username'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'