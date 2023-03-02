from django.shortcuts import render
from .models import Projects, GeneralRequirement


# Create your views here.


def index(request):
    return render(request, "projects/index.html", {
        "projects": Projects.objects.all()
    })


def xyz(request, project_id):
    project = Projects.objects.get(id=project_id)
    return render(request, "projects/proj_details.html", {
        "gen_req": GeneralRequirement.objects.all(),
        "project": project
    })
