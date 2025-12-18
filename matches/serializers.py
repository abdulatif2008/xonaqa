from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    man_of_the_match_name = serializers.CharField(
        source='man_of_the_match.first_name', read_only=True
    )
    man_of_the_match_surname = serializers.CharField(
        source='man_of_the_match.last_name', read_only=True
    )

    class Meta:
        model = Match
        fields = ['id', 'title', 'result', 'description', 'man_of_the_match_name', 'man_of_the_match_surname']
