from topics.models import Topic
from topics.serializers import TopicSerializer
from rest_framework import generics
from rest_framework import permissions
from helpers.permissions import IsOwnerOrReadOnly


    #List all topics, or create a new topic.

class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    #Retrieve, update or delete a Topic.

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

