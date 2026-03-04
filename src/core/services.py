from .models import MoodEntry


class MoodEntryService:

    @staticmethod
    def get_user_entries(user, limit=20):
        return MoodEntry.objects.for_user(user).recent(limit)

    @staticmethod
    def create_entry(user, form):
        entry = form.save(commit=False)
        entry.user = user
        entry.save()
        return entry
