# Generated by Django 4.1.1 on 2022-10-19 19:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FollowerModel',
            new_name='Follower',
        ),
    ]