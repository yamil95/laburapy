from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from applications.profesiones.models import Profesion
from applications.licitacion.models import Licitacion
from django.conf import settings
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
    profesiones = models.ManyToManyField(Profesion,related_name="profesiones")
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
    licitaciones = models.ManyToManyField(Licitacion, through="Propuesta")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['full_name',"modo_usuario"]

    objects = UserManager()

    def get_short_name(self):
        return self.email 
    
    def get_full_name(self):
        return self.full_name
    def __str__(self) -> str:
        return self.full_name + "-" + str (self.dni) 

CHOICES_MP = (("MP","MERCADO PAGO"),("TR","TRANSFERENCIA"),("EF","EFECTIVO"))

class Propuesta(models.Model):

    trabajador = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="trabajador", on_delete=models.CASCADE)
    licitacion = models.ForeignKey(Licitacion, related_name="licitacion_re", on_delete=models.CASCADE)
    presupuesto = models.FloatField("presupuesto")
    medios_de_pago = models.CharField("medios de pago", max_length=2,choices=CHOICES_MP)
    duracion = models.IntegerField("dias de trabajo",default=0)
    win  = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Propuesta"
        verbose_name_plural = "Propuestas"


    def __str__(self):
        return  self.trabajador.full_name + "-" + self.licitacion.nombre


