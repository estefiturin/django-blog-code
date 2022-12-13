from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    #importante para cambiar la forma de ingresar del usuario
    email = models.EmailField(unique=True)
    #añadir propiedades a los usuarios
    web_site = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    
    #cambiar que se usa para iniciar sección el usuario
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    