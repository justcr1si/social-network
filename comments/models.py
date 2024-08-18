from django.db import models

from profile_page.models import User
from feed.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300, verbose_name='Текст комментария')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
        verbose_name = 'комментария'
        verbose_name_plural = 'комментариев'
