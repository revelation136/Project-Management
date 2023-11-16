from django.db import models
# double dot means one step backward on directory
# from .. projects.models import Project

from django.apps import apps

Project = apps.get_model('projects', 'Project')


# Create your models here.


class EmployeeList(models.Model):
    first = models.CharField(max_length=64, default="")
    last = models.CharField(max_length=64, default="")
    position = models.CharField(max_length=64, default="")
    rate = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.last}, {self.first} | {self.position} ({self.rate})"


class ProjectWorkforce(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    first = models.ForeignKey(EmployeeList)