# Generated by Django 4.0.3 on 2022-04-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='', max_length=20),
        ),
    ]
