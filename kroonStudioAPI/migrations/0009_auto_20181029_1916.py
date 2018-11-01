# Generated by Django 2.1.2 on 2018-10-29 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kroonStudioAPI', '0008_auto_20181029_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_by_user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
