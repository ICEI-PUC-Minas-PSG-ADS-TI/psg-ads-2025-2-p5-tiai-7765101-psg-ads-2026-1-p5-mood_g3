from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import MoodEntryForm, UserRegistrationForm
from .services import MoodEntryService

def index(request):
    if request.user.is_authenticated:
        return redirect("core:dashboard")
    
    return render(request, "registration/login.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("core:dashboard")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["email"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
                first_name=form.cleaned_data["name"],
            )
            login(request, user)
            messages.success(request, "Conta criada com sucesso!")
            return redirect("core:dashboard")
    else:
        form = UserRegistrationForm()

    return render(request, "registration/login.html", {"register_form": form, "show_register": True})


@login_required
def dashboard_view(request):
    entries = MoodEntryService.get_user_entries(request.user)
    return render(request, "core/dashboard.html", {"entries": entries})

@login_required
def create_entry_view(request):
    if request.method == "POST":
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            MoodEntryService.create_entry(request.user, form)
            return redirect("core:dashboard")
    else:
        form = MoodEntryForm()

    return render(request, "core/create_entry.html", {"form": form})