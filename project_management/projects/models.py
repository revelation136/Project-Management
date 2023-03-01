from django.db import models


# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    duration = models.IntegerField()

    def __str__(self):
        return f"Name:{self.name} | Location:{self.location} | Owner:{self.owner} | Duration:{self.duration}"
