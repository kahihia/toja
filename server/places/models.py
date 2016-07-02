
from django.db import models


class Area(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(default='')


class Attraction(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    address_jp = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(default='')
    images = models.TextField(default='')
    has_location = models.BooleanField(default=False)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    area = models.ForeignKey(Area)


class Hospital(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    tel = models.CharField(max_length=100, blank=True, default='')
    hours = models.CharField(max_length=100, blank=True, default='')
    after_hours = models.CharField(max_length=100, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    url = models.TextField(default='')
    image = models.TextField(default='')
    has_location = models.BooleanField(default=False)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
