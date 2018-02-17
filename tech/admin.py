from django.contrib import admin
from .models import TechItem


# Register your models here.



class ItemAdmin(admin.ModelAdmin):
    pass


# register model admin with djadmin.

admin.site.register(TechItem, ItemAdmin)
