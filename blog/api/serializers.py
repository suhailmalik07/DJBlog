"""Serializers for Blog App"""
from rest_framework import serializers
from blog.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    """Post Serializer with Meta class"""
    class Meta:
        model = Post
        fields = ["id", "title", "content", "date_posted", "author"]
        read_only_fields = ['author']
