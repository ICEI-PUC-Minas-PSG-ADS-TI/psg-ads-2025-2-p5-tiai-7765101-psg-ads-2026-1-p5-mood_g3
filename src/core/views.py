from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import MoodEntryForm
from .services import MoodEntryService


@login_required
def dashboard_view(request):
    entries = MoodEntryService.get_user_entries(request.user)
    return render(request, "core/dashboard.html", {"entries": entries})


@login_required
@login_required
@login_required
def create_entry_view(request):
    if request.method == "POST":
        form = MoodEntryForm(request.POST)
        if form.is_valid():
            MoodEntryService.create_entry(request.user, form)
            return redirect("core:dashboard")
    else:
        form = MoodEntryForm()

    # O return deve ter 4 espaços (ou um TAB) de recuo para estar DENTRO da função
    return render(request, "registro_humor/registro_humor.html", {"form": form})