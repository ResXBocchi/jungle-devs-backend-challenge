from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework import generics

    #List all topics, or create a new comment.

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    #Retrieve, update or delete a comment.

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer