from django.urls import path

from . import views

urlpatterns = [
    # Login page
    path("login/", views.login_user, name="login"),
    # Logout page
    path("logout/", views.logout_view, name="logout"),
    # Regsitration page
    path("register/", views.register, name="register"),
]
