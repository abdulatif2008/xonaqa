from django.db import models


# =========================
# COACH / MANAGER MODEL
# =========================
class Coach(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='coaches/')

    def __str__(self):
        return self.name


# =========================
# PLAYER MODEL
# =========================
class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(null=True, blank=True)
    jersey_number = models.IntegerField()
    image = models.ImageField(upload_to='players/')
    position = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
