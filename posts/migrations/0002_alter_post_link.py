# Generated by Django 4.1.1 on 2022-10-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True, db_index=True),
        ),
    ]
