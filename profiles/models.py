from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile Model
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.TextField(max_length=255)
    profile_img = models.ImageField(
        upload_to='images/', default='../default_profile_gzzgv2'
    )

    class Meta:
        """
        Profile model meta class
        """
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Function to connect new instance of profile to owner
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)

