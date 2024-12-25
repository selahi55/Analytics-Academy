from django.urls import path
from . import views

urlpatterns = [
    # For the Admin
    # Login
    path('login/', views.login, name='login'),
    # Logout
    path('logout/', views.logout, name='logout'),

    # Data
    path('data/', views.data, name='data'),
    path('create-attendee/', views.create_attendee, name='create-attendee'),
    path('update-attendee/', views.update_attendee, name='update-attendee'),
    path('delete-attendee/', views.delete_attendee, name='delete-attendee'),

    # For the User
    path('post-data/', views.post_data, name="post_data"),
]