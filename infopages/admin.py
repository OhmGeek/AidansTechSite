from django.contrib import admin
from .models import InfoPage
# Register your models here.
class InfoPageAdmin(admin.ModelAdmin):
    pass


# register model admin with djadmin.

admin.site.register(InfoPage, InfoPageAdmin)
