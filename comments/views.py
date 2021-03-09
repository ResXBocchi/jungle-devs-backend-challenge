from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import generics, permissions, viewsets
from helpers.permissions import IsOwnerOrReadOnly



    #List all topics, or create a new comment.

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]