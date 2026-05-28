from datetime import datetime, time, timedelta

from django.db.models import QuerySet
from django.utils import timezone


class MoodEntryQuerySet(QuerySet):

    def for_user(self, user):
        return self.filter(user=user)

    def in_period(self, date_from=None, date_to=None):
        qs = self
        if date_from:
            start_date = datetime.strptime(date_from, "%Y-%m-%d").date()
            start_datetime = timezone.make_aware(datetime.combine(start_date, time.min), timezone.get_current_timezone())
            qs = qs.filter(created_at__gte=start_datetime)
        if date_to:
            end_date = datetime.strptime(date_to, "%Y-%m-%d").date()
            end_datetime = timezone.make_aware(
                datetime.combine(end_date + timedelta(days=1), time.min),
                timezone.get_current_timezone(),
            )
            qs = qs.filter(created_at__lt=end_datetime)
        return qs

    def recent(self, limit=20):
        return self.order_by("-created_at")[:limit]
