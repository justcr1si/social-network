from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=25, verbose_name='Имя пользователя',
                                unique=True)
    password = models.CharField(max_length=100, verbose_name='Пароль')
    description = models.TextField(max_length=200, verbose_name='Описание',
                                   blank=True, null=True)
    image = models.ImageField(
        verbose_name='Изображение', blank=True, null=True,
        upload_to='profile-images/')

    class Meta:
        db_table = 'user'
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователей'

    def __str__(self):
        return self.username
