from django.urls import path
from . import views

urlpatterns = [
    path("", views.admin_dashboard, name="dashboard"),
    path("attendees", views.attendees, name="attendees"),
    path("attendees/add", views.add_attendee, name="add-attendee"),
    path("attendees/<uuid:id>", views.attendee_detail, name="attendee-detail"),
    path("attendees/<uuid:id>/update", views.edit_attendee, name="update-attendee"),
    path("attendees/<uuid:id>/delete", views.delete_attendee, name="delete-attendee"),
]