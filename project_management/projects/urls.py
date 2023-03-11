from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:project_id>", views.pay_item, name="pay_item"),
]
