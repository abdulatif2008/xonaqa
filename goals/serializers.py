from rest_framework import serializers
from .models import Goal
from matches.serializers import MatchSerializer
from players.serializers import PlayerSerializer

class GoalSerializer(serializers.ModelSerializer):
    match_title = serializers.CharField(source='match.title', read_only=True)
    scored_by_name = serializers.SerializerMethodField()

    class Meta:
        model = Goal
        fields = ['id', 'match_title', 'result', 'video', 'scored_by_name']

    def get_scored_by_name(self, obj):
        if obj.scored_by:
            return f"{obj.scored_by.first_name} {obj.scored_by.last_name}"
        return None
