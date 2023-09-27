from django.db import models

# Create your models here.

class Store(models.Model):
    uid = models.CharField(max_length=32, primary_key=True)
    data = models.TextField();
    summary = models.TextField();