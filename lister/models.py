from django.db import models

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    
class Type(models.Model):
    nom = models.CharField(max_length=50, unique=True)

class Info(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    typ = models.ForeignKey(Type, on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    hostname = models.CharField(max_length=100)
