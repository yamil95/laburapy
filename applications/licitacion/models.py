from django.db import models
from django.conf import settings
# Create your models here.

CHOICES_STATUS = (("A","in progress"),("B","finalized"))
class Licitacion(models.Model):
    """Model definition for Licitacion."""
    nombre = models.CharField("proyecto", max_length=50,unique=True)
    solicitante_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="solicitante_rela", on_delete=models.CASCADE)
    trabajador_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="trabajador_rela", on_delete=models.CASCADE)
    estado  = models.CharField("estado_licitacion", max_length=1,choices=CHOICES_STATUS)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Licitacion."""

        verbose_name = 'Licitacion'
        verbose_name_plural = 'Licitacions'

    def __str__(self):
        """Unicode representation of Licitacion."""
        return self.nombre
