from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from .managers import MoodEntryQuerySet


class MoodEntry(models.Model):
    """Represents a single mood/emotion record for a given user."""

    class Emotion(models.TextChoices):
        HAPPY = "HAPPY", "Happy"
        SAD = "SAD", "Sad"
        NEUTRAL = "NEUTRAL", "Neutral"
        ANXIOUS = "ANXIOUS", "Anxious"
        STRESSED = "STRESSED", "Stressed"

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="mood_entries",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    intensity_level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Scale from 1 to 10",
    )
    emotion = models.CharField(
        max_length=20,
        choices=Emotion.choices,
        default=Emotion.NEUTRAL,
    )
    notes = models.TextField(blank=True, null=True)

    objects = MoodEntryQuerySet.as_manager()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Mood Entry"
        verbose_name_plural = "Mood Entries"

    def __str__(self) -> str:
        return (
            f"{self.user.username} – {self.get_emotion_display()} "
            f"({self.intensity_level}/10) on "
            f"{self.created_at:%Y-%m-%d}"
        )