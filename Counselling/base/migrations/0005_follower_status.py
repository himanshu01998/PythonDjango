# Generated by Django 3.2.9 on 2021-12-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20211208_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
