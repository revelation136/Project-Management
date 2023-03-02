from django.db import models


# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    duration = models.IntegerField()

    def __str__(self):
        return f"Name:{self.name} | Location:{self.location} | Owner:{self.owner} | Duration:{self.duration}"


class GeneralRequirement(models.Model):
    name = models.ForeignKey(Projects, on_delete=models.CASCADE)
    project_supervision = models.IntegerField()
    delivery = models.IntegerField()
    service_vehicle = models.IntegerField()
    water_consumption = models.IntegerField()
    power_consumption = models.IntegerField()
    first_aid = models.IntegerField()

    def __str__(self):
        return f"""
            Name: {self.name.name}
            Project Supervision: ${self.project_supervision}
            Delivery of Materials: ${self.delivery}
            Service Vehicle: ${self.service_vehicle}
            Water Consumption: ${self.water_consumption}
            Power Consumption: ${self.power_consumption}
            First Aid: ${self.first_aid}
        """
