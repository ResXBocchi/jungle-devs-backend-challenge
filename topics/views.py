from topics.models import Topic
from topics.serializers import TopicSerializer
from rest_framework import generics

    #List all topics, or create a new topic.

class TopicList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    #Retrieve, update or delete a Topic.

class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
