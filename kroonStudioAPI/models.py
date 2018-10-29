from django.conf import settings
from django.contrib.auth.models import User, models


class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        verbose_name_plural = "categories"
        ordering = ('title',)

    def __str__(self):
        return self.title


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100, blank=False, default='')
    content = models.TextField()

    category_id = models.ForeignKey(Category, related_name='article_cat', on_delete=models.CASCADE)
    created_by_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_by_user_id',
                                           on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ('-updated_at', )

    def __str__(self):
        return self.title
