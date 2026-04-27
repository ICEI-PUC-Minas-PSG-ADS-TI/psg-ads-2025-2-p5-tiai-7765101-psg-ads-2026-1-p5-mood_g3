from .models import MoodEntry


class MoodEntryService:

    @staticmethod
    def get_user_entries(user, date_from=None, date_to=None, limit=20):
        qs = MoodEntry.objects.for_user(user).in_period(date_from, date_to)
        if date_from or date_to:
            return qs.order_by("-created_at")
        return qs.recent(limit)

    @staticmethod
    def create_entry(user, form):
        entry = form.save(commit=False)
        entry.user = user
        entry.save()
        return entry

    @staticmethod
    def update_entry(entry, form):
        return form.save()

    @staticmethod
    def delete_entry(entry):
        entry.delete()
