from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import generics
from rest_framework import permissions


    #List all topics, or create a new comment.

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    #Retrieve, update or delete a comment.

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
