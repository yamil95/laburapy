from django.db import models
# Create your models here.
class Profesion(models.Model):

    name = models.CharField("nombre", max_length=100)
       

    class Meta:
        verbose_name = "Profesion"
        verbose_name_plural = "Profesions"

    def __str__(self):
        return self.name


