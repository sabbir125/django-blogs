from email.mime import image
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import My_blogs


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=20, min_length=6)
    username = serializers.CharField(max_length=20, min_length=4)
    password = serializers.CharField(max_length=100, min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]
        # print(fields)


    def validate(self, data):
        email = data.get("email", None)
        username = data.get("username", None)

        print(email)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "email already exists"})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "username already exists"})

        return super().validate(data)

    def create(self, validated_data):
        # print(**validated_data)
        return User.objects.create_user(**validated_data)


class MY_BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = My_blogs
        exclude  =["id"] 