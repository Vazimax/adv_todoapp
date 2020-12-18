from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    task = models.CharField(max_length=100)
    published_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
    