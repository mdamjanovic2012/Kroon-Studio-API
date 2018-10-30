from django.contrib.auth.models import User
from kroonStudioAPI import permissions
from kroonStudioAPI.models import Category, Article
from rest_framework import viewsets
from kroonStudioAPI.serializers import UserSerializer, CategorySerializer, ArticleSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self): # Only admin can edit users
        return [IsAdminUser()]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('title')
    serializer_class = CategorySerializer

    def get_permissions(self): # Only admin can edit categories
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]

        return super(self.__class__, self).get_permissions()


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('$title', '$content') # Regex search

    def perform_create(self, serializer):
        serializer.save(created_by_user_id=self.request.user)

    def get_permissions(self): # Permission for edition articles
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.ArticleEditPermission, ]

        return super(self.__class__, self).get_permissions()