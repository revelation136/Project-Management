from django.shortcuts import render
from .models import Project, PayItem


# Create your views here.


def index(request):
    return render(request, "projects/index.html", {
        "projects": Project.objects.all(),
    })


def pay_item(request, project_id):
    project = Project.objects.get(id=project_id)
    pay_items = project.payitem.all()
    return render(request, "projects/proj_details.html", {
        "project": project,
        "pay_items": pay_items,
    })