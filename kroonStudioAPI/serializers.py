from django.contrib.auth.models import User
from kroonStudioAPI.models import Article, Category
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'url', 'username', 'email')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(required=True, max_length=100, allow_blank=False)

    class Meta:
        model = Category
        fields = ('id', 'title',)


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    created_by_user_id = UserSerializer(many=False, default=serializers.CurrentUserDefault(),
                                                            read_only=True)
    title = serializers.CharField(required=True, max_length=100, allow_blank=False)

    class Meta:
        model = Article
        fields = ('id', 'title', 'category_id', 'content', 'updated_at', 'created_by_user_id')

    def to_representation(self, instance):
        representation = super(ArticleSerializer, self).to_representation(instance)
        representation['category_id'] = CategorySerializer(instance.category_id).data
        return representation
