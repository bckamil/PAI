from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Tournament(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    discipline = models.CharField(max_length=64, null=False, blank=False)
    datetime = models.DateTimeField()
    limit = models.IntegerField(validators=[MinValueValidator(2)])
    deadline = models.DateTimeField()
    organizer = models.CharField(max_length=128, null=False, blank=False)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament_application = models.ForeignKey(
        Tournament, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=64)
    ranking = models.IntegerField(validators=[MinValueValidator(1)])


class Match(models.Model):
    player_1 = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, related_name='player_2')
    player_2 = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, related_name='player_1')
    winner = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True, related_name='winner')
    winner_set_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True, related_name='winner_set_by')
    accept = models.BooleanField(default=None, blank=True, null=True)

    tournament_level = models.IntegerField()
    next_match = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-tournament_level', 'id']


class SponsorLogo(models.Model):
    logo = models.ImageField()
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
