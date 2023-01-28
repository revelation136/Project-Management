from django.shortcuts import render


# Create your views here.


def work_force(request):
    return render(request, "work_force/work_force.html")
