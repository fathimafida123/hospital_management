from django.db import models
class Patient(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    
