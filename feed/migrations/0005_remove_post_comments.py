# Generated by Django 4.2.14 on 2024-08-14 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_alter_post_comments_alter_post_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
    ]
