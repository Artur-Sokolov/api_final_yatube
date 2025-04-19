from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register(r'posts', PostViewSet, basename='posts')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
v1_router.register(r'follow', FollowViewSet, basename='follow')
v1_router.register(r'groups', GroupViewSet, basename='groups')

api_v1_urls = [
    path('', include(v1_router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(api_v1_urls)),
]
