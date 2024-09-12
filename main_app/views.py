from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import MyPOV


# Define the home view function
class Home(LoginView):
    template_name = "home.html"


def home(request):
    # Send a simple HTML response
    return render(request, "home.html")


def explore(request):
    povs = MyPOV.objects.all()
    return render(request, "explore.html", {"povs": povs})


@login_required
def pov_index(request):
    povs = MyPOV.objects.filter(user=request.user)
    return render(request, "povs/index.html", {"povs": povs})


@login_required
def pov_detail(request, pov_id):
    pov = MyPOV.objects.get(id=pov_id)
    return render(request, "povs/detail.html", {"pov": pov})


def signup(request):
    error_message = ""
    if request.method == "POST":
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect("pov-index")
        else:
            error_message = "Invalid sign up - try again"
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "signup.html", context)


class CreatePost(LoginRequiredMixin, CreateView):
    model = MyPOV
    fields = ["title", "description"]

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the pov
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = MyPOV
    fields = ["title", "description"]


class DeletePost(LoginRequiredMixin, DeleteView):
    model = MyPOV
    success_url = reverse_lazy("pov-index")
