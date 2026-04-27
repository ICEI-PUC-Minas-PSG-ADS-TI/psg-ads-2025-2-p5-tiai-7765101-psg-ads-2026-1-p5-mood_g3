from django.db.models import QuerySet


class MoodEntryQuerySet(QuerySet):

    def for_user(self, user):
        return self.filter(user=user)

    def in_period(self, date_from=None, date_to=None):
        qs = self
        if date_from:
            qs = qs.filter(created_at__date__gte=date_from)
        if date_to:
            qs = qs.filter(created_at__date__lte=date_to)
        return qs

    def recent(self, limit=20):
        return self.order_by("-created_at")[:limit]
