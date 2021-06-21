from django.db import models

# Create your models here.
class users(models.Model):
    uid=models.CharField(max_length=50,primary_key=True)
    name=models.CharField(max_length=50)

class govt(models.Model):
    uid = models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    ph_no = models.CharField(max_length=10)
    tax_amt = models.IntegerField(default=0)