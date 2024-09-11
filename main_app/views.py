from django.shortcuts import render
from django.http import HttpResponse
from .models import MyPOV


# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

# def sign_up(request):
#     return render(request, "POV/signup.html", {"myPOVs": myPOVs})

def sign_up(request):
    return render(request, "POV/signup.html")


def sign_in(request):
    return render(request, "POV/signin.html")
