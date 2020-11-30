from django.db import models

# Create your models here.
class DoctorRegister(models.Model):
    Name=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Phone=models.IntegerField()

class BloodRegister(models.Model):
    Name= models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Number = models.IntegerField()
    Age = models.IntegerField()
    Test = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)

class VitaminRegister(models.Model):
    Name= models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Number = models.IntegerField()
    Age = models.IntegerField()
    Test = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)

class HormoneRegister(models.Model):
    Name= models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Number = models.IntegerField()
    Age = models.IntegerField()
    Test = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)

class SerologyRegister(models.Model):
    Name= models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Number = models.IntegerField()
    Age = models.IntegerField()
    Test = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)

class CopdRegister(models.Model):
    Name=models.CharField(max_length=50)
    Aadhar=models.IntegerField()
    Email=models.EmailField(max_length=50)
    Age=models.IntegerField()
    Gender=models.IntegerField()
    Weight=models.IntegerField()
    Lipcolour=models.IntegerField()
    Fev=models.CharField(max_length=50)
    Intensity=models.CharField(max_length=50)
    Temperature=models.IntegerField()
    Med=models.CharField(max_length=50)
    Pred=models.CharField(max_length=50)