from django.db import models
# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=50, unique=True)

class Partenaire(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    
class Type(models.Model):
    nom = models.CharField(max_length=50, unique=True)

class Info(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    partenaire = models.ForeignKey(Partenaire, on_delete=models.CASCADE)
    typ = models.ForeignKey(Type, on_delete=models.CASCADE)
    marge = models.FloatField()
    récurrent = models.FloatField()
    etat = models.CharField(max_length=50)
    facturé = models.CharField(max_length=100)
    dateCreation = models.DateField(max_length=100)
    dateCloture = models.DateField(max_length=100)

ok