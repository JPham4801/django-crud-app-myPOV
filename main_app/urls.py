from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("signup/", views.sign_up, name="sign-up"),
    path("signin/", views.sign_in, name="sign-in"),
]
