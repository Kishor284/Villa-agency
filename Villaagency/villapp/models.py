from django.db import models

# Create your models here.
class signup1(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=50)
    gmail=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class adminadd(models.Model):
    total_flat_space=models.CharField(max_length=50)
    floor_no=models.IntegerField
    number_of_rooms=models.IntegerField
    parking_available=models.CharField(max_length=50)
    payment_process=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images') 
    description=models.CharField(max_length=250) 