from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator

from .models import CustomNewUser


User = get_user_model()

User  = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the custom user model used by the `accounts` app."""

    class Meta:
        model = User
        fields = ["id", "email", "username", "first_name", "last_name", "start_date"]


class SignupSerializer(serializers.ModelSerializer):
    """Handles registration and ensures passwords match."""

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "password2"]

        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=["email", "username"],
                message="email or username already exists",
            )
        ]
    def validate(self, data):
        # print(data)
        passwrd = data.get("password") 
        passwr2 = data.get("password2") 

        if passwrd != passwr2:
            raise(serializers.ValidationError({"Failed":f"Password must be same"}))
        
        return data


    def create(self, validated_data):
        user = self.Meta.model(
        email=validated_data['email'],
        username=validated_data['username'],
            )
        user.set_password(validated_data['password'])
        user.save()
        return user 

        


