from comments.models import Comment
from posts.models import Post
from comments.api.v1.serializers import CommentSerializer
from rest_framework import generics, permissions, viewsets
from helpers.permissions import IsOwnerOrReadOnly



    #List all topics, or create a new comment.

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post = Post.objects.get())

