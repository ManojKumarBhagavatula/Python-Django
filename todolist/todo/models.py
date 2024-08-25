# models.py
from django.db import models

class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
