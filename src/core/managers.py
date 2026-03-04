from django.db.models import QuerySet


class MoodEntryQuerySet(QuerySet):

    def for_user(self, user):
        return self.filter(user=user)

    def recent(self, limit=20):
        return self.order_by("-created_at")[:limit]
