from rest_framework import serializers
from .models import Project, Pledge, Comment, User
from users.serializers import CustomUserSerializer
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'project', 'title', 'content', 'author']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    content = serializers.CharField
    # author = serializers.ReadOnlyField(source='owner.id')

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get(
            'content', instance.content)

        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance


class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment',
                  'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField('%a, %d %b %Y %H:%M %Z')
    # '%a, %d %b %Y %H:%M %p %Z' -> "Fri, 20 Mar 2020 14:28 PM UTC"

    comments = CommentSerializer(many=True)
    owner_id = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')
    total = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get(
            'date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    liked_by = CustomUserSerializer(many=True, read_only=True)
