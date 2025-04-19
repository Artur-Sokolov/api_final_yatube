from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from .models import Post
from api.serializers import PostSerializer, CommentSerializer
from api.permissions import IsOwnerOrReadOnly
