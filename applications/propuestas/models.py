from django.db import models
from applications.licitacion.models import Licitacion
from django.conf import settings
# Create your models here.

CHOICES = [("A","aceptada"),("B","rechazada")]
class Propuesta(models.Model):

    precio = models.IntegerField("presupuesto",blank=False)
    licitacion = models.ForeignKey(Licitacion, related_name="licitacion_propuesta", on_delete=models.CASCADE)
    descripcion = models.TextField("descripcion",blank=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="usuario_propuesta", on_delete=models.CASCADE)
    duracion = models.IntegerField("duracion del proyecto")
    fecha = models.DateTimeField("fecha", auto_now_add=True)
    state = models.CharField("estado", max_length=1,choices=CHOICES)

    class Meta:
        verbose_name = "Propuesta"
        verbose_name_plural = "Propuestas"

    def __str__(self):
        return self.name


