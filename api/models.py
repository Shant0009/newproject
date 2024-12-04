from django.db import models
class User(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=10)
    mobilenumber=models.CharField(max_length=10)

def _str_(self):
    return self.name 