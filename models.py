from django.db import models
# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=150)
    email = models.IntegerField(default=0)

    def __str__(self):
        return self.username