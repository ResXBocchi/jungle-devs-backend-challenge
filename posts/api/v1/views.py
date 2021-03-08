from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import generics
from rest_framework import permissions
from helpers.permissions import IsOwnerOrReadOnly



    #List all topics, or create a new post.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]