from django.db import models


# Create your models here.

class Desh_inf(models.Model):
    desh_name = models.CharField(max_length=50)
    desh_age = models.IntegerField()
