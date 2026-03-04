from rest_framework import serializers

from .models import MoodEntry


class MoodEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = MoodEntry
        fields = ["id", "emotion", "intensity_level", "notes", "created_at"]
        read_only_fields = ["id", "created_at"]
