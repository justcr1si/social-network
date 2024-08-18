from django.db import models

from profile_page.models import User


class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100, verbose_name='Тема поста')
    text = models.TextField(verbose_name='Текст поста', max_length=1000)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'
        verbose_name = 'поста'
        verbose_name_plural = 'постов'
