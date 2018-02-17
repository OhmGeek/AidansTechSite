from django.db import models
from tech.models import TechItem
# Create your models here.

class Hire(models.Model):
    """ A requested hire """
    booking_name = models.CharField(max_length=250)
    hirer_name = models.CharField(max_length=100)
    invoice_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    date_out = models.DateTimeField()
    date_in = models.DateTimeField()
    contact_number = models.CharField(max_length=20)
    waive_charges = models.BooleanField(default=False)

    @property
    def total_hire_cost(self):
        if(waive_charges):
            return 0.00 # free
        # Otherwise calculate
        total = 0.00
        items_hired = ItemHire.objects.filter(hire=self.pk)
        for item in items_hired:
            total += item.item.cost
            return total

class ItemHire(models.Model):
    """ Specific items to hire """
    item = models.ForeignKey(TechItem)
    hire = models.ForeignKey(Hire)
