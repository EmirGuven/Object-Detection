from django.db import models

# Create your models here.

class Object_Data(models.Model):
    Object_Id = models.IntegerField()
    Name = models.CharField(max_length=50)
    Object_Dimensions = models.CharField(max_length=50)