from django.contrib.auth.models import User
from kroonStudioAPI.models import Category, Article
from rest_framework import viewsets
from kroonStudioAPI.serializers import UserSerializer, CategorySerializer, ArticleSerializer
from rest_framework.permissions import IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        return [IsAdminUser()]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('title')
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('updated_at')
    serializer_class = ArticleSerializer
