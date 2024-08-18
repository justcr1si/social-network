# Generated by Django 4.2.14 on 2024-08-14 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_remove_post_comments'),
        ('comments', '0003_delete_commentroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='feed.post'),
        ),
    ]
