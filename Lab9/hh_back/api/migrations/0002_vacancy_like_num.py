# Generated by Django 4.2 on 2023-04-08 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='like_num',
            field=models.FloatField(default=0),
        ),
    ]
