from django.conf import settings
from django.shortcuts import render
from djoser.views import UserViewSet as DjoserUserViewSet
from recipes.models import Tag, User
from rest_framework import filters, permissions, serializers, status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.pagination import PageNumberPagination

from .serializers import TagSerializer, UserSerializer


class UserViewSet(DjoserUserViewSet):
    """Вьюсет для работы с пользователями"""
    http_method_names = ['get', 'post', 'head']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    #permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        """Дает доступ к эндпоинту /me/ только
            аутентифицированным пользователям"""
        if self.action == 'me':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class TagViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с тегами."""
    http_method_names = ['get']
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = None

