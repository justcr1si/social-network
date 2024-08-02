# Generated by Django 4.2.14 on 2024-08-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_page', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, unique=True, verbose_name='Имя пользователя')),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
            ],
        ),
    ]
