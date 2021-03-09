"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin
from topics.views import TopicViewSet
from comments.views import CommentViewSet
from posts.views import PostViewSet
from rest_framework_nested import routers



from helpers.health_check_view import health_check

""" Main router """
topic_router = routers.DefaultRouter()

topic_router.register(r'topics', TopicViewSet, basename='topics')
## generates:
# /topics/
# /topics/{urlname}/
post_router = routers.NestedSimpleRouter(topic_router, r'topics', lookup='topic')
post_router.register(r'posts', PostViewSet, basename='posts')
## generates:
# /topics/{urlname}/posts/
# /topics/{urlname}/posts/{post_id}/
comment_router = routers.NestedSimpleRouter(post_router, r'posts', lookup='post')
comment_router.register(r'comments', CommentViewSet, basename='comments')
## generates:
# /topics/{urlname}/posts/{post_id}/comments/
# /topics/{urlname}/posts/{post_id}/comments/{comment_id}/

###
# URLs
###
urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Applications
    url(r'^', include('accounts.urls')),
    url(r'^', include(topic_router.urls)),
    url(r'^', include(post_router.urls)),
    url(r'^', include(comment_router.urls)),

]
