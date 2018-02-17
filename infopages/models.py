from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class InfoPage(models.Model):
    title = models.CharField(max_length=120)
    content = HTMLField()
    slug = models.SlugField(max_length=20)
