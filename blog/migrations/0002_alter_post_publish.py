# Generated by Django 3.2.7 on 2021-09-08 12:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 12, 55, 25, 881734, tzinfo=utc)),
        ),
    ]
