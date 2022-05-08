# Generated by Django 4.0.3 on 2022-04-07 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogSite', '0004_alter_post_options_alter_post_publish_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('body', models.CharField(max_length=250)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogSite.post')),
            ],
        ),
    ]