import json
from pathlib import Path

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from core.models import MoodEntry

SEEDS = Path(__file__).resolve().parent.parent.parent / "seeds"


class Command(BaseCommand):
    help = "Seed users and mood entries from JSON files."

    def handle(self, *args, **options):
        users = json.loads((SEEDS / "user_dump.json").read_text())
        entries = json.loads((SEEDS / "registries_dump.json").read_text())

        for u in users:
            if not User.objects.filter(username=u["email"]).exists():
                User.objects.create_user(
                    username=u["email"], email=u["email"],
                    password=u["password"], first_name=u["name"]
                )

        if not MoodEntry.objects.exists():
            for e in entries:
                user = User.objects.get(username=e["user_email"])
                MoodEntry.objects.create(
                    user=user, emotion=e["emotion"],
                    intensity_level=e["intensity_level"],
                    notes=e.get("notes")
                )
                

        self.stdout.write(self.style.SUCCESS("Seed done."))
