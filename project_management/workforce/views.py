from django.shortcuts import render
from .models import EmployeeList

# Create your views here.


def employee_list(request):
    return render(request, "workforce/index.html", {
        "employees": EmployeeList.objects.all()
    })
