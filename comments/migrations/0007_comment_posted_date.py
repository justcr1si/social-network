# Generated by Django 4.2.14 on 2024-08-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_alter_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_date',
            field=models.DateField(auto_now=True, verbose_name='Дата публикации'),
        ),
    ]
