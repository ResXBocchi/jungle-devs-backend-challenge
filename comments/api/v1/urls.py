from .views import CommentViewSet
from rest_framework_nested import routers
from posts.api.v1.urls import post_router
from django.conf.urls import url, include


comment_router = routers.NestedSimpleRouter(post_router, r'posts', lookup='post')
comment_router.register(r'comments', CommentViewSet, basename='comments')
## generates:
# /topics/{urlname}/posts/{post_id}/comments/
# /topics/{urlname}/posts/{post_id}/comments/{comment_id}/

urlpatterns = [
    url(r'', include(comment_router.urls))
]
