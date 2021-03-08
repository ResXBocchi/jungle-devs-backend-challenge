from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import generics
from rest_framework import permissions


    #List all topics, or create a new post.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    #Retrieve, update or delete a post.

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
