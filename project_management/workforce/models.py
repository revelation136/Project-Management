from django.db import models


# Create your models here.


class Manpower(models.Model):
    first = models.CharField(max_length=64, default="")
    last = models.CharField(max_length=64, default="")
    position = models.CharField(max_length=64, default="")
    rate = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.last}, {self.first} | {self.position} ({self.rate})"
