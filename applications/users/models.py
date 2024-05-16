from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    MODE_CHOICES = (
        ('S', 'solicitante'),
        ('T', 'trabajador'),
    )

    email = models.EmailField(unique=True)
    dni = models.CharField('dni', max_length=100)
    full_name = models.CharField('Nombres', max_length=100)
    profesion = models.CharField(
        'profesion',
        max_length=50, 
        blank=True
    )
    genero = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )
    date_birth = models.DateField(
        'Fecha de nacimiento', 
        blank=True,
        null=True
    )

    #
    modo_usuario = models.CharField(
        max_length=1, 
        choices=MODE_CHOICES, 
        blank=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name',"modo_usuario"]

    objects = UserManager()

    def get_short_name(self):
        return self.email
    
    def get_full_name(self):
        return self.full_name
