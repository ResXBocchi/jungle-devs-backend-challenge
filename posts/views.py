from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import generics
from rest_framework import permissions
from helpers.permissions import IsOwnerOrReadOnly



    #List all topics, or create a new post.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    #Retrieve, update or delete a post.

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
