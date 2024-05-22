from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    # path("", views.RegisterView, name="sign-up"),
    path("login/", views.LoginView, name="sign-in"),
    path("register/", views.RegisterView, name="sign-up"),
    path("sign-out/", views.logoutView, name="sign-out"),
]
