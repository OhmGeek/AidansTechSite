# -*- coding: utf-8 -*-
from django.db import models


class TechTag(models.Model):
    """ Tags assigned to items"""
    name = models.CharField(max_length=50)

    def __str__(self):
        """ Override the Tag Name """
        return self.name


# Create your models here.
class TechItem(models.Model):
    """ Individual items """
    name = models.CharField(max_length=70)
    description = models.TextField()
    quantity = models.IntegerField()
    tags = models.ManyToManyField(TechTag, blank=True)
    image = models.URLField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        """ Override the Item Name"""
        return self.name


class Hire(models.Model):
    """ A requested hire """
    booking_name = models.CharField(max_length=250)
    hirer_name = models.CharField(max_length=100)
    invoice_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    date_out = models.DateTimeField()
    date_in = models.DateTimeField()
    contact_number = models.CharField(max_length=20)


class ItemHire(models.Model):
    """ Specific items to hire """
    item = models.ForeignKey(TechItem)
    hire = models.ForeignKey(Hire)
