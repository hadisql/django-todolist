from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Task(models.Model):
    title = models.TextField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    priority = models.PositiveSmallIntegerField(default=1,
                                                validators=[MinValueValidator(1),
                                                            MaxValueValidator(3)],
                                                choices=[(1,'1: Low'),
                                                         (2,'2: Normal'),
                                                         (3,'3: High')])

    created_by = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
