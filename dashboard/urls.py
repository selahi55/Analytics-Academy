from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.admin_dashboard, name="dashboard"),
    path("attendees", views.attendees, name="attendees"),
    path("attendees/add", views.add_attendee, name="add-attendee"),
    path("attendees/email", views.email_attendees, name="email-all"),
    path("attendees/<uuid:id>", views.attendee_detail, name="attendee-detail"),
    path("attendees/<uuid:id>/update", views.edit_attendee, name="update-attendee"),
    path("attendees/<uuid:id>/delete", views.delete_attendee, name="delete-attendee"),
    path("attendees/<uuid:id>/email", views.email_attendee, name="email-attendee"),

    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password-reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]