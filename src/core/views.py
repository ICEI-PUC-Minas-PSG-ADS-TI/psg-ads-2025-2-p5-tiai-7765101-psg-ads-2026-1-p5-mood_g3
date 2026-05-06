from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Count, Avg
from django.db.models.functions import TruncDate
from .forms import MoodEntryForm, UserRegistrationForm
from .models import MoodEntry
from .services import MoodEntryService

def index(request):
    if request.user.is_authenticated:
        return redirect("core:dashboard")
    users = User.objects.count()
    registers = MoodEntry.objects.count()
    return render(request, "core/home.html", {"users": users, "registers": registers})


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
    date_from = request.GET.get("date_from") or None
    date_to = request.GET.get("date_to") or None
    entries = MoodEntryService.get_user_entries(request.user, date_from=date_from, date_to=date_to)
    return render(request, "core/dashboard.html", {
        "entries": entries,
        "date_from": date_from or "",
        "date_to": date_to or "",
    })

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


@login_required
def edit_entry_view(request, pk):
    entry = get_object_or_404(MoodEntry, pk=pk, user=request.user)
    if request.method == "POST":
        form = MoodEntryForm(request.POST, instance=entry)
        if form.is_valid():
            MoodEntryService.update_entry(entry, form)
            return redirect("core:dashboard")
    else:
        form = MoodEntryForm(instance=entry)
    return render(request, "core/edit_entry.html", {"form": form, "entry": entry})


@login_required
def delete_entry_view(request, pk):
    entry = get_object_or_404(MoodEntry, pk=pk, user=request.user)
    if request.method == "POST":
        MoodEntryService.delete_entry(entry)
        return redirect("core:dashboard")
    return render(request, "core/delete_entry.html", {"entry": entry})

@login_required
def dashboard_graphs(request):
    entries = MoodEntry.objects.filter(user=request.user)

    daily = (
        entries.annotate(date=TruncDate("created_at"))
        .values("date")
        .annotate(avg=Avg("intensity_level"))
        .order_by("date")
    )

    emotions = (
        entries.values("emotion")
        .annotate(count=Count("emotion"))
        .order_by("-count")
    )

    return render(request, "core/dashboard_graphs.html", {
        "daily": list(daily),
        "emotions": list(emotions),
    })