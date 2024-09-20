from django.db import models

# Create your models here.

class Tiffin(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='tiffin_images/')

    def __str__(self):
        return self.name

class ColdDrink(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cold_drink_images/')

    def __str__(self):
        return self.name

 