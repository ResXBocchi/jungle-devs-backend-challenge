from .views import PostViewSet
from topics.api.v1.urls import topic_router
from rest_framework_nested import routers
from django.conf.urls import url, include


post_router = routers.NestedSimpleRouter(topic_router, r'topics', lookup='topic')
post_router.register(r'posts', PostViewSet, basename='posts')
## generates:
# /topics/{urlname}/posts/
# /topics/{urlname}/posts/{post_id}/


urlpatterns = [
    url(r'', include(post_router.urls))
]
