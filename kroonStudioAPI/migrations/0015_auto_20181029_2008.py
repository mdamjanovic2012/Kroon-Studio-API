# Generated by Django 2.1.2 on 2018-10-29 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kroonStudioAPI', '0014_auto_20181029_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-updated_at',)},
        ),
    ]