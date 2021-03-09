from rest_framework import serializers
from topics.models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id','author_id', 'created_at', 'updated_at','title','name','description','urlname']
        lookup_field = 'urlname'
