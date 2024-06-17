from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def login_user(request):
    error_message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            # Handle invalid login attempt
            error_message = "Invalid username or password"
    else:
        form = AuthenticationForm()

    context = {"form": form, "error_message": error_message}
    return render(request, "users/login.html", context)


def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    """Register a new user"""
    if request.method != "POST":
        # Display blank registration form
        form = UserCreationForm()
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            # Log the user in and athenticate to home page
            authenticated_user = authenticate(
                username=new_user.username, password=request.POST["password1"]
            )
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse("index"))

    context = {"form": form}
    return render(request, "users/register.html", context)
