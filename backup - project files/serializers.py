from django.contrib.auth.models import User
from .models import Project, Pledge, Comment, Category, Favourite
from rest_framework import serializers
from users.serializers import CustomUserSerializer

'''Serializer / Forms'''


class CommentSerializer(serializers.ModelSerializer):
    commentator = serializers.ReadOnlyField(source='commentator.username')
    project = serializers.SlugRelatedField(
        queryset=Project.objects.all(), slug_field="title")

    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ['id', 'project', 'title', 'content', 'author']
        # read_only_fields = ['id']


class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.username')

    class Meta:
        model = Pledge
        fields = '__all__'

        '''THIS LINE __all__ replaces the needs in the model.serializer to dd the fields seperately'''


class PledgeDetailSerializer(PledgeSerializer):
    project = serializers.CharField(source='project.title')

    class Meta:
        model = Pledge
        fields = '__all__'


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


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    liked_by = CustomUserSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'name'


class CategoryDetailSerializer(CategorySerializer):
    category_projects = ProjectSerializer(many=True, read_only=True)
