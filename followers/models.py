from django.db import models
from django.contrib.auth.models import User


class FollowerModel(models.Model):
    """
    Class for follower model
    """
    owner = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        """
        Meta class for follower model
        """
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner}{self.followed}'