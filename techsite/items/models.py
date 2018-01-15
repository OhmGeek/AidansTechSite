from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    day_hire_price = models.DecimalField(max_digits=6, decimal_places=2)
    details_json = models.TextField() #Storing JSON as a text field, as no full support of JSON

    def __str__(self):
        return self.name
