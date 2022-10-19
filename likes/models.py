from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Class for likes model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )

    class Meta:
        """
        Likes model meta class
        """
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner}{self.post}'