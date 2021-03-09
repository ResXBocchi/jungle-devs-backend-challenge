from .views import TopicViewSet
from rest_framework_nested import routers
from django.conf.urls import url, include



topic_router = routers.DefaultRouter()
topic_router.register(r'topics', TopicViewSet, basename='topics')
## generates:
# /topics/
# /topics/{urlname}/

urlpatterns = [
    url(r'', include(topic_router.urls))
]
