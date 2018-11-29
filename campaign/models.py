from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
    )

    description = models.CharField(
        max_length=50,
    )

    game_master = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name = 'gm'
    )

    players = models.ManyToManyField(
        User,
        related_name = 'player',
        blank=True,
        null=True,
    )

    public = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name


class Character(models.Model):
  name = models.CharField(
    unique=True,
    max_length=50,
  )

  tagline = models.CharField(
    max_length=50,
  )

  player = models.ForeignKey(
    User,
    on_delete=models.PROTECT,
    blank=True,
    null=True,
  )

  def __str__(self):
    return self.name


class Faction(models.Model):
  name = models.CharField(
    unique=True,
    max_length=50,
  )

  tagline = models.CharField(
    max_length=50,
  )

  def __str__(self):
    return self.name


class Item(models.Model):
  name = models.CharField(
    unique=True,
    max_length=50,
  )

  def __str__(self):
    return self.name


class Location(models.Model):
  name = models.CharField(
    unique=True,
    max_length=50,
  )

  def __str__(self):
    return self.name
