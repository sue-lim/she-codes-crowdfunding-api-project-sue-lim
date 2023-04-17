from django.contrib.auth.models import User
from .models import Project, Pledge, Comment, Category, Favourite
from rest_framework import serializers
from users.serializers import CustomUserSerializer

'''Serializer / Forms'''


class CommentSerializer(serializers.ModelSerializer):
    commentator = serializers.ReadOnlyField(source='commentator.username')
    # project = serializers.SlugRelatedField(
    #     queryset=Project.objects.all(), slug_field="title")

    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ['id', 'project', 'title', 'content', 'author']
        # read_only_fields = ['id']

    def get_commentator(self, obj):
        if obj.anonymous:
            return None
        else:
            return obj.commentator.username
        
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
    
class CommentDetailSerializer(serializers.ModelSerializer):
        # project = serializers.SlugRelatedField(
    #     queryset=Project.objects.all(), slug_field="title")

    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ['id', 'project', 'title', 'content', 'commentator']
        read_only_fields = ['id','commentator']


class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.username')
    # project = serializers.SlugRelatedField(
    #     queryset=Project.objects.all(), slug_field="title")

    class Meta:
        model = Pledge
        # fields = ['id', 'amount', 'comment','anonymous', 'project', 'supporter']
        # read_only_fields = ['id', 'supporter']
        fields = '__all__'
        '''THIS LINE __all__ replaces the needs in the model.serializer to dd the fields seperately'''

    def get_supporter(self, obj):
        if obj.anonymous:
            return None
        else:
            return obj.supporter.username

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
        # fields = ["id", "amount", "comment", "anonymous",
        #           "project", "supporter", "date_pledged"]
        read_only_fields = ["id", "supporter", "amount", "project"]


class ProjectSerializer(serializers.ModelSerializer):
    goal = serializers.IntegerField()
    sum_pledges = serializers.ReadOnlyField()
    goal_balance = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    # comments = CommentSerializer(many=True)
    # owner_id = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')
    total = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = '__all__'


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    liked_by = CustomUserSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['title', 'description','goal','image','is_open','liked_by']
        read_only_fields = ['id', 'owner']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'name'


class CategoryDetailSerializer(CategorySerializer):
    category_projects = ProjectSerializer(many=True, read_only=True)
