from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    descript = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
