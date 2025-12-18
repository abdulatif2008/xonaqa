from django.db import models
from matches.models import Match
from players.models import Player

class Goal(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    scored_by = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    result = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.scored_by} - {self.match}"
