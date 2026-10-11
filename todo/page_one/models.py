from django.db import models
from django.db.models import CharField


class Checkboxes(models.Model):
    checked = models.BooleanField(default=None)


class Tasks(models.Model):
    conn = models.ManyToManyField(Checkboxes)
    task = models.CharField(max_length=200, blank=True)



