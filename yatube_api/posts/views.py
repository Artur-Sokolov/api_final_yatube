from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from .models import Post, Comment
from api.serializers import PostSerializer, CommentSerializer
from api.permissions import IsOwnerOrReadOnly


class ConditionalPagination(LimitOffsetPagination):
    default_limit = 10

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    pagination_class = ConditionalPagination

    def get_paginated_response(self, data):
        if any(k in self.request.query_params for k in ('limit', 'offset')):
            return super().get_paginated_response(data)
        return Response(data)

    def paginate_queryset(self, queryset):
        if any(k in self.request.query_params for k in ('limit', 'offset')):
            return super().paginate_queryset(queryset)
        return None

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    pagination_class = None

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)
