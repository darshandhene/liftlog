from django.urls import path
from django.contrib.auth import views as auth_views
from journal import views

urlpatterns = [
    path("", views.home, name="journal-home"),
    path("workouts/<int:pk>/", views.detail, name="journal-detail"),
    path("register/", views.register, name="web-register"),
    path("login/", auth_views.LoginView.as_view(template_name="journal/form.html"), name="web-login"),
    path("logout/", auth_views.LogoutView.as_view(), name="web-logout"),
]
