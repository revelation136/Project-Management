from django.core.validators import RegexValidator
from django.db import models


# Create your models here.


class Project(models.Model):
    contract_id = models.CharField(
        max_length=50,
        validators=[RegexValidator(r'^[a-zA-Z0-9]+$')],
        default="",
    )
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    duration = models.IntegerField()

    def __str__(self):
        return f"Contract ID: {self.contract_id} | Name:{self.name}"


class PayItem(models.Model):
    contract_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='payitem')
    mobilization = models.IntegerField()
    occupational_safety = models.IntegerField()
    temporary_facility = models.IntegerField()
    reinforce_concrete = models.IntegerField()
    masonry_works = models.IntegerField()
    steel_works = models.IntegerField()

    def __str__(self):
        return f"""
            Mobilization: {self.mobilization}
            Occupational Safety: {self.occupational_safety}
            Temporary Facility: {self.temporary_facility}
            Reinforce Concrete: {self.reinforce_concrete}
            Masonry Works: {self.masonry_works}
            Steel Works: {self.steel_works}
        """
# query: project = Project.objects.get(pk=1)
# items = project.payitem.all() PayItem = payitem this is the syntax