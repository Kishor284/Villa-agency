from django.db import models
from os.path import basename

# Create your models here.
class signup1(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50) 
    phoneno=models.CharField(max_length=50)
    gmail=models.CharField(max_length=50)
    password=models.CharField(max_length=50)



class sdata(models.Model):
    t1=models.CharField(max_length=55)
    t2=models.CharField(max_length=55)
    t3=models.CharField(max_length=55)
    t4=models.CharField(max_length=55)
    t5=models.CharField(max_length=55)
    t6=models.CharField(max_length=60)

    def __str__(self): 
        return self.t1



class image1(models.Model):
    name=models.CharField(max_length=60)
    uimage=models.ImageField(upload_to='images/')

    def get_image_name(self):
        return basename(self.uimage.name)