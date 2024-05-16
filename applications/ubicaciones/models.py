from django.db import models

# Create your models here.

class Provincias (models.Model):

    nombre = models.CharField("provincia", max_length=100)


    def __str__(self) -> str:
        return str (self.id) +"-"+ self.nombre 

class Localidades (models.Model):

    nombre = models.CharField("localidad", max_length=50)
    provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE, related_name='localidades')

    def __str__(self) -> str:
        return str(self.id)+ "-"+ self.nombre 