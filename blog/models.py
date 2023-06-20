from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True)