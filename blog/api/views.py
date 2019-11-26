"""API Views"""
from rest_framework.viewsets import ModelViewSet
from blog.models import Post
from .serializers import PostModelSerializer
from rest_framework import permissions


class PostModelViewSet(ModelViewSet):
    """Post model CRUD Views"""
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer_class):
        serializer_class.save(author=self.request.user)
