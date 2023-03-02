from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path("", views.index, name="index"),
    path("project/<int:project_id>", views.xyz, name="xyz")
]
