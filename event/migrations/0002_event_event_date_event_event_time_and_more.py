# Generated by Django 4.1.5 on 2023-05-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(help_text='Enter event date', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_time',
            field=models.TimeField(help_text='Enter event time', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_is_liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_location',
            field=models.CharField(help_text='Enter event Location', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(help_text='Enter Event Name', max_length=100),
        ),
    ]
