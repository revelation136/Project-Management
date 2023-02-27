from django.shortcuts import render
from .models import Manpower

# Create your views here.


def employee_list(request):
    return render(request, "workforce/index.html", {
        "manpowers": Manpower.objects.all()
    })
