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

    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()

    category_id = models.ForeignKey(Category, related_name='article_cat', on_delete=models.CASCADE)
    created_by_user_id = models.ForeignKey(User, related_name='article_usr', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title

