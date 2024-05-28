from django.db import models

# Create your models here.
class customer_data(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)


class customer_info(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
 #
 # customer= customer(id=12,firestname='sohag',lastname='hossen',email=sohag@gmail.com)
 #  customer.save()cd .
