from datetime import datetime
from django.db import models

# Create your models here.
class Dogs(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    image = models.ImageField(upload_to='dog_images/')
    Age = models.IntegerField(default= 5)
    date_registered = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return f'{self.name}'