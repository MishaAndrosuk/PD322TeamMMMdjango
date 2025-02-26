from .models import CustomUser
from rest_framework import serializers
import uuid
from django.utils.timezone import now
import os
from django.conf import settings

from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar', 'role']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.avatar:
            representation['avatar'] = f"{settings.MEDIA_URL}{instance.avatar}"
        return representation



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    role = serializers.CharField(required=False, default="student")

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name', 'role']

    def validate_role(self, value):
        value = value.lower()
        if value not in CustomUser.ROLES:
            raise serializers.ValidationError("Invalid role")
        return value

    def create(self, validated_data):
        email = validated_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email already exists."})

        password = validated_data.pop('password')
        role_input = validated_data.pop("role", "student")
        validated_data["role"] = CustomUser.ROLES.get(role_input, "Student")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user



class AvatarUpdateSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=True)

    class Meta:
        model = CustomUser
        fields = ['avatar']

    def update(self, instance, validated_data):
        if instance.avatar:
            old_avatar_path = instance.avatar.path
            if os.path.exists(old_avatar_path):
                try:
                    os.remove(old_avatar_path)
                except Exception as e:
                    raise serializers.ValidationError(f"Failed to delete the old avatar: {str(e)}")


        new_avatar = validated_data.get('avatar')

        extension = new_avatar.name.split('.')[-1]
        unique_filename = f"{uuid.uuid4().hex}_{int(now().timestamp())}.{extension}"

        new_avatar.name = unique_filename
        instance.avatar = new_avatar

        instance.save()
        return instance



class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']

    def update(self, instance, validated_data):

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)


        password = validated_data.get('password')
        if password:
            instance.password = make_password(password)

        instance.save()
        return instance

