# Generated by Django 2.1.2 on 2018-10-27 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kroonStudioAPI', '0002_auto_20181028_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
