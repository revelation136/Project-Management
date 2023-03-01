from django.shortcuts import render
from .models import Projects


# Create your views here.


def index(request):
    return render(request, "projects/index.html", {
        "projects": Projects.objects.all()
    })
