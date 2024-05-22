from django.db import models
from django.conf import settings
from applications.ubicaciones.models import Provincias,Localidades
# Create your models here.
class Trabajo(models.Model):
    """Model definition for Trabajo."""

    nombre = models.CharField("nombre proyecto", max_length=100,blank=False)
    solicitante_id = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="trabajo_solicitante", on_delete=models.CASCADE)
    trabajador_id = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="trabajo_trabajador", on_delete=models.CASCADE)
    descripcion = models.TextField("descripcion del proyecto",blank=False)
    fecha_creacion  = models.DateField("fecha",auto_now_add=True)
    estado  = models.BooleanField("estado proyecto",default=False)
    provincia = models.ForeignKey(Provincias, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidades, on_delete=models.CASCADE)
    subtrabajos = models.ManyToManyField('self', blank=True, related_name='trabajos_padre')
    
    class Meta:
        """Meta definition for Trabajo."""

        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'

    def __str__(self):
        """Unicode representation of Trabajo."""
        return self.nombre 
