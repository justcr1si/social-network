# Generated by Django 4.2.14 on 2024-08-01 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0004_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, verbose_name='Пароль'),
        ),
    ]
