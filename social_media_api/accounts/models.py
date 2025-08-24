from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)


# followers/following – directional M2M
followers = models.ManyToManyField(
    "self", symmetrical=False, related_name="following", blank=True
)


def __str__(self):
    return self.username