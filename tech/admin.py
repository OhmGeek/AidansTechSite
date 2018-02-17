from django.contrib import admin
from .models import TechTag, TechItem


# Register your models here.

class TagAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    pass


# register model admin with djadmin.

admin.site.register(TechTag, TagAdmin)
admin.site.register(TechItem, ItemAdmin)
