# Generated by Django 4.1.5 on 2023-05-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_event_date_event_event_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_img',
            field=models.ImageField(upload_to='uploads/images'),
        ),
    ]
