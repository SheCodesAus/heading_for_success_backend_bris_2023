from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):

    image = models.URLField(max_length=200, blank=True)
    pass

    def __str__(self):
        return self.username