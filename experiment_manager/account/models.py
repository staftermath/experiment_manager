from django.contrib.auth.models import AbstractUser
from django.db import models


class Team(models.Model):

    name = models.CharField(max_length=128, verbose_name="name")
    description = models.TextField(max_length=1024, verbose_name="description", blank=True)

    def __str__(self):
        return self.name


class TeamUser(AbstractUser):

    teams = models.ManyToManyField(Team)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
