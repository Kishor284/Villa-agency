from django.db import models

# Create your models here.

class signup(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=50)
    gmail=models.CharField(max_length=50)