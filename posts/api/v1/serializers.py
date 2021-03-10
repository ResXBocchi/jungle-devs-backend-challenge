from rest_framework import serializers
from topics.api.v1.serializers import TopicSerializer
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author','topic')
