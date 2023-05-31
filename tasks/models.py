from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    priority = models.PositiveIntegerField(default=1)

    created_by = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
