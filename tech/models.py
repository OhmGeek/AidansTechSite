# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
# Create your models here.
class TechItem(models.Model):
    """ Individual items """
    name = models.CharField(max_length=70)
    description = models.TextField()
    quantity = models.IntegerField()
    image = models.URLField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    weight_kg = models.DecimalField(max_digits=6, decimal_places=1, blank=True)
    user_guide = models.URLField(blank=True)

    def __str__(self):
        """ Override the Item Name"""
        return self.name

    def get_absolute_url(self):
        return '/equipment/item/' + str(self.pk)
