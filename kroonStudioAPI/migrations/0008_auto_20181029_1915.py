# Generated by Django 2.1.2 on 2018-10-29 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kroonStudioAPI', '0007_auto_20181029_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_by_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='article_usr', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
