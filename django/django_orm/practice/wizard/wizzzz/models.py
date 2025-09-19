from django.db import models

# Create your models here.
class Wizarrd(models.Model):
    name  = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.house})"