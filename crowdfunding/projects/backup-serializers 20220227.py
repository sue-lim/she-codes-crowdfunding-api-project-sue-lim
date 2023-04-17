from django.contrib.auth.models import User
from .models import Project, Pledge, Comment, Category, Favourite
from rest_framework import serializers
from users.serializers import CustomUserSerializer


'''Comments Serializer / Form'''


class CommentSerializer(serializers.ModelSerializer):
    commentator = serializers.ReadOnlyField(source='commentator.username')
    project = serializers.SlugRelatedField(
        queryset=Project.objects.all(), slug_field="title")

    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ['id', 'project', 'title', 'content', 'author']
        # read_only_fields = ['id']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance


'''Pledge Serializer / Form'''


class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.username')
    project = serializers.SlugRelatedField(
        queryset=Project.objects.all(), slug_field="title")

    class Meta:
        model = Pledge
        fields = '__all__'
        '''THIS LINE __all__ replaces the needs in the model.serializer to dd the fields seperately'''

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance


class PledgeDetailSerializer(serializers.ModelSerializer):
    # project = serializers.SlugRelatedField(
    #     queryset=Project.objects.all(), slug_field="title")
    class Meta:
        model = Pledge
        fields = '__all__'
        read_only_fields = ["id", "supporter", "amount", "project"]


class ProjectSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    image = serializers.URLField()
    # is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.username')
    goal = serializers.IntegerField()
    sum_pledges = serializers.ReadOnlyField()
    goal_balance = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = '__all__'

    # def create(self, validated_data):
    #     return Project.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.save()
    #     return instance

    # def create(self, validated_data):
    #     return Project.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get(
    #         'description', instance.description)
    #     instance.goal = validated_data.get('goal', instance.goal)
    #     instance.image = validated_data.get('image', instance.image)
    #     instance.is_open = validated_data.get('is_open', instance.is_open)
    #     instance.date_created = validated_data.get(
    #         'date_created', instance.date_created)
    #     instance.owner = validated_data.get('owner', instance.owner)
    #     instance.save()
    #     return instance


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    liked_by = CustomUserSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


'''Category Serializer'''


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'name'


class CategoryDetailSerializer(CategorySerializer):
    category_projects = ProjectSerializer(many=True, read_only=True)
