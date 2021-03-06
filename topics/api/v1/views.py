from topics.models import Topic
from topics.api.v1.serializers import TopicSerializer
from rest_framework import generics, permissions, viewsets
from helpers.permissions import IsOwnerOrReadOnly


    #List all topics, or create a new topic.

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'urlname'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
