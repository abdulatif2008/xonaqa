from django.db import models
from players.models import Player

class Match(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    result = models.CharField(max_length=20)
    man_of_the_match = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
