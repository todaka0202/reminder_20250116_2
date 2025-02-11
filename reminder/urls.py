from django.urls import path

from . import views

app_name = "reminder"

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("SaveSchedul/", views.SaveSchedule, name="SaveSchedule"),
    ]
