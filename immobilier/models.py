from django.db import models
from django.contrib.auth.models import User


# PROFIL UTILISATEUR
class Profil(models.Model):
    TYPE_USER = (
        ('client', 'Client'),
        ('proprietaire', 'Propriétaire'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profil")
    type_user = models.CharField(max_length=20, choices=TYPE_USER)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


# MAISON
class Maison(models.Model):

    nom = models.CharField(max_length=200)
    localisation = models.CharField(max_length=200)
    prix = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='maisons/')
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


# TEMOIGNAGES
class Temoignage(models.Model):

    nom = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.nom


# CONTACT
class Contact(models.Model):

    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.nom