from django.db import models

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
    t6=models.ImageField(upload_to='images/')
    def __str__(self): 
        return self.t1


class villaimage(models.Model):
    name=models.CharField(max_length=50)
    images=models.ImageField(upload_to='images/')

class Data(models.Model):
    BED = models.CharField(max_length=50)
    BATH = models.CharField(max_length=50)
    ARE = models.CharField(max_length=50)
    FLO = models.CharField(max_length=50)
    PAR = models.CharField(max_length=50)
    IMG = models.ImageField(upload_to='images/')
