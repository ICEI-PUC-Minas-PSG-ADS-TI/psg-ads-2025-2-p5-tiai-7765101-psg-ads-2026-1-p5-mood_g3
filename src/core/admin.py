from django.contrib import admin

from .models import MoodEntry


@admin.register(MoodEntry)
class MoodEntryAdmin(admin.ModelAdmin):
    list_display = ("user", "emotion", "intensity_level", "created_at")
    list_filter = ("emotion", "created_at")
    search_fields = ("user__username", "notes")
    readonly_fields = ("created_at",)
