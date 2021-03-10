from posts.models import Post
from topics.models import Topic
from posts.api.v1.serializers import PostSerializer
from topics.api.v1.serializers import TopicSerializer
from rest_framework import generics, permissions, viewsets,serializers
from helpers.permissions import IsOwnerOrReadOnly



    #List all topics, or create a new post.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,  topic = Topic.objects.get())