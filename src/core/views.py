from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import MoodEntryForm
from .services import MoodEntryService


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
