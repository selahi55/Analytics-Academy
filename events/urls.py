from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("form/", views.apply, name="apply"),
    path("program/", views.program, name="program"),
]