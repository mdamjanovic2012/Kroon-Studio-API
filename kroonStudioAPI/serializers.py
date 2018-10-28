from django.contrib.auth.models import User
from kroonStudioAPI.models import Article, Category
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=False,source='article_usr', read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=False, source='article_cat', read_only=True)

    class Meta:
        model = Article
        fields = ('title', 'content', 'updated_at', 'created_at', 'category', 'user')


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('title',)
