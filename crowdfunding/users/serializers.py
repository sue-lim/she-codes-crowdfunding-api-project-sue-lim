from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


# Serializer to Get User Details using Django Token Authentication
class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField(required=True,
                                   validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'password2']
        extra_kwargs = {'first_name': {'required': True},
                        'last_name': {'required': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Your password fields didn't match."})
        return attrs


class CustomUserDetailSerializer(CustomUserSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined','password', 'password2']
        read_only_fields =['id','last_login', 'date_joined']
        extra_kwargs = {'first_name': {'required': True},
                        'last_name': {'required': True}}


# Serializer to Register User
# class CustomUserRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser


class CustomUserChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['old_password', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Your password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        if password := validated_data.get('password'):
            instance.set_password(password)
        instance.save()

        return instance
###################################################################################################

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#         read_only_fields = ['id']


# class CustomUserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     username = serializers.CharField(max_length=200)
#     email = serializers.EmailField()
#     password = serializers.CharField(min_length=8, write_only=True)

#     # def create(self, validated_data):
#     #     return CustomUser.objects.create(**validated_data)

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         user = CustomUser(**validated_data)
#         user.set_password(password)
#         user.save()
#         return user.objects.update(**validated_data)

        # def create(self, validated_data):
        #     return CustomUser.objects.update(**validated_data)

#############################
# Questions
# 1 hashing password
# 2 updating passwords
