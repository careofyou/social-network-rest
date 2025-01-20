from rest_framework import serializers
from .models import Profile, Category, Post, Comment
from django.contrib.auth.models import User

class UserSerizalizer(serializers.ModelSerializer):
    # user model serializer
    
    class Meta:
        model = User
        fields = ('id', 'username')

class ProfileSerializer(serializers.ModelSerializer):
    # user profile model serializer
    user = UserSerizalizer(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'info')

class CommentSerializer(serializers.ModelSerializer):
    # comment model serializer 
    author = UserSerizalizer(read_only=True)

    class Meta:
        model = Comment 
        fields = ('id', 'author', 'text', 'created')

class PostSerializer(serializers.ModelSerializer):
    # post model serializer
    author = UserSerizalizer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    likes_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'category', 'published', 'updated', 'comments', 'likes_count')

    def get_likes_count(self, obj):
        return obj.likes.count()

class CategorySerializer(serializers.ModelSerializer):
    # cat serializer
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'posts')
    