# Generated by Django 2.1.2 on 2018-10-30 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kroonStudioAPI', '0020_auto_20181030_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportrecipient',
            name='scheduled_report',
        ),
        migrations.RemoveField(
            model_name='scheduledreportgroup',
            name='scheduled_report',
        ),
        migrations.DeleteModel(
            name='ReportRecipient',
        ),
        migrations.DeleteModel(
            name='ScheduledReport',
        ),
        migrations.DeleteModel(
            name='ScheduledReportGroup',
        ),
    ]
