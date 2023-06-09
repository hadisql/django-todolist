from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [(1,'1: Low'),(2,'2: Normal'),(3,'3: High')]
    title = models.TextField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    priority = models.PositiveSmallIntegerField(default=PRIORITY_CHOICES[1][1],
                                                validators=[MinValueValidator(1),
                                                            MaxValueValidator(3)],
                                                choices=PRIORITY_CHOICES)

    created_by = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, null=True, related_name="tags")

    def __str__(self):
        return self.title
