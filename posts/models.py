from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2000)
    image = models.ImageField(
        upload_to='images/', default='../default_post_jshpia.jpg'
    )

    class Meta:
        """
        Post model meta class
        """
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}'
