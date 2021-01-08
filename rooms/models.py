from django.db import models
import uuid
ID_FIELD_LENGTH = 16
# Create your models here.


#Definition of class Auditorium
class auditorium(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    photo = models.ImageField(upload_to='auditorium')
    name=models.CharField(max_length=50)
    capacity=models.IntegerField()
    water_f=models.BooleanField()
    toilet_f=models.BooleanField()
    snacks_f=models.BooleanField()
    wifi_f=models.BooleanField()
    address=models.CharField(max_length=50)
    rating=models.FloatField()
    pricePH=models.DecimalField(max_digits=10, decimal_places=4)


#Definition of class ComputerLab
class computerlab(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    photo = models.ImageField(upload_to='auditorium')
    name=models.CharField(max_length=50)
    system_specs=models.CharField(max_length=50)
    capacity=models.IntegerField()
    water_f=models.BooleanField()
    toilet_f=models.BooleanField()
    snacks_f=models.BooleanField()
    wifi_f=models.BooleanField()
    address=models.CharField(max_length=50)
    rating=models.FloatField()
    pricePH=models.DecimalField(max_digits=10, decimal_places=4)


#Definition of class Conference
class conference(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    photo = models.ImageField(upload_to='auditorium')
    name=models.CharField(max_length=50)
    capacity=models.IntegerField()
    water_f=models.BooleanField()
    toilet_f=models.BooleanField()
    snacks_f=models.BooleanField()
    wifi_f=models.BooleanField()
    address=models.CharField(max_length=50)
    rating=models.FloatField()
    pricePH=models.DecimalField(max_digits=10, decimal_places=4)
