from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import CommentViewSet, PostViewSet
from api.views import FollowViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/jwt', include('djoser.urls.jwt')),
]
